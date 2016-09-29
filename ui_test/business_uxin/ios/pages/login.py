#-*- coding: UTF-8 -*-

## Location info
## pagename_location_name = "xxxxx"
# Verify code mode login page
verify_code_login_location_login_title = u"现在登录，让故事发生"
verify_code_login_location_phone_number = "UIATarget.localTarget().frontMostApp().windows()[0].textFields()[0]"
verify_code_login_location_country_code = "UIATarget.localTarget().frontMostApp().windows()[0].buttons()[0]"
verify_code_login_location_country_code_text = "UIATarget.localTarget().frontMostApp().windows()[0].staticTexts()[1]"
verify_code_login_location_verify_code = "UIATarget.localTarget().frontMostApp().windows()[0].textFields()[1]"
verify_code_login_location_get_verify_code = "UIATarget.localTarget().frontMostApp().windows()[0].buttons()[1]"
verify_code_login_location_login_btn = u"登录"
verify_code_login_location_use_password = u"使用密码登录"
verify_code_login_location_agreement = u"登录默认同意《有信服务条款》"

# Password mode login page
password_login_location_login_title = verify_code_login_location_login_title
password_login_location_phone_number = verify_code_login_location_phone_number 
password_login_location_country_code = verify_code_login_location_country_code
password_login_location_country_code_text = verify_code_login_location_country_code_text
password_login_location_password = "UIATarget.localTarget().frontMostApp().windows()[0].secureTextFields()[0]"
password_login_location_login_btn = verify_code_login_location_login_btn
password_login_location_forget_password = u"忘记密码"
password_login_location_use_verify_code = u"使用验证码登录"
password_login_location_agreement = verify_code_login_location_agreement


## Verification info
## pagename_verification_name = "xxxxx"
# Verify code mode login page
verify_code_login_verification_login_title = u"现在登录，让故事发生"
verify_code_login_verification_phone_number_placeholder = u"请输入手机号码"
verify_code_login_verification_country_code_china = u"中国 +86"
verify_code_login_verification_verify_code_placeholder = u"请输入验证码"
verify_code_login_verification_get_verify_code = u"获取验证码"
verify_code_login_verification_resend_verify_code = u"重新发送"
verify_code_login_verification_login_btn_text = u"登录"
verify_code_login_verification_use_password = u"使用密码登录"
verify_code_login_verification_agreement = u"登录默认同意《有信服务条款》"

# Password mode login page
password_login_verification_login_title = verify_code_login_verification_login_title
password_login_verification_phone_number_placeholder = verify_code_login_verification_phone_number_placeholder
password_login_verification_country_code_china = verify_code_login_verification_country_code_china
password_login_verification_login_btn_text = verify_code_login_verification_login_btn_text
password_login_verification_forget_password = u"忘记密码"
password_login_verification_use_verify_code = u"使用验证码登录"
password_login_verification_agreement = verify_code_login_verification_agreement
