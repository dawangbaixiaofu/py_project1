import sched
import Single
import time
import datetime

conn = Single.Connection(host='localhost', user='root', port=3306, password='729813', database='test')
cur = conn.cursor()
schedule = sched.scheduler(timefunc=time.time, delayfunc=time.sleep)
current_time = datetime.datetime.now()


def act_queue(delay):
    cur.execute(query="call test.iphone_count();")
    # 执行循环任务结束的时间条件
    if datetime.datetime.now() > current_time + datetime.timedelta(seconds=20):
        return
    schedule.enter(delay, 1, action=act_queue, argument=(delay,))


def main():
    schedule.enter(0, 1, act_queue, argument=(10,))
    schedule.run()  # 当执行run的时候会执行action这个时候再次在队列中加入任务

    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    main()
