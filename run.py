# -*- coding: utf-8 -*-

import time


# 运行函数


def run():
    while True:
        with open('/tmp/a.txt', 'a+') as fd:
            fd.write('running....\n')
        time.sleep(3)


def foo():
    pass
