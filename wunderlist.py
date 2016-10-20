# -*- coding: utf-8 -*-

from parse_json import ParseJson
from qingdan import Qingdan
from task import Task
from markdown_writer import MarkdownWriter
from markdown_formatter import MarkdownFormatter

parse_json = ParseJson()

qingdan = parse_json.parse('data.json','OpenSource')

#for task in qingdan.tasks:
#    print(task.title)


writer = MarkdownWriter('blog.md')

formatter = MarkdownFormatter()

writer.open_file()

category_list = ['Android','OpenSource']
categories = formatter.generate_categories(category_list)

tag_list = ['Android','OpenSource']
tags = formatter.generate_tags(tag_list)

writer.write_blog_head('Android 开源项目','2016-10-19 10:08:50',categories,tags,'Android 开源代码干货，包括动画／自定义View／开源项目等，持续更新中~')

for task in qingdan.tasks:
    task_title = formatter.generate_H2(task.title)
    writer.write_task_title(task_title)
    for subtask in task.subtasks:
        subtask.format()
        subtask_title = formatter.generate_list_item(subtask.title)
        writer.write_subtask_title(subtask_title)
writer.close_file()
