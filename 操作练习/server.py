# coding=utf-8
import os
import time
from multiprocessing import Process


class Main:
    def kill_adb(self):
        command = "taskkill /f /t /im adb.exe"
        os.system(command)

    def sim_cmd(self):
        # 小米5
        command = "appium -a 127.0.0.1 -p 4723  -U  b9388cbb  --no-reset"
        # 小米4
        # command = "appium -a 127.0.0.1 -p 4723  -U  f2209864  --no-reset"
        # 360奇酷手机
        # command = "appium -a 127.0.0.1 -p 4725 -bp 4726 -U 8681-M02-0xa0a151df --no-reset"
        # 魅族MX5
        # command = "appium -a 127.0.0.1 -p 4725 -bp 4726 -U 85GABMN9UDD2 --no-reset"
        # ViVo
        # command = "appium -a 127.0.0.1 -p 4723  -U  54a9608b  --no-reset"
        # 华为荣耀
        # command = "appium -a 127.0.0.1 -p 4723  -U  WPV0216928015105  --no-reset"
        # 三星galaxy s5
        # command = "appium -a 127.0.0.1 -p 4723  -U  eda69645  --no-reset"
        os.system(command)


    def func_main(self):
        command = "python test_case\TestCase.py"
        os.system(command)

    def main(self):
        plan = Process(target=self.kill_adb)
        plan.start()
        plan.join()
        time.sleep(0.5)
        server = Process(target=self.sim_cmd)
        server.start()


if __name__ == '__main__':
    Main().main()
