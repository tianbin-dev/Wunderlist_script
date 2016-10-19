# -*- coding: utf-8 -*-

class MarkdownWriter:

    def __init__(self,filename):
        self.filename = filename

    def open_file(self):
        self.file = open(self.filename,'w')

    def close_file(self):
        self.file.close()

    def write_blog_head(self,title,date,categories,tags,des):
        self.file.write('---\ntitle: '+title+' \ndate: '+date+' \ncategories: '+categories+' \ntags: '+tags+' \n---\n\n'+des+'\n \n <!-- more -->\n')

    def write_task_title(self,task_title):
        self.file.write(task_title+'\n')

    def write_subtask_title_list(self,subtask_title_list):
        for subtask_title in subtask_title_list: 
            self.file.write(subtask_title+'\n')
