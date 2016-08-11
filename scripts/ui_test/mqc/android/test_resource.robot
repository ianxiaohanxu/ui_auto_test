***Settings***
| Documentation  | *Define some resource here(e.g. Library, Keywords, Variables)* | 
| Library        | ui_test.android | WITH NAME | android | 
| Variables      | ui_test/business/android/pages/all_pages.py | 
| Variables      | ui_test/business/testdata.py | 
| Variables      | ui_test/platform/constant.py | 

***Keywords***
Setup
|  | ${username}   | ${password} | android.get_account | 
|  | set test variable | ${username} | 
|  | set test variable | ${password} | 
|  | android.ready | 

Teardown
|  | android.free_account | ${username} | 
|  | android.teardown | 