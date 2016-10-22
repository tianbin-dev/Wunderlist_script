# -*- coding: utf-8 -*-
class MarkdownWriter:

    def __init__(self, filename):
        self.file = open(filename, 'w')

    def open_file(self):
        pass

    def close_file(self):
        self.file.close()

    def write_task_title(self, task_title):
        self.file.write('\n' + task_title + '\n\n')

    def write_subtask_title(self, subtask_title):
        self.file.write(subtask_title + '\n')
