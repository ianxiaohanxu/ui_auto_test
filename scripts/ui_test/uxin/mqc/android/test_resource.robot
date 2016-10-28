| *** Settings *** |
| Documentation  | *Define some resource here(e.g. Library, Keywords, Variables)* |
| Library        | ui_test.android | WITH NAME | android |
| Variables      | ui_test/business_uxin/android/pages/all_pages.py |
| Variables      | ui_test/business_uxin/testdata.py |
| Variables      | ui_test/platform/constant.py |

| *** Keywords *** |
| Setup |
|    | [Arguments]  | ${stype}=normal | 
|    | ${username} | ${password} | android.get_account | ${stype} |
|    | set test variable | ${username} |
|    | set test variable | ${password} |
|    | android.ready |

| Teardown |
|    | [Arguments]  | 
|    | android.free_account | ${username} |
|    | android.teardown |

