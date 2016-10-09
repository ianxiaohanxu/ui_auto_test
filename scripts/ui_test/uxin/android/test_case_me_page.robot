***Settings***
| Documentation  | All test cases on me page | 
| Resource       | test_resource.robot | 
| Test setup     | Setup | 
| Test teardown  | Teardown | 

***Test Cases***
Check Me Page > Setting > General 
|  | [Documentation] | cover message setting page & voice testing page & clear cache function | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} |
|  | android.click   | ${bottom_location_me} |
|  | android.verify  | ${me_location_settings} | 
|  | android.click   | ${me_location_settings} | 
|  | android.verify  | ${settings_location_exit} | 
|  | android.click   | ${settings_verification_general} | 
|  | android.verify  | ${setting_general_verification_title} | 
|  | android.click   | ${setting_general_location_message_setting} |
|  | android.verify  | ${setting_general_message_setting_verification_title} |
|  | android.verify  | ${setting_general_message_setting_verification_voice} |
|  | android.verify  | ${setting_general_message_setting_verification_shock} |
|  | android.verify  | ${setting_general_message_setting_verification_telephone} |
|  | android.verify  | ${setting_general_message_setting_verification_speaker} |
|  | android.click   | ${setting_general_message_setting_location_back} |
|  | android.verify  | ${settings_verification_general} |
|  | android.click   | ${setting_general_location_voice_testing} |
|  | android.verify  | ${setting_general_voice_testing_verification_title} |
|  | android.click   | ${setting_general_voice_testing_location_back} |
|  | android.verify  | ${settings_verification_general} |
|  | android.click   | ${setting_general_location_clear_cache} |
|  | android.verify  | ${setting_general_location_clear_cache_ok} |
|  | android.click   | ${setting_general_location_back} |
|  | android.verify  | ${settings_verification_title} |
|  | android.click   | ${settings_location_back} |
|  | android.verify  | ${me_verification_title} |

Check Me Page > Setting > Backup address 
|  | [Documentation] | cover back up and recovery function | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} |
|  | android.click   | ${bottom_location_me} |
|  | android.verify  | ${me_location_settings} | 
|  | android.click   | ${me_location_settings} | 
|  | android.verify  | ${settings_location_exit} | 
|  | android.click   | ${settings_verification_backup_address} |
|  | android.verify  | ${settings_backup_address_verification_title} |
|  | android.click   | ${setting_backup_address_location_bak} |
|  | android.verify  | ${settings_backup_address_bak_dialog_verification_title} |
|  | android.click   | ${settings_backup_address_bak_dialog_location_cancle} |
|  | android.verify  | ${settings_backup_address_verification_title} |
|  | android.click   | ${settings_backup_address_location_cover} |
|  | android.verify  | ${settings_backup_address_cover_dialog_verification_title} |
|  | android.click   | ${settings_backup_address_cover_dialog_location_cancle} |
|  | android.verify  | ${settings_backup_address_verification_title} |
|  | android.click   | ${settings_backup_address_location_back} |
|  | android.verify  | ${settings_verification_title} |
|  | android.click   | ${settings_location_back} |
|  | android.verify  | ${me_verification_title} |

Check Me Page > Setting > strange number popup window
|  | [Documentation] | enable strange number popup window is useful | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} |
|  | android.click   | ${bottom_location_me} |
|  | android.verify  | ${me_location_settings} | 
|  | android.click   | ${me_location_settings} | 
|  | android.verify  | ${settings_location_exit} | 
|  | android.click   | ${settings_verification_strange_number} |
|  | android.verify  | ${settings_strange_number_verification_title} |
|  | android.verify  | ${settings_strange_number_verification_switch} |
|  | android.click   | ${settings_strange_number_location_back} |
|  | android.verify  | ${settings_verification_title} |
|  | android.click   | ${settings_location_back} |
|  | android.verify  | ${me_verification_title} |


Check Me Page > Setting > social account binding
|  | [Documentation] | cover qq and weibo binding | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} |
|  | android.click   | ${bottom_location_me} |
|  | android.verify  | ${me_location_settings} | 
|  | android.click   | ${me_location_settings} | 
|  | android.verify  | ${settings_location_exit} | 
|  | android.click   | ${settings_verification_social_account} |
|  | android.verify  | ${settings_social_account_verification_title} |
|  | android.verify  | ${settings_social_account_location_qq} |
|  | android.verify  | ${settings_social_account_location_sina} |
|  | android.click   | ${settings_social_account_location_back} |
|  | android.verify  | ${settings_verification_title} |
|  | android.click   | ${settings_location_back} |
|  | android.verify  | ${me_verification_title} |


