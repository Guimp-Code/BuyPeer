<?php

namespace App\Http\Resources;


use App\Models\ThemeSetting;
use Illuminate\Http\Resources\Json\JsonResource;

class SettingResource extends JsonResource
{

    public array $info;

    public function __construct($info)
    {
        parent::__construct($info);
        $this->info = $info;
    }

    public function toArray($request): array
    {
		return [
			'company_name'                          => $this->info['company_name']                          ?? 'Toriba',
			'company_email'                         => $this->info['company_email']                         ?? '',
			"company_calling_code"                  => $this->info['company_calling_code']                  ?? '+55',
			'company_phone'                         => $this->info['company_phone']                         ?? '',
			'company_country_code'                  => $this->info['company_country_code']                  ?? 'BRA',
			'company_address'                       => $this->info['company_address']                       ?? '',
			'site_default_language'                 => $this->info['site_default_language']                 ?? 1,
			'site_android_app_link'                 => $this->info['site_android_app_link']                 ?? '',
			'site_ios_app_link'                     => $this->info['site_ios_app_link']                     ?? '',
			'site_copyright'                        => $this->info['site_copyright']                        ?? '',
			'site_currency_position'                => $this->info['site_currency_position']                ?? 5,
			'site_digit_after_decimal_point'        => $this->info['site_digit_after_decimal_point']        ?? '2',
			'site_default_currency_symbol'          => $this->info['site_default_currency_symbol']          ?? 'R$',
			'site_phone_verification'               => $this->info['site_phone_verification']               ?? 2,
			'site_email_verification'               => $this->info['site_email_verification']               ?? 1,
			'site_language_switch'                  => $this->info['site_language_switch']                  ?? 1,
			'site_online_payment_gateway'           => $this->info['site_online_payment_gateway']           ?? 2,
			'site_cash_on_delivery'                 => $this->info['site_cash_on_delivery']                 ?? 1,
			'shipping_setup_method'                 => $this->info['shipping_setup_method']                 ?? null,
			'shipping_setup_flat_rate_wise_cost'    => $this->info['shipping_setup_flat_rate_wise_cost']    ?? null,
			'shipping_setup_area_wise_default_cost' => $this->info['shipping_setup_area_wise_default_cost'] ?? null,
			'theme_logo'                            => ($this->themeImage('theme_logo'))->logo,
			'theme_footer_logo'                     => ($this->themeImage('theme_footer_logo'))->footerLogo,
			'theme_favicon_logo'                    => ($this->themeImage('theme_favicon_logo'))->faviconLogo,
			'otp_type'                              => $this->info['otp_type']                              ?? 1,
			'otp_digit_limit'                       => $this->info['otp_digit_limit']                       ?? 4,
			'otp_expire_time'                       => $this->info['otp_expire_time']                       ?? 5,
			'social_media_facebook'                 => $this->info['social_media_facebook']                 ?? '',
			'social_media_instagram'                => $this->info['social_media_instagram']                ?? '',
			'social_media_twitter'                  => $this->info['social_media_twitter']                  ?? '',
			'social_media_youtube'                  => $this->info['social_media_youtube']                  ?? '',
			'cookies_details_page_id'               => $this->info['cookies_details_page_id']               ?? 0,
			'cookies_summary'                       => $this->info['cookies_summary']                       ?? '',
			'notification_fcm_api_key'              => $this->info['notification_fcm_api_key']              ?? '',
			'notification_fcm_auth_domain'          => $this->info['notification_fcm_auth_domain']          ?? '',
			'notification_fcm_project_id'           => $this->info['notification_fcm_project_id']           ?? '',
			'notification_fcm_storage_bucket'       => $this->info['notification_fcm_storage_bucket']       ?? '',
			'notification_fcm_messaging_sender_id'  => $this->info['notification_fcm_messaging_sender_id']  ?? '',
			'notification_fcm_app_id'               => $this->info['notification_fcm_app_id']               ?? '',
			'notification_fcm_measurement_id'       => $this->info['notification_fcm_measurement_id']       ?? '',
			'notification_fcm_public_vapid_key'     => $this->info['notification_fcm_public_vapid_key']     ?? '',
			'whatsapp_status'                       => $this->info['whatsapp_status']                       ?? 2,
			'whatsapp_number'                       => $this->info['whatsapp_number']                       ?? '',
			'whatsapp_calling_code'                 => $this->info['whatsapp_calling_code']                 ?? '+55',
			'notification_audio'                    => asset('/audio/notification.mp3'),
			'image_cart'                            => asset('/images/required/empty-cart.gif'),
			'image_wishlist'                        => asset('/images/required/empty-wishlist.gif'),
			'image_app_store'                       => asset('/images/required/app-store.png'),
			'image_play_store'                      => asset('/images/required/play-store.png'),
			'image_confirm'                         => asset('/images/required/confirm.gif'),
			'image_403'                             => asset('/images/required/403.png'),
			'image_404'                             => asset('/images/required/404.png'),
			'not_found'                             => asset('/images/default/not-found/not_found.png')
		];
    }

	public function themeImage($key)
	{
		return ThemeSetting::where(['key' => $key])->first() ?? new ThemeSetting();
	}
}
