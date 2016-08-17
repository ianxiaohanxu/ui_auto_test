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
    android.verify    ${contact_location_title }
    android.verify    ${contact_location_search }
    android.click    ${contact_location_search }
    android.verify    ${contact_search_location_input_field }
    android.verify    ${contact_search_location_input_cancel }
    android.click    ${contact_search_location_input_cancel }
    android.verify    ${contact_location_title }
    android.click    ${contact_location_search }
    android.verify    ${contact_search_location_input_field }
    android.verify    ${contact_search_location_input_cancel }
    ${yxt}    converttostring    有信团
    android.enter    ${yxt}    ${contact_search_location_input_field }
    ${yxtd}    converttostring    有信团队
    android.verify    ${yxtd}

Delete a contact
    [Documentation]    delete a contact #执行前需要手动添加一个“adeletephone1”的联系人
    [Tags]    P0    Regression
    android.loginwithpassword    ${username}    ${password}
    android.click    ${bottom_location_contact }
    android.verify    ${contact_location_title}
    android.longclick    adeletephone    duration=5000
    android.verify    ${contact_longclick_dialogbox_location_lookup }
    android.verify    ${contact_longclick_dialogbox_location_edit_contact }
    android.verify    ${contact_longclick_dialogbox_location_delete_contact }
    android.verify    ${contact_longclick_dialogbox_location_add_collection }
    android.verify    ${contact_longclick_dialogbox_location_cancle }
    android.click    ${contact_longclick_dialogbox_location_cancle}
    android.verify    ${contact_location_title }
    android.longclick    adeletephone    duration=5000
    android.click    ${contact_longclick_dialogbox_location_delete_contact }
    android.verify    ${contact_confirm_delete_dialogbox_location_message }
    android.click    ${contact_confirm_delete_dialogbox_location_ok }
    android.verify    ${contact_location_title }
    android.waituntilnotpresent    adeletephone    ${40}

Collect a contact
    [Documentation]    collect a contact \ # \ 执行前手动添加联系人"acollectionphone1"
    [Tags]    P0    Regression
    android.loginwithpassword    ${username}    ${password}
    android.click    ${bottom_location_contact }
    android.verify    ${contact_location_title}
    android.longclick    acollectionphone1    duration=5000
    android.verify    ${contact_longclick_dialogbox_location_add_collection }
    android.verify    ${contact_longclick_dialogbox_location_cancle }
    android.click    ${contact_longclick_dialogbox_location_add_collection }
    android.verify    ${contact_location_head_collection }
    android.longclick    acollectionphone1    duration=5000
    android.verify    ${contact_longclick_dialogbox_location_cancle_collection }
    android.click    ${contact_longclick_dialogbox_location_cancle_collection }
    android.verify    ${contact_location_title }
    android.waituntilnotpresent    ${contact_location_head_collection }
    android.verify    acollectionphone1

Lookup a contact
    [Documentation]    Lookup a contact #执行前需要添加联系人“acollectionphone1”
    [Tags]    P0    Regression
    android.loginwithpassword    ${username}    ${password}
    android.click    ${bottom_location_contact }
    android.verify    ${contact_location_title}
    android.longclick    acollectionphone1    duration=5000
    android.verify    ${contact_longclick_dialogbox_location_lookup }
    android.verify    ${contact_longclick_dialogbox_location_cancle }
    android.click     ${contact_longclick_dialogbox_location_lookup }
    android.verify    ${contact_detail_location_name }
    android.verify    ${contact_detail_location_phone }
    android.verify    ${contact_detail_location_tel_icon }
    android.verify    ${contact_detail_location_message_icon }
    android.verify    ${contact_detail_location_user_head }
    android.click     ${contact_detail_location_back }
    android.verify    ${contact_location_title }
    android.click     acollectionphone1
    android.verify    ${contact_detail_location_name }
    android.verify    ${contact_detail_location_phone }
    android.verify    ${contact_detail_location_tel_icon }
    android.verify    ${contact_detail_location_message_icon }
    android.verify    ${contact_detail_location_user_head }

Send free message
    [Documentation]    Send a free message to a contact who is uxin user.    #执行前手动添加联系人“acollectionphone1”且号码为已注册有信的号码
    [Tags]    P0    Regression
    android.loginwithpassword    ${username}    ${password}
    android.click    ${bottom_location_contact }
    android.verify    ${contact_location_title}
    android.click    acollectionphone1
    android.verify    ${contact_detail_location_tel_icon }
    android.verify    ${contact_detail_location_message_icon }
    android.click    ${contact_detail_location_message_icon}
    android.verify    ${contact_detail_sentmessage_mode_location_free_mode }
    android.verify    ${contact_detail_sentmessage_mode_location_nomal_mode }
    android.click    ${contact_detail_sentmessage_mode_location_free_mode}
    android.verify    ${contact_free_talk_location_title }
    android.verify    ${contact_free_talk_location_detail_icon }
    android.verify    ${contact_free_talk_location_emotion_button }
    android.verify    ${contact_free_talk_location_more_button }
    android.click    ${contact_free_talk_location_more_button}
    android.verify    ${contact_free_talk_location_voice_talk_button }
    android.verify    ${contact_free_talk_location_send_photo_button }
    android.verify    ${contact_free_talk_location_call_camera_button }
    android.verify    ${contact_free_talk_location_get_location_button }
    android.click    ${contact_free_talk_location_message_button}
    android.verify    ${contact_free_talk_location_text_input_box }
    android.enter    Hello world!    ${contact_free_talk_location_text_input_box }
    android.click    ${contact_free_talk_location_send_button }
    android.verify    Hello world!
    android.click    ${contact_free_talk_location_emotion_button }
    android.verify    ${contact_free_talk_location_all_emotions }
    android.click    ${contact_free_talk_location_emotion_button }
    android.waituntilnotpresent    ${contact_free_talk_location_all_emotions }
