***Settings***
| Documentation  | All test cases on me page | 
| Resource       | test_resource.robot | 
| Test setup     | Setup | 
| Test teardown  | Teardown | 

***Test Cases***
Redirect on me page
|  | [Documentation] | Test redirection on me page | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} |

***Me Location Settings***
|  | android.verify  | ${me_location_settings} | 
|  | android.click   | ${me_location_settings} | 
|  | android.verify  | ${settings_location_exit} | 

#verify setting > general
|  | android.click   | ${setting_general} | 
|  | android.verify  | ${setting_general_title} | 
|  | android.click   | ${setting_general_message_setting} |
|  | android.verify  | ${setting_general_message_setting_title} |
|  | android.verify  | ${setting_general_message_setting_voice} |
|  | android.verify  | ${setting_general_message_setting_shock} |
|  | android.verify  | ${setting_general_message_setting_telephone} |
|  | android.verify  | ${setting_general_message_setting_speaker} |
|  | android.click   | ${setting_general_message_setting_back} |
|  | android.verify  | ${setting_general} |
|  | android.click   | ${setting_general_voice_testing} |
|  | android.verify  | ${setting_general_voice_testing_title} |
|  | android.click   | ${setting_general_voice_testing_back} |
|  | android.verify  | ${setting_general} |
|  | android.click   | ${setting_general_clear_cache} |
|  | android.verify  | ${setting_general_clear_cache_ok} |
|  | android.click   | ${setting_general_back} |
|  | android.verify  | ${settings_verification_title} |

#Setting > backup address list
|  | android.click   | ${setting_backup_address} |
|  | android.verify  | ${setting_backup_address_title} |
|  | android.click   | ${setting_backup_address_bak} |
|  | android.verify  | ${setting_backup_address_bak_title} |
|  | android.click   | ${setting_backup_address_bak_cancle} |
|  | android.verify  | ${setting_backup_address_title} |
|  | android.click   | ${setting_backup_address_cover} |
|  | android.verify  | ${setting_backup_address_cover_title} |
|  | android.click   | ${setting_backup_address_cover_cancle} |
|  | android.verify  | ${setting_backup_address_title} |
|  | android.click   | ${setting_backup_address_back} |
|  | android.verify  | ${settings_verification_title} |

#Setting > strange number popup window
|  | android.click   | ${setting_strange_number} |
|  | android.verify  | ${setting_strange_number_title} |
|  | android.verify  | ${setting_strange_number_switch} |
|  | android.click   | ${setting_strange_number_back} |
|  | android.verify  | ${settings_verification_title} |

#Setting > social account binding
|  | android.click   | ${setting_social_account} |
|  | android.verify  | ${setting_social_account_title} |
|  | android.verify  | ${setting_social_account_qq} |
|  | android.verify  | ${setting_social_account_sina} |
|  | android.click   | ${setting_social_account_back} |
|  | android.verify  | ${settings_verification_title} |

#Setting > contact us
|  | android.click   | ${setting_contact_us} |
|  | android.verify  | ${setting_contact_us_title} |
|  | android.click   | ${setting_contact_us_back} |
|  | android.verify  | ${settings_verification_title} |

#Setting > about us
|  | android.click   | ${setting_about_us} |
|  | android.verify  | ${setting_about_us_title} |
|  | android.click   | ${setting_about_us_back} |
|  | android.verify  | ${settings_verification_title} |

#go back to me page 
|  | android.click   | ${settings_location_back} |
|  | android.verify  | ${me_location_title} |

***Test Cases***
Personality Setting test case
|  | [Documentation] | Personality Setting test case | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} |

#Me > personality setting
|  | android.verify  | ${me_personality_location_settings} |
|  | android.click   | ${me_personality_location_settings} |
|  | android.verify  | ${personality_setting_title} |

#Me > personality setting > calloutshow
|  | android.click   | ${personality_setting_calloutshow} |
|  | android.verify  | ${personality_setting_calloutshow_title} | ${5} | 
|  | android.click   | ${personality_setting_calloutshow_back} |
|  | android.verify  | ${personality_setting_title} |

#Me > personality setting > theme
|  | android.click   | ${personality_setting_theme} |
|  | android.verify  | ${personality_setting_theme_title} | ${15} |
|  | android.click   | ${personality_setting_theme_back} |
|  | android.verify  | ${personality_setting_title} |

