# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppRegister2(LaunchApp):
    def run(self):
        self.case_module = u"注册"  # 用例所属模块
        self.case_title = u'注册页面-正确的用户名和密码，空的验证码，注册验证'  # 用例名称
        self.zentao_id = 1885  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_REGISTER_002
        self.driver = self.return_driver()
        self.logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s", CASE_MODULE="%s"]'
                         % (self.basename, self.case_title, self.zentao_id, self.case_module))  # 记录log

        try:
            self.launch_app(True)  # 启动APP
            self.case()
        except WebDriverException:
            self.debug.error(traceback.format_exc())  # Message: ***

    # 用例动作
    def case(self):
        try:
            self.widget_click(self.page["login_page"]["title"],
                              self.page["login_page"]["to_register"],
                              self.page["register_page"]["title"],
                              1, 1, 1, 10, 0.5)

            user_name = self.widget_click(self.page["register_page"]["title"],
                                          self.page["register_page"]["username"],
                                          self.page["register_page"]["title"],
                                          1, 1, 1, 10, 0.5)

            # 发送数据
            data = conf["user_and_pwd"][self.user]["user_name"]
            data = str(data).decode('hex').replace(" ", "")
            user_name.clear()
            self.ac.send_keys(user_name, data)
            self.logger.info(u'[APP_INPUT] ["用户名"] input success')
            time.sleep(0.5)

            pwd = self.widget_click(self.page["register_page"]["title"],
                                    self.page["register_page"]["password"],
                                    self.page["register_page"]["title"],
                                    1, 1, 1, 10, 0.5)

            data = "123456"
            self.show_pwd(self.wait_widget(self.page["register_page"]["check_box"]))
            pwd.clear()
            self.ac.send_keys(pwd, data)
            self.logger.info(u'[APP_INPUT] ["注册密码"] input success')
            time.sleep(0.5)

            self.widget_click(self.page["register_page"]["title"],
                              self.page["register_page"]["get_check_code"],
                              self.page["register_page"]["title"],
                              1, 1, 1, 10, 0.5)

            widget_px = self.page["register_page"]["register_button"]
            width = int(int(self.device_info["dpi"]["width"]) * widget_px[3]["px"]["width"])
            height = int(int(self.device_info["dpi"]["height"]) * widget_px[3]["px"]["height"])
            self.driver.tap([(width, height)], )
            self.logger.info(u'[APP_CLICK] operate_widget ["%s"] success' % widget_px[2])

            while True:
                try:
                    self.wait_widget(self.page["loading_popup"]["title"], 0.5, 0.1)
                except TimeoutException:
                    break

                # 截屏获取设备toast消息
                ScreenShot(self.device_info, self.zentao_id, self.basename, self.logger)

            self.case_over("screen")
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
