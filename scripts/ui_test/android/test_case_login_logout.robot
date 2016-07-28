***Settings***
| Documentation  | All test cases for login & logout scenarios | 
| Resource       | test_resource.robot | 
| Test setup     | android.ready | 
| Test teardown  | android.teardown | 


***test cases***
Log in with password and log out
|  | [Documentation] | Log in with password and log out | 
|  | [tags]          | dist | regression | 
|  | android.login_with_password | ${phone1_number} | ${phone1_password} | 
|  | android.logout | 

First launch and check welcome pages
|  | [Documentation] | First time launch the app after installation, make sure welcome pages show the corrent info. | 
|  | ...             | Also test installation and uninstallation. | 
|  | [tags]          | dist | regression | 
|  | android.remove_app | ${uxin_package_name} | 
|  | android.install_app | ${app_path} |  
|  | android.launch_app | 
|  | android.verify  | ${welcome_location_launch_btn} | 
|  | ${title_text}   | android.text | ${welcome_location_guide_title} | 
|  | Should be equal | ${title_text} | ${welcome_verification_page_1_title} | 
|  | ${content_text} | android.text | ${welcome_location_guide_content} | 
|  | Should be equal | ${content_text} | ${welcome_verification_page_1_content} | 
|  | android.swipe_left | 
|  | ${title_text}   | android.text | ${welcome_location_guide_title} | 
|  | Should be equal | ${title_text} | ${welcome_verification_page_2_title} | 
|  | ${content_text} | android.text | ${welcome_location_guide_content} | 
|  | Should be equal | ${content_text} | ${welcome_verification_page_2_content} | 
|  | android.swipe_left | 
|  | ${title_text}   | android.text | ${welcome_location_guide_title} | 
|  | Should be equal | ${title_text} | ${welcome_verification_page_3_title} | 
|  | ${content_text} | android.text | ${welcome_location_guide_content} | 
|  | Should be equal | ${content_text} | ${welcome_verification_page_3_content} | 
|  | android.click   | ${welcome_location_launch_btn} | 
|  | android.verify  | ${verify_code_login_location_login_title} | 
