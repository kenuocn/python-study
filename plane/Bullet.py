# -*- coding:utf-8 -*-
from BaseBullet import BaseBullet


class Bullet(BaseBullet):
    def __init__(self, screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x + 40, y - 20, "./resource/bullet.png")

    # 子弹步长
    def move(self):
        self.y -= 10

    # 判断子弹y轴是否已经越界
    def judge(self):
        if self.y < 0:
            return True
        else:
            return False
