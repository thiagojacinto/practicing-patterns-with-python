#!bin/python3
# -*- coding: UTF-8 -*-

class Budget(object):
  
    def __init__(self, value) -> None:
        self.__value = value

    @property
    def value(self):
        return self.__value
