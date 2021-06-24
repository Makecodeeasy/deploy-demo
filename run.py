# -*- coding: utf-8 -*-

import time


# 运行一个函数

def run():
    while True:
        with open('/tmp/a.txt', 'a+') as fd:
            fd.write('running....\n')
        time.sleep(3)
