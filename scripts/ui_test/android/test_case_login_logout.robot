***Settings***
| Documentation  | All test cases for login & logout scenarios | 
| Resource       | test_resource.robot | 
| Test setup     | Setup | 
| Test teardown  | Teardown | 


***test cases***
Log in with password and log out
|  | [Documentation] | Log in with password and log out | 
|  | [tags]          | dist | regression | P0 | 
|  | android.login_with_password | ${username} | ${password} | 
|  | android.logout | 

