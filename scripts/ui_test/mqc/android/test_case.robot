***Settings***
| Documentation  | All test cases for login & logout scenarios | 
| Resource       | test_resource.robot | 
| Test setup     | Setup | 
| Test teardown  | Teardown | 


***test cases***
Log in with password and log out
|  | [Documentation] | Log in with password and log out | 
|  | [tags]          | dist | P0 | regression | 
|  | android.login_with_password | ${username} | ${password} | 
|  | android.logout | 

Redirect in dial page
|  | [Documentation] | Test redirection on dial page | 
|  | [tags]          | dist | P0 | regression | 
|  | android.login_with_password | ${username} | ${password} | 
|  | android.verify  | ${dial_location_top_left_ad} | 
|  | android.click   | ${dial_location_top_left_ad} | 
|  | android.verify  | ${webview_location_view_area} | 
|  | android.press   | Back | 
|  | android.verify  | ${dial_location_multi_call} | 
|  | android.click   | ${dial_location_multi_call} | 
|  | android.verify  | ${multi_call_contact_location_selected_bar} | 
|  | android.click   | ${multi_call_contact_location_back} | 
|  | android.verify  | ${dial_location_search_bar} | 
|  | android.click   | ${dial_location_search_bar} | 
|  | android.verify  | ${contact_search_location_input_cancel} | 
|  | android.click   | ${contact_search_location_input_cancel} | 
|  | android.verify  | ${bottom_location_dial} | 
|  | android.click   | ${bottom_location_dial} | 
|  | android.verify  | ${dial_location_keypad} | 

Redirect on contact page
|  | [Documentation] | Test redirection on contact page | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${password} | 
|  | android.click   | ${bottom_location_contact} | 
|  | android.verify  | ${contact_location_add_new} | 
|  | android.click   | ${contact_location_add_new} | 
|  | android.press   | Back | 
|  | android.verify  | ${contact_location_search} | 
|  | android.click   | ${contact_location_search} | 
|  | android.verify  | ${contact_search_location_input_cancel} | 
|  | android.click   | ${contact_search_location_input_cancel} | 
|  | android.verify  | ${contact_location_invite} | 
|  | android.click   | ${contact_location_invite} | 
|  | android.verify  | ${contact_invite_location_qq_btn} | 
|  | android.click   | ${contact_invite_location_back} | 
|  | android.verify  | ${contact_location_direct_num} | 
|  | android.click   | ${contact_location_direct_num} | 
|  | android.verify  | ${contact_direct_location_title} | 
|  | android.click   | ${contact_direct_location_back} | 
|  | android.verify  | ${contact_location_title} | 

Redirect on discovery page
|  | [Documentation] | Test redirection on discovery page | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${password} | 
|  | android.click   | ${bottom_location_discovery} | 
|  | android.verify  | ${discovery_location_random_call} | 
|  | android.click   | ${discovery_location_random_call} | 
|  | android.verify  | ${random_call_location_charm} | 
|  | android.click   | ${random_call_location_back} | 
|  | android.verify  | ${discovery_location_title} | 

Redirect on me page
|  | [Documentation] | Test redirection on me page | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${password} | 
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

Initial a call and hang up before answer
|  | [Documentation] | Make a call, check the UI, and hang up before it anwsered. | 
|  | [tags]          | regression | P1 | dist |
|  | android.login_with_password | ${username} | ${password} | 
|  | android.click   | ${bottom_location_dial} | 
|  | android.verify  | ${dial_location_keypad} | 
|  | android.click   | ${dial_location_keypad_one} | 
|  | android.click   | ${dial_location_keypad_three} |
|  | android.click   | ${dial_location_keypad_zero} | 
|  | android.click   | ${dial_location_keypad_zero} | 
|  | android.click   | ${dial_location_keypad_zero} | 
|  | android.click   | ${dial_location_keypad_zero} | 
|  | android.click   | ${dial_location_keypad_zero} | 
|  | android.click   | ${dial_location_keypad_zero} | 
|  | android.click   | ${dial_location_keypad_zero} | 
|  | android.click   | ${dial_location_keypad_zero} | 
|  | android.click   | ${dial_location_keypad_zero} | 
|  | ${num}          | android.text  | ${dial_location_phone_number} | 
|  | Should be Equal | ${num} | 130-0000-0000 | 
|  | android.click   | ${bottom_location_call} | 
|  | android.make_call | 
|  | android.verify  | ${calling_location_avatar} | 
|  | android.verify  | ${calling_location_call_name} | 
#|  | ${status_text}  | android.text  | ${calling_location_call_status} | 
#|  | Should be Equal | ${status_text} | ${calling_verification_call_status_ringing} | 
|  | android.verify  | ${calling_location_hang_up} | 
|  | android.click   | ${calling_location_hang_up} | 
|  | android.verify  | ${bottom_location_dial} | 