Check Me Page > Setting > contact us
|  | [Documentation] | ensure we can arrive at contact us page | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} |
|  | android.click   | ${bottom_location_me} |
|  | android.verify  | ${me_location_settings} | 
|  | android.click   | ${me_location_settings} | 
|  | android.verify  | ${settings_location_exit} | 
|  | android.click   | ${settings_verification_contact_us} |
|  | android.verify  | ${settings_contact_us_verification_title} |
|  | android.click   | ${settings_contact_us_location_back} |
|  | android.verify  | ${settings_verification_title} |
|  | android.click   | ${settings_location_back} |
|  | android.verify  | ${me_verification_title} |

Check Me Page > Setting > about us
|  | [Documentation] | ensure we can arrive at about us page | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} |
|  | android.click   | ${bottom_location_me} |
|  | android.verify  | ${me_location_settings} | 
|  | android.click   | ${me_location_settings} | 
|  | android.verify  | ${settings_location_exit} | 
|  | android.click   | ${settings_verification_about_us} |
|  | android.verify  | ${settings_about_us_verification_title} |
|  | android.click   | ${settings_about_us_location_back} |
|  | android.verify  | ${settings_verification_title} |
|  | android.click   | ${settings_location_back} |
|  | android.verify  | ${me_verification_title} |

Check Me Page > Personality Setting > calloutshow
|  | [Documentation] | ensure calloutshow page exsits | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} | 
|  | android.click   | ${bottom_location_me} |
|  | android.verify  | ${me_location_personality_settings} |
|  | android.click   | ${me_location_personality_settings} |
|  | android.verify  | ${me_personality_setting_verification_title} |
|  | android.click   | ${me_personality_setting_verification_calloutshow} |
|  | android.verify  | ${me_personality_setting_calloutshow_verification_title} | ${5} | 
|  | android.click   | ${me_personality_setting_calloutshow_location_back} |
|  | android.verify  | ${me_personality_setting_verification_title} |
|  | android.click   | ${me_personality_setting_location_back} |
|  | android.verify  | ${me_verification_title} |

Check Me Page > Personality Setting > incoming
|  | [Documentation] | ensure incoming page exsits | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} | 
|  | android.click   | ${bottom_location_me} |
|  | android.verify  | ${me_location_personality_settings} |
|  | android.click   | ${me_location_personality_settings} |
|  | android.verify  | ${me_personality_setting_verification_title} |
|  | android.click   | ${me_personality_setting_verification_incoming} |
|  | android.verify  | ${me_personality_setting_incoming_verification_title} | ${5} | 
|  | android.click   | ${me_personality_setting_incoming_location_back} |
|  | android.verify  | ${me_personality_setting_verification_title} |
|  | android.click   | ${me_personality_setting_location_back} |
|  | android.verify  | ${me_verification_title} |

Check Me Page > Personality Setting > theme
|  | [Documentation] | ensure theme page exsits | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} | 
|  | android.click   | ${bottom_location_me} |
|  | android.verify  | ${me_location_personality_settings} |
|  | android.click   | ${me_location_personality_settings} |
|  | android.verify  | ${me_personality_setting_verification_title} |
|  | android.click   | ${me_personality_setting_verification_theme} |
|  | android.verify  | ${me_personality_setting_theme_verification_title} | ${5} |
|  | android.click   | ${me_personality_setting_theme_location_back} |
|  | android.verify  | ${me_personality_setting_verification_title} |
|  | android.click   | ${me_personality_setting_location_back} |
|  | android.verify  | ${me_verification_title} |

Check Me Page > Personality Setting > pressmusic
|  | [Documentation] | ensure pressmusic page exsits | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} | 
|  | android.click   | ${bottom_location_me} |
|  | android.verify  | ${me_location_personality_settings} |
|  | android.click   | ${me_location_personality_settings} |
|  | android.verify  | ${me_personality_setting_verification_title} |
|  | android.click   | ${me_personality_setting_verification_pressmusic} |
|  | android.verify  | ${me_personality_setting_pressmusic_verification_title} | ${5} |
|  | android.click   | ${me_personality_setting_pressmusic_location_back} |
|  | android.verify  | ${me_personality_setting_verification_title} |
|  | android.click   | ${me_personality_setting_location_back} |
|  | android.verify  | ${me_verification_title} |

