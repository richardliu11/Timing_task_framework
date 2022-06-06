# python定时任务框架
# -*- coding: utf-8 -*-
# Author : richard
# Date : 2022/6/6


'''
pip install apscheduler
参数说明：
hour:每天执行的时间的小时
minute:每天执行的时间的分钟
如下实例中，表示的是每天10:15自动执行任务task
misfire_grace_time:容错时间（秒）

'''

from apscheduler.schedulers.blocking import BlockingScheduler


def task():
    print('如果你突然打了个喷嚏~')



def main():#主程序控制定时任务
    """主函数"""

    # 创建定时对象
    scheduler = BlockingScheduler(timezone="Asia/Shanghai")

    # 定义任务
    scheduler.add_job(task, 'cron', hour=10, minute=15,misfire_grace_time=10)

    # 启动任务
    print("+++ +++ +++ 启动 +++ +++ +++")
    scheduler.start()




if __name__ == '__main__':
    main()