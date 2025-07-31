<?php

namespace Database\Seeders;


use Dipokhalder\EnvEditor\EnvEditor;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Artisan;
use Smartisan\Settings\Facades\Settings;


class MailTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $envService = new EnvEditor();

        Settings::group('mail')->set([
            'mail_mailer'     => 'smtp',
            'mail_host'       => env('MAIL_HOST', ''),
            'mail_port'       => env('MAIL_PORT', 587),
            'mail_username'   => env('MAIL_USERNAME', ''),
            'mail_password'   => env('MAIL_PASSWORD', ''),
            'mail_encryption' => env('MAIL_ENCRYPTION', 'tls'),
            'mail_from_name'  => env('MAIL_FROM_NAME', 'BUYPEER'),
            'mail_from_email' => env('MAIL_FROM_ADDRESS', '')
        ]);

        $envService->addData([
            'MAIL_MAILER'       => 'smtp',
            'MAIL_HOST'         => env('MAIL_HOST', ''),
            'MAIL_PORT'         => env('MAIL_PORT', 587),
            'MAIL_USERNAME'     => env('MAIL_USERNAME', ''),
            'MAIL_PASSWORD'     => env('MAIL_PASSWORD', ''),
            'MAIL_ENCRYPTION'   => env('MAIL_ENCRYPTION', 'tls'),
            'MAIL_FROM_NAME'    => env('MAIL_FROM_NAME', 'BUYPEER'),
            'MAIL_FROM_ADDRESS' => env('MAIL_FROM_ADDRESS', '')
        ]);
        Artisan::call('optimize:clear');
    }
}
