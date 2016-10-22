# -*- coding: utf-8 -*-
from parse_json import *
from markdown_writer import MarkdownWriter
from markdown_formatter import *

qingdan = parse_json('data.json', 'qingdan_name')

writer = MarkdownWriter('blog.md')

writer.open_file()

for task in qingdan.tasks:

    task_title = generate_h2(task.title)
    writer.write_task_title(task_title)

    for subtask in task.subtasks:
        subtask.format_when_contain_url()
        subtask_title = generate_list_item(subtask.title)
        writer.write_subtask_title(subtask_title)

writer.close_file()

print ('done')
