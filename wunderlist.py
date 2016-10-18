# -*- coding: utf-8 -*-

from parse_json import ParseJson
from qingdan import Qingdan
from task import Task

parse_json = ParseJson()

qingdan = parse_json.parse('data.json','OpenSource')

for task in qingdan.tasks:
    print(task.title)
