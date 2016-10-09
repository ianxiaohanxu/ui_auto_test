***Settings***
| Documentation  | All test cases on me page | 
| Resource       | test_resource.robot | 
| Test setup     | Setup | 
| Test teardown  | Teardown | 

***Test Cases***
Check Me Page > Account balance > U account book
|  | [Documentation] | ensure u account book page exists | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} |
|  | android.click   | ${bottom_location_me} |
|  | android.verify  | ${me_location_account_balance} |
|  | android.click   | ${me_location_account_balance} |
|  | android.verify  | ${me_account_balance_verification_title} |


|  | android.verify  | ${me_account_balance_U_account_book_verification_title} |

#|  | android.click   | ${me_account_balance_location_U_account_book} |
#|  | android.click   | ${account_book_verification_title} |

|  | android.verify  | ${me_account_balance_U_account_book_verification_title} |
|  | android.click   | ${me_account_balance_U_account_book_location_rule} |
|  | android.verify  | ${me_account_balance_rule_verification_title} |
|  | android.press   | Back | 
|  | android.verify  | ${me_account_balance_U_account_book_verification_title} |
|  | android.press   | Back | 
|  | android.verify  | ${me_account_balance_verification_title} |
|  | android.press   | Back | 
|  | android.verify  | ${me_verification_title} |



