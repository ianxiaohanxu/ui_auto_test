| *** Settings *** |
| Documentation  | *Define some resource here(e.g. Library, Keywords, Variables)* |
| Library        | ui_test.uxin_android | WITH NAME | android |
| Variables      | ui_test/business_uxin/android/pages/all_pages.py |
| Variables      | ui_test/business_uxin/testdata.py |
| Variables      | ui_test/platform/constant.py |

| *** Keywords *** |
| Setup |
|    | ${username} | ${password} | android.get_account |
|    | set test variable | ${username} |
|    | set test variable | ${password} |
|    | android.ready |

| Teardown |
|    | android.free_account | ${username} |
|    | android.teardown |
