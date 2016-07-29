***Settings***
| Documentation  | All test cases on dial page | 
| Resource       | test_resource.robot | 
| Test setup     | android.ready | 
| Test teardown  | android.teardown | 


***Test Cases***
Redirect in dial page
|  | [Documentation] | Test redirection on dial page | 
|  | [tags]          | dist | P0 | 
|  | android.login_with_password | ${phone1_number} | ${ phone1_password } | 
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
