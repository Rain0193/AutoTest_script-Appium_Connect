# coding=utf-8
from src.testcase.GN_Y201S.WidgetOperation import *


class GNY201SEem3(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"电量计量"  # 用例所属模块
        self.case_title = u'FUT_EEM_电价设置验证（待定）'  # 用例名称
        self.zentao_id = 551  # 禅道ID

    # 用例动作
    def case(self):
        device = conf["MAC"]["AL"][0]
        self.set_power(device, "power_off")

        self.choose_home_device(device)

        self.close_mode_timer()

        self.close_general_timer()

        self.ac.swipe(0.5, 0.9, 0.5, 0.1, self.driver)

        self.widget_click(self.page["control_device_page"]["set_elec"],
                          self.page["set_elec_page"]["title"])

        self.widget_click(self.page["set_elec_page"]["peak_valley_button"],
                          self.page["set_elec_page"]["title"])

        self.widget_click(self.page["set_elec_page"]["peak_valley_price"],
                          self.page["peak_valley_price_page"]["title"])

        self.widget_click(self.page["peak_valley_price_page"]["set_peak_price"],
                          self.page["set_peak_price_page"]["title"])

        peak_price = self.widget_click(self.page["set_peak_price_page"]["set_price"],
                                       self.page["set_peak_price_page"]["title"])

        peak_data = "5"
        peak_price.clear()
        self.ac.send_keys(peak_price, peak_data, self.driver)
        self.debug.info(u'[APP_INPUT] ["峰电价"] input success')
        time.sleep(0.5)

        self.widget_click(self.page["set_peak_price_page"]["confirm"],
                          self.page["peak_valley_price_page"]["title"])

        attr = self.ac.get_attribute(self.wait_widget(self.page["peak_valley_price_page"]["set_peak_price"]), "name")
        if peak_data not in attr:
            raise TimeoutException("peak set error!")

        self.widget_click(self.page["peak_valley_price_page"]["set_valley_price"],
                          self.page["set_valley_price_page"]["title"])

        valley_price = self.widget_click(self.page["set_valley_price_page"]["set_price"],
                                         self.page["set_valley_price_page"]["title"])

        valley_data = "2"
        valley_price.clear()
        self.ac.send_keys(valley_price, valley_data, self.driver)
        self.debug.info(u'[APP_INPUT] ["谷电价"] input success')
        time.sleep(0.5)

        self.widget_click(self.page["set_valley_price_page"]["confirm"],
                          self.page["peak_valley_price_page"]["title"])

        attr = self.ac.get_attribute(self.wait_widget(self.page["peak_valley_price_page"]["set_valley_price"]), "name")
        if valley_data not in attr:
            raise TimeoutException("peak set error!")

        now = time.strftime("%H:%M")

        attribute = self.ac.get_attribute(self.wait_widget(self.page["peak_valley_price_page"]["start_time"]), "name")
        if u"未设置" in attribute:
            time_roll = "08:00"
        else:
            time_roll = re.findall("(\d+:\d+)", attribute)[0]

        delay_time_1 = ["08:00", "point"]
        self.widget_click(self.page["peak_valley_price_page"]["start_time"],
                          self.page["timer_roll_popup"]["title"])

        self.set_timer_roll(self.page["timer_roll_popup"]["roll"],
                            self.page["timer_roll_popup"]["roll_h"],
                            self.page["timer_roll_popup"]["roll_m"],
                            time_roll, now, delay_time_1)

        self.widget_click(self.page["timer_roll_popup"]["confirm"],
                          self.page["peak_valley_price_page"]["title"])

        delay_time_2 = ["22:00", "point"]
        self.widget_click(self.page["peak_valley_price_page"]["end_time"],
                          self.page["peak_valley_price_page"]["end_h"])

        self.set_timer_roll(self.page["timer_roll_popup"]["roll"],
                            self.page["timer_roll_popup"]["roll_h"],
                            self.page["timer_roll_popup"]["roll_m"],
                            time_roll, now, delay_time_2)

        self.widget_click(self.page["timer_roll_popup"]["confirm"],
                          self.page["peak_valley_price_page"]["title"])

        self.widget_click(self.page["peak_valley_price_page"]["to_return"],
                          self.page["set_elec_page"]["title"])

        self.widget_click(self.page["set_elec_page"]["confirm"],
                          self.page["control_device_page"]["title"])

        now_h = int(time.strftime("%H"))
        elec, elec_bill = self.get_device_elect(now_h + 2, True)

        peak_price = [v for k, v in elec.items() if 6 <= k <= 22]
        valley_price = [v for k, v in elec.items() if k < 6 and k > 22]

        elec_bill_info = ("current [elec_bill: %s, peak_price: %s, peak_data: %s, valley_price: %s, valley_data: %s]"
                          % (sum(elec_bill.values()), sum(peak_price), peak_data, sum(valley_price), valley_data))
        self.debug.info(elec_bill_info)

        if sum(elec_bill.values()) != sum(peak_price) * int(peak_data) + sum(valley_price) * int(valley_data):
            raise TimeoutException(elec_bill_info)
