***Settings***
| Documentation  | All test cases for login & logout scenarios | 
| Resource       | test_resource.robot | 
| Test setup     | android.ready | 
| Test teardown  | android.teardown | 


***test cases***
Log in with password and log out
|  | [Documentation] | Log in with password and log out | 
|  | [tags]          | smoke | regression | 
|  | android.login_with_password | ${phone1_number} | ${phone1_password} | 
|  | android.logout | 
