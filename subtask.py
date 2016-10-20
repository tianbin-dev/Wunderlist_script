# -*- coding: utf-8 -*-

import re

class Subtask:

    def __init__(self):
        self.title = ''

    def set_title(self,title):
        self.title = title

    def __str__(self):
        return self.title

    def format(self):
        subtask_title = ''
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', self.title)
        if len(urls) > 0:
            url_start_index = self.title.index(urls[0])
            subtask_title += str(self.title[0:url_start_index]).strip()
        for url in urls:
            subtask_title += '\n'+str(url).strip()
        self.title = subtask_title

