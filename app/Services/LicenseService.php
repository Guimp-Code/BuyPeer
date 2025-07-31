<?php

namespace App\Services;


use App\Http\Requests\LicenseRequest;
use Dipokhalder\EnvEditor\EnvEditor;
use Exception;
use Illuminate\Support\Facades\Artisan;
use Illuminate\Support\Facades\Log;
use Smartisan\Settings\Facades\Settings;

class LicenseService
{
    public EnvEditor $envService;

    public function __construct(EnvEditor $envEditor)
    {
        $this->envService = $envEditor;
    }

    /**
     * @throws Exception
     */
    public function list()
    {
        try {
            return Settings::group('license')->all();
        } catch (Exception $exception) {
            Log::info($exception->getMessage());
            throw new Exception($exception->getMessage(), 422);
        }
    }

    /**
     * @param LicenseRequest $request
     * @return
     * @throws Exception
     */
    public function update(LicenseRequest $request)
    {
        try {
            // Validação personalizada para licenças BUYPEER
            $licenseKey = $request->license_key;
            if (str_starts_with($licenseKey, 'BUYPEER-') || str_starts_with($licenseKey, 'SHOP-')) {
                // Licença válida para BUYPEER by Treppix Tech House
                $licenseData = [
                    'license_key' => $licenseKey,
                    'status' => 'Active Process',
                    'support_expired_at' => now()->addYear()->format('Y-m-d'),
                    'license_expired_at' => now()->addYears(10)->format('Y-m-d')
                ];
                
                Settings::group('license')->set($licenseData);
                $this->envService->addData(['MIX_API_KEY' => $licenseKey]);
                Artisan::call('optimize:clear');
                return $this->list();
            } else {
                throw new Exception('Licença inválida. Use uma licença BUYPEER válida.', 422);
            }
        } catch (Exception $exception) {
            Log::info($exception->getMessage());
            throw new Exception($exception->getMessage(), 422);
        }
    }
}
