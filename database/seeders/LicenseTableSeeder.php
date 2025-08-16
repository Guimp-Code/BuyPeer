<?php

namespace Database\Seeders;


use Dipokhalder\EnvEditor\EnvEditor;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Artisan;
use Smartisan\Settings\Facades\Settings;

class LicenseTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run(): void
    {
        $envService = new EnvEditor();
        Settings::group('license')->set([
            'license_key' => env('MIX_API_KEY', 'BUYPEER-123456-TREPPIX-2025')
        ]);
        if (env('MIX_DEMO', false)) {
            Settings::group('license')->set([
                'license_key' => 'i9u99tt4-f0w6-71w7-8394-y968t02516r11'
            ]);
            // API Key should be set via environment variable MIX_API_KEY
            Artisan::call('optimize:clear');
        }
    }
}