Check Me Page > Personality Setting > starlock
|  | [Documentation] | ensure starlock page exsits| 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} | 
|  | android.click   | ${bottom_location_me} |
|  | android.verify  | ${me_location_personality_settings} |
|  | android.click   | ${me_location_personality_settings} |
|  | android.verify  | ${me_personality_setting_verification_title} |
|  | android.click   | ${me_personality_setting_verification_starclock} |
|  | android.verify  | ${me_personality_setting_starclock_verification_title} | ${5} |
|  | android.click   | ${me_personality_setting_starclock_location_back} |
|  | android.verify  | ${me_personality_setting_verification_title} |
|  | android.click   | ${me_personality_setting_location_back} |
|  | android.verify  | ${me_verification_title} |

Check Me Page > Personality Setting > My Personality > Theme
|  | [Documentation] | ensure theme page exsits| 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} | 
|  | android.click   | ${bottom_location_me} |
|  | android.verify  | ${me_location_personality_settings} |
|  | android.click   | ${me_location_personality_settings} | 
|  | android.verify  | ${me_personality_setting_location_my} |
|  | android.click   | ${me_personality_setting_location_my} |
|  | android.verify  | ${me_personality_setting_my_verification_title} |
|  | android.click   | ${me_personality_setting_my_location_theme} |
|  | android.verify  | ${me_personality_setting_my_theme_verification_title} | ${5} |
|  | android.click   | ${me_personality_setting_my_theme_location_back} |
|  | android.verify  | ${me_personality_setting_my_verification_title} |
|  | android.click   | ${me_personality_setting_my_location_back} |
|  | android.verify  | ${me_personality_setting_verification_title} |
|  | android.click   | ${me_personality_setting_location_back} |
|  | android.verify  | ${me_verification_title} |

Check Me Page > Personality Setting > My Personality > Incoming
|  | [Documentation] | ensure incoming page exsits | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} | 
|  | android.click   | ${bottom_location_me} |
|  | android.verify  | ${me_location_personality_settings} |
|  | android.click   | ${me_location_personality_settings} | 
|  | android.verify  | ${me_personality_setting_location_my} |
|  | android.click   | ${me_personality_setting_location_my} |
|  | android.verify  | ${me_personality_setting_my_verification_title} |
|  | android.click   | ${me_personality_setting_my_location_incoming} |
|  | android.verify  | ${me_personality_setting_my_incoming_verification_title} | ${5} |
|  | android.click   | ${me_personality_setting_my_incoming_location_back} |
|  | android.verify  | ${me_personality_setting_my_verification_title} |
|  | android.click   | ${me_personality_setting_my_location_back} |
|  | android.verify  | ${me_personality_setting_verification_title} |
|  | android.click   | ${me_personality_setting_location_back} |
|  | android.verify  | ${me_verification_title} |

Check Me Page > Personality Setting > My Personality > CalloutShow
|  | [Documentation] | ensure calloutshow page exsits | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} | 
|  | android.click   | ${bottom_location_me} |
|  | android.verify  | ${me_location_personality_settings} |
|  | android.click   | ${me_location_personality_settings} | 
|  | android.verify  | ${me_personality_setting_location_my} |
|  | android.click   | ${me_personality_setting_location_my} |
|  | android.verify  | ${me_personality_setting_my_verification_title} |
|  | android.click   | ${me_personality_setting_my_location_calloutshow} |
|  | android.verify  | ${me_personality_setting_my_calloutshow_verification_title} | ${5} |
|  | android.click   | ${me_personality_setting_my_calloutshow_location_back} |
|  | android.verify  | ${me_personality_setting_my_verification_title} |
|  | android.click   | ${me_personality_setting_my_location_back} |
|  | android.verify  | ${me_personality_setting_verification_title} |
|  | android.click   | ${me_personality_setting_location_back} |
|  | android.verify  | ${me_verification_title} |

Check Me Page > Personality Setting > My Personality > PressMusic
|  | [Documentation] | ensure pressmusic page exsits | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} | 
|  | android.click   | ${bottom_location_me} |
|  | android.verify  | ${me_location_personality_settings} |
|  | android.click   | ${me_location_personality_settings} | 
|  | android.verify  | ${me_personality_setting_location_my} |
|  | android.click   | ${me_personality_setting_location_my} |
|  | android.verify  | ${me_personality_setting_my_verification_title} |
|  | android.click   | ${me_personality_setting_my_location_pressmusic} |
|  | android.verify  | ${me_personality_setting_my_pressmusic_verification_title} | ${5} |
|  | android.click   | ${me_personality_setting_my_pressmusic_location_back} |
|  | android.verify  | ${me_personality_setting_my_verification_title} |
|  | android.click   | ${me_personality_setting_my_location_back} |
|  | android.verify  | ${me_personality_setting_verification_title} |
|  | android.click   | ${me_personality_setting_location_back} |
|  | android.verify  | ${me_verification_title} |

