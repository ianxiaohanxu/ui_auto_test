*** Settings ***
Documentation     All test cases on contact page
Test Setup        Setup
Test Teardown     Teardown
Resource          test_resource.robot

*** Test Cases ***
Redirect on contact page
    [Documentation]    Test redirection on contact page
    [Tags]    dist    P0    Regression
    android.login_with_password    ${username}    ${ password }
    android.click    ${bottom_location_contact}
    android.verify    ${contact_location_add_new}
    android.click    ${contact_location_add_new}
    android.press    Back
    android.verify    ${contact_location_search}
    android.click    ${contact_location_search}
    android.verify    ${contact_search_location_input_cancel}
    android.click    ${contact_search_location_input_cancel}
    android.verify    ${contact_location_invite}
    android.click    ${contact_location_invite}
    android.verify    ${contact_invite_location_qq_btn}
    android.click    ${contact_invite_location_back}
    android.verify    ${contact_location_direct_num}
    android.click    ${contact_location_direct_num}
    android.verify    ${contact_direct_location_title}
    android.click    ${contact_direct_location_back}
    android.verify    ${contact_location_title}

Search Contact
    [Documentation]    Search a contact
    [Tags]    P0    Regression
    android.loginwithpassword    ${username}    ${password}
    android.click    ${bottom_location_contact }
    sleep    5
    android.verify    ${contact_location_title }
    android.click    ${contact_location_search }
    android.click    ${contact_search_location_input_cancel }
    android.verify    ${contact_location_title }
    android.click    ${contact_location_search }
    ${yxt}    converttostring    有信团
    android.enter    ${yxt}    ${contact_search_location_input_field }
    ${yxtd}    converttostring    有信团队
    android.verify    ${yxtd}

Delete a contact
    [Documentation]    delete a contact #执行前需要手动添加一个“adeletephone1”的联系人
    [Tags]    P0    Regression
    android.loginwithpassword    ${username}    ${password}
    android.click    ${bottom_location_contact }
    sleep    5
    android.verify    ${contact_location_title}
    android.longclick    adeletephone1    duration=5000
    android.verify    ${contact_longclick_dialogbox_location_lookup }
    android.verify    ${contact_longclick_dialogbox_location_edit_contact }
    android.verify    ${contact_longclick_dialogbox_location_delete_contact }
    android.verify    ${contact_longclick_dialogbox_location_add_collection }
    android.verify    ${contact_longclick_dialogbox_location_cancle }
    android.click    ${contact_longclick_dialogbox_location_cancle}
    android.verify    ${contact_location_title }
    android.longclick    adeletephone1    duration=5000
    android.click    ${contact_longclick_dialogbox_location_delete_contact }
    android.verify    ${contact_confirm_delete_dialogbox_location_message }
    android.click    ${contact_confirm_delete_dialogbox_location_ok }
    sleep    35
    ${bool}    iselementpresent    adeletephone1
    ${boolstr}    converttostring    ${bool}
    Log    ${boolstr}
    shouldbeequal    False    ${boolstr}
