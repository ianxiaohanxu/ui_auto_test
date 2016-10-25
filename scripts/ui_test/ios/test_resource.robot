***Settings***
| Documentation  | *Define some resource here(e.g. Library, Keywords, Variables)* | 
| Library        | ui_test.ios | WITH NAME | ios | 
| Variables      | ui_test/business_uxin/ios/pages/all_pages.py | 
| Variables      | ui_test/business_uxin/testdata.py | 
| Variables      | ui_test/platform/constant.py | 

***Keywords***
Setup
|  | ${username}   | ${password} | ios.get_account | 
|  | set test variable | ${username} | 
|  | set test variable | ${password} | 
|  | ios.ready | 

Teardown
|  | ios.free_account | ${username} | 
|  | ios.teardown | 