Check Me Page > Personality Setting > My Personality > StarLock
|  | [Documentation] | ensure starlock page exsits | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} | 
|  | android.click   | ${bottom_location_me} |
|  | android.verify  | ${me_location_personality_settings} |
|  | android.click   | ${me_location_personality_settings} | 
|  | android.verify  | ${me_personality_setting_location_my} |
|  | android.click   | ${me_personality_setting_location_my} |
|  | android.verify  | ${me_personality_setting_my_verification_title} |
|  | android.click   | ${me_personality_setting_my_location_starclock} |
|  | android.verify  | ${me_personality_setting_my_starclock_verification_title} | ${5} |
|  | android.click   | ${me_personality_setting_my_starclock_location_back} |
|  | android.verify  | ${me_personality_setting_my_verification_title} |
|  | android.click   | ${me_personality_setting_my_location_back} |
|  | android.verify  | ${me_personality_setting_verification_title} |
|  | android.click   | ${me_personality_setting_location_back} |
|  | android.verify  | ${me_verification_title} |

#==============================================================================================
Check Me Page > User Profile
|  | [Documentation] | ensure u icon exists on user profile page | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} |
|  | android.click   | ${bottom_location_me} |
|  | android.verify  | ${me_location_user_profile_phone} |
|  | android.click   | ${me_location_user_profile} |
|  | android.verify  | ${me_user_profile_verification_title} |
|  | android.verify  | ${me_user_profile_location_u_icon} |
|  | android.click   | ${me_user_profile_location_back} |
|  | android.verify  | ${me_verification_title} |

Check Me Page > User Profile > Edit
|  | [Documentation] | ensure edit user profile page's basic info exists | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} |
|  | android.click   | ${bottom_location_me} |
|  | android.verify  | ${me_location_user_profile_phone} |
|  | android.click   | ${me_location_user_profile} |
|  | android.verify  | ${me_user_profile_verification_title} |
|  | android.click   | ${me_user_profile_location_edit} |
|  | android.verify  | ${me_user_profile_edit_verification_title} |
|  | android.verify  | ${me_user_profile_edit_verification_ok} |
|  | android.verify  | ${me_user_profile_edit_verificaiton_msg} |
|  | android.verify  | ${me_user_profile_edit_verification_image} |
|  | android.verify  | ${me_user_profile_edit_verification_nickname} |
|  | android.verify  | ${me_user_profile_edit_verification_phone} |
|  | android.click   | ${me_user_profile_edit_location_back} |
|  | android.verify  | ${me_user_profile_verification_title} |
|  | android.click   | ${me_user_profile_location_back} |
|  | android.verify  | ${me_verification_title} |

#==============================================================================================
Check Me Page > Account Balance
|  | [Documentation] | ensure u icon exists on account balance page | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} |
|  | android.click   | ${bottom_location_me} |
|  | android.verify  | ${me_location_account_balance} |
|  | android.click   | ${me_location_account_balance} |
|  | android.verify  | ${me_account_balance_verification_title} |
|  | android.verify  | ${me_account_balance_location_u_icon} |
|  | android.click   | ${me_account_balance_location_back} |
|  | android.verify  | ${me_verification_title} |

Check Me Page > Account balance > recommend friend
|  | [Documentation] | ensure share and invite function is useful | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} |
|  | android.click   | ${bottom_location_me} |
|  | android.verify  | ${me_location_account_balance} |
|  | android.click   | ${me_location_account_balance} |
|  | android.verify  | ${me_account_balance_verification_title} |
|  | android.click   | ${me_account_balance_location_recmduxin} |
|  | android.verify  | ${me_account_balance_recmduxin_verification_title} |
|  | android.verify  | ${me_account_balance_recmduxin_location_qyq} |
|  | android.verify  | ${me_account_balance_recmduxin_location_qzone} |
|  | android.verify  | ${me_account_balance_recmduxin_location_wb} |
|  | android.verify  | ${me_account_balance_recmduxin_location_invitefriend} |
|  | android.click   | ${me_account_balance_recmduxin_location_back} |
|  | android.verify  | ${me_account_balance_verification_title} |
|  | android.click   | ${me_account_balance_location_back} |
|  | android.verify  | ${me_verification_title} |

Check Me Page > buy vip
|  | [Documentation] | ensure buy vip page exists | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} |
|  | android.click   | ${bottom_location_me} |
|  | android.verify  | ${me_location_user_vip_btn} |
|  | android.click   | ${me_location_user_vip_btn} |
|  | android.verify  | ${me_vip_location_buy_btn} |
|  | android.click   | ${me_vip_location_back} |
|  | android.verify  | ${me_verification_title} |
