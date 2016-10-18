# -*- coding: utf-8 -*-
import json
from pprint import pprint
from task import Task
from subtask import Subtask
from qingdan import Qingdan

class ParseJson:

    def parse(self,filename,qingdan_name):

        with open(filename) as data_file:    
            data = json.load(data_file)
        lists = data.get('data').get('lists')
        qingdan_id = ""
        for qingdan in lists:
            title = qingdan.get('title')
            if title == qingdan_name:
                qingdan_id = qingdan.get('id')
                break

        tasks = data.get('data').get('tasks')
        subtasks = data.get('data').get('subtasks')

        myqingdan = Qingdan()
        mytasks = []
        myqingdan.set_tasks(mytasks)

        for task in tasks:
            list_id = task.get('list_id')
            if list_id == qingdan_id:
                mytask = Task()
                mytask.set_title(task.get('title'))
                print('title--'+mytask.title)
                mysubtasks = []
                for subtask in subtasks:
                    task_id = subtask.get('task_id')
                    if task_id == task.get('id'): 
                        mysubtask = Subtask()
                        mysubtask.set_title(subtask.get('title'))
                        mysubtasks.append(mysubtask)
                        print('subtitle--'+mysubtask.title)
                mytask.set_subtasks(mysubtasks)
                mytasks.append(mytask)
                print(mytask.title)


        for task in myqingdan.tasks:
            print(task.title)
