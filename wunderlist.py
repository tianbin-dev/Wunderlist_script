# -*- coding: utf-8 -*-
import json
from pprint import pprint
from task import Task
from subtask import Subtask
from qingdan import Qingdan

with open('data.json') as data_file:    
        data = json.load(data_file)
        lists = data.get('data').get('lists')
        open_source_id = ""
        for qingdan in lists:
            title = qingdan.get('title')
            if title == 'OpenSource':
                open_source_id = qingdan.get('id')
                break
       # pprint(open_source_id)
        
        tasks = data.get('data').get('tasks')
        subtasks = data.get('data').get('subtasks')
        
        open_source_qingdan = Qingdan()
        mytasks = []
        open_source_qingdan.set_tasks(mytasks)
        
        for task in tasks:
            list_id = task.get('list_id')
            if list_id == open_source_id:
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
            

        for task in open_source_qingdan.tasks:
            print(task.title)
