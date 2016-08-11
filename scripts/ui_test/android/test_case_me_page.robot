***Settings***
| Documentation  | All test cases on me page | 
| Resource       | test_resource.robot | 
| Test setup     | Setup | 
| Test teardown  | Teardown | 


***Test Cases***
Redirect on me page
|  | [Documentation] | Test redirection on me page | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} | 
|  | android.verify  | ${me_location_settings} | 
|  | android.click   | ${me_location_settings} | 
|  | android.verify  | ${settings_location_exit} | 
|  | android.click   | ${settings_location_back} | 
|  | android.verify  | ${me_location_user_profile} | 
|  | android.click   | ${me_location_user_profile} | 
|  | android.verify  | ${me_user_profile_location_title} | 
|  | android.click   | ${me_user_profile_location_back} | 
|  | android.verify  | ${me_location_user_account} | 
|  | android.click   | ${me_location_user_account} | 
|  | android.verify  | ${me_balance_location_title} | 
|  | android.click   | ${me_balance_location_back} | 
|  | android.verify  | ${me_location_user_personalization} | 
|  | android.click   | ${me_location_user_personalization} | 
|  | android.verify  | ${me_personality_location_title} | 
|  | android.click   | ${me_personality_location_back} | 
|  | android.verify  | ${me_location_user_vip_btn} | 
|  | android.click   | ${me_location_user_vip_btn} | 
|  | android.verify  | ${me_vip_location_title} | 
|  | android.click   | ${me_vip_location_back} | 
|  | android.verify  | ${me_location_donate_vip} | 
|  | android.click   | ${me_location_donate_vip} | 
|  | android.verify  | ${me_send_vip_location_title} | 
|  | android.click   | ${me_send_vip_location_back} | 
|  | android.verify  | ${me_location_title} | 
