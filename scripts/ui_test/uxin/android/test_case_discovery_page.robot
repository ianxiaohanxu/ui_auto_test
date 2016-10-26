***Settings***
| Documentation  | All test cases on discovery page | 
| Resource       | test_resource.robot | 
| Test setup     | Setup | 
| Test teardown  | Teardown | 


***Test Cases***
Redirect on discovery page
|  | [Documentation] | Test redirection on discovery page | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_discovery} | 
|  | android.verify  | ${discovery_location_random_call} | 
|  | android.click   | ${discovery_location_random_call} | 
|  | android.verify  | ${random_call_location_charm} | 
|  | android.click   | ${random_call_location_back} | 
|  | android.verify  | ${discovery_location_title} | 
