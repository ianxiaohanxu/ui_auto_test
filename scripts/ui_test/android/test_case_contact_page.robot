***Settings***
| Documentation  | All test cases on contact page | 
| Resource       | test_resource.robot | 
| Test setup     | android.ready | 
| Test teardown  | android.teardown | 


***Test Cases***
Redirect on contact page
|  | [Documentation] | Test redirection on contact page | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${phone1_number} | ${ phone1_password } | 
|  | android.click   | ${bottom_location_contact} | 
|  | android.verify  | ${contact_location_add_new} | 
|  | android.click   | ${contact_location_add_new} | 
|  | android.verify  | ${new_contact_location_cancel} | 
|  | android.click   | ${new_contact_location_cancel} | 
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


