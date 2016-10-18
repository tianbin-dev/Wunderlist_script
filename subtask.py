# -*- coding: utf-8 -*-
class Subtask:

    def __init__(self):
        self.title = ''

    def set_title(self,title):
        self.title = title

    def __str__(self):
        return self.title
