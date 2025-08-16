<?php

namespace App\Http\Requests;

use App\Services\InstallerService;
use Dipokhalder\EnvEditor\EnvEditor;
use Illuminate\Foundation\Http\FormRequest;

class LicenseRequest extends FormRequest
{
    /**
     * Determine if the user is authorized to make this request.
     *
     * @return bool
     */
    public function authorize(): bool
    {
        return true;
    }

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array
     */
    public function rules(): array
    {
        return [
            'license_key' => ['required', 'string', 'max:500'],
        ];
    }

    public function messages(): array
    {
        return [
            'license_key.required' => 'The license code field is required.',
        ];
    }

    public function withValidator($validator): void
    {
        // License step disabled: skip side-effects
    }
}
