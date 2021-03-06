# coding=utf-8
from src.testcase.GN_Y201S.WidgetOperation import *


class GNY201SNormalTimer7(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"FUT_NTIMER_普通定时(#48)"  # 用例所属模块
        self.case_title = u'FUT_NTIMER_普通交叉定时'  # 用例名称
        self.zentao_id = 505  # 禅道ID

    # 用例动作
    def case(self):
        device = conf["MAC"]["AL"][0]
        self.set_power(device, "power_off")

        self.choose_home_device(device)

        self.close_mode_timer()

        self.close_general_timer()

        self.widget_click(self.page["control_device_page"]["normal_timer"],
                          self.page["normal_timer_page"]["title"])

        self.delete_normal_timer()

        now = time.strftime("%H:%M")

        delay_time_1 = 2
        start_time_1, set_time_1, cycle1 = self.create_normal_timer(now, delay_time_1, "power_on", u"永不")

        delay_time_2 = 4
        start_time_2, set_time_2, cycle2 = self.create_normal_timer(now, delay_time_2, "power_off", u"永不")

        delay_time_3 = 6
        start_time_3, set_time_3, cycle3 = self.create_normal_timer(now, delay_time_3, "power_on", u"永不")

        delay_time_4 = 6
        start_time_4, set_time_4, cycle4 = self.create_normal_timer(now, delay_time_4, "power_off", u"永不")

        self.widget_click(self.page["normal_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        attribute = self.ac.get_attribute(self.wait_widget(self.page["control_device_page"]["launch_mode"]), "name")
        if attribute != u"定时任务开":
            raise TimeoutException("mode launch failed, current: %s" % [attribute])

        self.widget_click(self.page["control_device_page"]["to_return"],
                          self.page["app_home_page"]["title"])

        self.check_timer(device, start_time_1, set_time_1, u"开", cycle1)
        self.check_timer(device, start_time_2, set_time_2, u"关", cycle2)
        self.check_timer(device, start_time_3, set_time_3, u"开", cycle3)
        self.check_timer(device, start_time_4, set_time_4, u"关", cycle4)
