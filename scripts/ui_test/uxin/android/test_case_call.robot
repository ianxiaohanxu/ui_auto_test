***Settings***
| Documentation  | All test cases for call scenarios | 
| Resource       | test_resource.robot | 
| Test setup     | Setup | 
| Test teardown  | Teardown | 


***Test Cases***
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
|  | android.verify  | ${calling_location_hang_up} | 
|  | android.click   | ${calling_location_hang_up} | 
|  | android.verify  | ${bottom_location_dial} | 
