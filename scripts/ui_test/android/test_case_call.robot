***Settings***
| Documentation  | All test cases for call scenarios | 
| Resource       | test_resource.robot | 
| Test setup     | android.ready | 
| Test teardown  | android.teardown | 


***Test Cases***
Initial a call and hang up before answer
|  | [Documentation] | Make a call, check the UI, and hang up before it anwsered. | 
|  | [tags]          | regression | P1 | 
|  | android.login_with_password | ${phone1_number} | ${phone1_password} | 
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
|  | android.verify  | ${calling_location_avatar} | 
|  | android.verify  | ${calling_location_call_name} | 
|  | ${status_text}  | android.text  | ${calling_location_call_status} | 
|  | Should be Equal | ${status_text} | ${calling_verification_call_status_ringing} | 

|  | android.logout  | 
