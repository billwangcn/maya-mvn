# -*-coding:utf-8-*-
__author__ = 'wb'

import os, sys, time, uuid

strList = ['派索', '凯', '杰', '寇', '赞', '劳埃德', '加满都', '妮雅']


class UserUtils():
    def getCurrentTime(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def getUUID(self):
        return uuid.uuid4()

    def getCurrentPath(self):
        return os.getcwd()

    def getItem(self):
        result_i = ''
        result_j = ''

        for i, j in strList:
            print(i)
            print(j)
            result_i = i
            result_j = j
        return result_i, result_j


if __name__ == '__main__':
    ut = UserUtils()
    print(ut.getCurrentTime())
    print(ut.getUUID())
    print(ut.getCurrentPath())
    i,j=ut.getItem()

    print(i)
    print(j)