#Me > personality setting > pressmusic
|  | android.click   | ${personality_setting_pressmusic} |
|  | android.verify  | ${personality_setting_pressmusic_title} | ${5} |
|  | android.click   | ${personality_setting_pressmusic_back} |
|  | android.verify  | ${personality_setting_title} |

#Me > personality setting > starclock
|  | android.click   | ${personality_setting_starclock} |
|  | android.verify  | ${personality_setting_starclock_title} | ${5} |
|  | android.click   | ${personality_setting_starclock_back} |
|  | android.verify  | ${personality_setting_title} |

#Me > personality setting > my personality
|  | android.click   | ${personality_setting_my} |
|  | android.verify  | ${personality_setting_my_title} |

|  | android.click   | ${personality_setting_my_theme} |
|  | android.verify  | ${personality_setting_my_theme_title} | ${15} |
|  | android.click   | ${personality_setting_my_theme_back} |
|  | android.verify  | ${personality_setting_my_title} |

|  | android.click   | ${personality_setting_my_calloutshow} |
|  | android.verify  | ${personality_setting_my_calloutshow_title} | ${5} |
|  | android.click   | ${personality_setting_my_calloutshow_back} |
|  | android.verify  | ${personality_setting_my_title} |

|  | android.click   | ${personality_setting_my_pressmusic} |
|  | android.verify  | ${personality_setting_my_pressmusic_title} | ${5} |
|  | android.click   | ${personality_setting_my_pressmusic_back} |
|  | android.verify  | ${personality_setting_my_title} |

|  | android.click   | ${personality_setting_my_starclock} |
|  | android.verify  | ${personality_setting_my_starclock_title} | ${5} |
|  | android.click   | ${personality_setting_my_starclock_back} |
|  | android.verify  | ${personality_setting_my_title} |

# end ,go to me page
|  | android.click   | ${personality_setting_my_back} |
|  | android.verify  | ${personality_setting_title} |
|  | android.click   | ${personality_setting_back} |
|  | android.verify  | ${me_location_title} |

***Test Cases***
User Profile
|  | [Documentation] | User Profile | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} |

#User profile detail page
|  | android.verify  | ${me_user_profile_phone} |
|  | android.click   | ${me_user_profile} |
|  | android.verify  | ${me_user_profile_title} |
|  | android.verify  | ${me_user_profile_u_icon} |
|  | android.click   | ${me_user_profile_edit} |
|  | android.verify  | ${me_user_profile_edit_title} |
|  | android.verify  | ${me_user_profile_edit_ok} |
|  | android.verify  | ${me_user_profile_edit_ok} |
|  | android.verify  | ${me_user_profile_edit_msg} |
|  | android.verify  | ${me_user_profile_edit_image} |
|  | android.verify  | ${me_user_profile_edit_nickname} |
|  | android.verify  | ${me_user_profile_edit_phone} |

#End, go to me page
|  | android.click   | ${me_user_profile_edit_back} |
|  | android.verify  | ${me_user_profile_title} |
|  | android.click   | ${me_user_profile_back} |
|  | android.verify  | ${me_location_title} |

***Test Cases***
Account Balance
|  | [Documentation] | Account Balance | 
|  | [tags]          | dist | P0 | Regression | 
|  | android.login_with_password | ${username} | ${ password } | 
|  | android.click   | ${bottom_location_me} |

#Account balance detail page
|  | android.verify  | ${me_account_balance} |
|  | android.click   | ${me_account_balance} |
|  | android.verify  | ${me_account_balance_title} |
|  | android.verify  | ${me_account_balance_u_icon} |

#Account balance > recommend friend
|  | android.click   | ${me_account_balance_recmduxin} |
|  | android.verify  | ${me_account_balance_recmduxin_title} |
|  | android.verify  | ${me_account_balance_recmduxin_qyq} |
|  | android.verify  | ${me_account_balance_recmduxin_qzone} |
|  | android.verify  | ${me_account_balance_recmduxin_wb} |
|  | android.verify  | ${me_account_balance_recmduxin_invitefriend} |
|  | android.click   | ${me_account_balance_recmduxin_back} |
|  | android.verify  | ${me_account_balance_title} |
|  | android.click   | ${me_account_balance_back} |
|  | android.verify  | ${me_location_title} |
