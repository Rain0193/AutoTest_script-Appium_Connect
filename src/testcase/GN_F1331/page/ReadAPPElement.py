# coding=utf-8
# 由CreateSomeFiles.py生成
from src.testcase.GN_F1331.page.AppPageElement import *


class PageElement(object):
    """
    京东微联-GN_F1331 all page element
    """

    def __init__(self, phone_os):
        self.mpw = MainPageWidget(phone_os)

    def get_page_element(self):
        d = {}
        d["account_setting_page"] = self.mpw.account_setting_page()
        d["add_device_list_page"] = self.mpw.add_device_list_page()
        d["add_device_method_page"] = self.mpw.add_device_method_page()
        d["add_history_list_page"] = self.mpw.add_history_list_page()
        d["add_normal_timer_page"] = self.mpw.add_normal_timer_page()
        d["add_outlet_list_page"] = self.mpw.add_outlet_list_page()
        d["add_specification_page"] = self.mpw.add_specification_page()
        d["app_home_page"] = self.mpw.app_home_page()
        d["change_nickname_page"] = self.mpw.change_nickname_page()
        d["control_device_page"] = self.mpw.control_device_page()
        d["cycle_timer_page"] = self.mpw.cycle_timer_page()
        d["delay_timer_page"] = self.mpw.delay_timer_page()
        d["device_info_page"] = self.mpw.device_info_page()
        d["down_timer_page"] = self.mpw.down_timer_page()
        d["elec_bill_page"] = self.mpw.elec_bill_page()
        d["elec_page"] = self.mpw.elec_page()
        d["help_setting_page"] = self.mpw.help_setting_page()
        d["input_wifi_password_page"] = self.mpw.input_wifi_password_page()
        d["login_page"] = self.mpw.login_page()
        d["mid_timer_page"] = self.mpw.mid_timer_page()
        d["peak_valley_price_page"] = self.mpw.peak_valley_price_page()
        d["search_device_fail_page"] = self.mpw.search_device_fail_page()
        d["search_device_loading_page"] = self.mpw.search_device_loading_page()
        d["search_device_success_page"] = self.mpw.search_device_success_page()
        d["set_elec_page"] = self.mpw.set_elec_page()
        d["single_price_page"] = self.mpw.single_price_page()
        d["timer_log_page"] = self.mpw.timer_log_page()
        d["timer_notes_page"] = self.mpw.timer_notes_page()
        d["timer_repeat_page"] = self.mpw.timer_repeat_page()
        d["up_timer_page"] = self.mpw.up_timer_page()

        d["bind_device_fail_popup"] = self.mpw.bind_device_fail_popup()
        d["close_ad_popup"] = self.mpw.close_ad_popup()
        d["loading_popup"] = self.mpw.loading_popup()
        d["logout_popup"] = self.mpw.logout_popup()
        d["mode_timer_conflict_popup"] = self.mpw.mode_timer_conflict_popup()
        d["timer_edit_popup"] = self.mpw.timer_edit_popup()
        d["timer_log_clear_popup"] = self.mpw.timer_log_clear_popup()
        d["unbind_device_popup"] = self.mpw.unbind_device_popup()
        d["update_popup"] = self.mpw.update_popup()

        return d
