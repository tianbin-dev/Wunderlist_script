# -*- coding: utf-8 -*-
class Task:
    def __init__(self):
        self.title = ''
        self.subtasks = []

    def set_title(self, title):
        self.title = title

    def set_subtasks(self, subtasks):
        self.subtasks = subtasks
