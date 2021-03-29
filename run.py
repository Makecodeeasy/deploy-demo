# -*- coding: utf-8 -*-

import time


def run():
    while True:
        with open('/tmp/a.txt', 'a+') as fd:
            fd.write('running....\n')
        time.sleep(3)
