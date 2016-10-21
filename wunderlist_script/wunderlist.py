# -*- coding: utf-8 -*-

from parse_json import ParseJson
from qingdan import Qingdan
from task import Task
from markdown_writer import MarkdownWriter
from markdown_formatter import MarkdownFormatter

parse_json = ParseJson()

qingdan = parse_json.parse('data.json','OpenSource')

writer = MarkdownWriter('blog.md')

formatter = MarkdownFormatter()

writer.open_file()

for task in qingdan.tasks:
    task_title = formatter.generate_H2(task.title)
    writer.write_task_title(task_title)
    for subtask in task.subtasks:
        subtask.format_when_contain_url()
        subtask_title = formatter.generate_list_item(subtask.title)
        writer.write_subtask_title(subtask_title)
writer.close_file()
