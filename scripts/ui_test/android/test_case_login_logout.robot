| *** Settings *** |
| Documentation  | All test cases for login & logout scenarios |
| Test Setup     | Setup |
| Test Teardown  | Teardown |
| Resource       | test_resource.robot |
| Library        | ../../../Resources/tools_library.py |

| *** test cases *** |
| Log in with password and log out |
|    | [Documentation] | Log in with password and log out |
|    | [Tags] | dist | regression | P0 |
|    | android.login_with_password | ${username} | ${password} |
|    | android.logout |

| Login with verity code |
|    | android.verify | ${verify_code_login_location_country_code} |
|    | android.click | ${verify_code_login_location_country_code} |
|    | android.verify | ${verify_code_login_location_country_usual_area} |
|    | android.click | ${verify_code_login_location_country_code_china} |
|    | android.verify | ${verify_code_login_location_login_title} |
|    | ${username} | ${password} | android.get_account |
|    | android.enter | ${username} | ${verify_code_login_location_phone_number} |
|    | android.click | ${verify_code_login_location_get_verify_code} |
|    | ${result} | get_login_ac | ${username} |
|    | log | ${result} |
|    | android.enter | ${result} | ${verify_code_login_location_verify_code} |
|    | android.click | ${verify_code_login_location_login_btn} |
|    | ${res} | android.is_element_present | ${bottom_location_me} | ${5} |
|    | Run Keyword If | '${res}'=='True' | android.verify | ${bottom_location_me} |
|    | ... | ELSE | Run Keywords | android.verify | ${auth_verification_title } |
|    | ... | AND | android.verify | ${auth_verification_contact_permission_text } |

| Login with forget password |
|    | android.verify | ${verify_code_login_location_use_password} |
|    | android.click | ${verify_code_login_location_use_password} |
|    | android.verify | ${password_login_verification_forget_password} |
|    | android.click | ${password_login_verification_forget_password} |
|    | android.verify | ${forget_password_verification_title} |
|    | android.click | ${forget_password_location_country_code} |
|    | android.verify | ${forget_password_location_country_usual_area} |
|    | android.click | ${forget_password_location_country_code_china} |
|    | ${username} | ${password} | android.get_account |
|    | android.enter | ${username} | ${verify_code_login_location_phone_number} |
|    | android.click | ${verify_code_login_location_get_verify_code} |
|    | ${result} | get_login_ac | ${username} |
|    | android.enter | ${result} | ${verify_code_login_location_verify_code} |
|    | android.click | ${forget_password_location_next} |
|    | android.verify | ${forget_password_location_sumit_btn} |
|    | android.enter | 111333 | ${forget_password_location_eidt_password} |
|    | android.click | ${forget_password_location_sumit_btn} |
|    | android.verify | ${forget_password_location_change_success} |
|    | android.click | ${forget_password_location_change_sumit_btn} |
|    | ${res} | android.is_element_present | ${bottom_location_me} | ${5} |
|    | Run Keyword If | '${res}'=='True' | android.verify | ${bottom_location_me} |
|    | ... | ELSE | Run Keywords | android.verify | ${auth_verification_title } |
|    | ... | AND | android.verify | ${auth_verification_contact_permission_text } |
