# -*- coding: utf-8 -*-
def generate_h1(content):
    return '# ' + content


def generate_h2(content):
    return '## ' + content


def generate_H3(content):
    return '### ' + content


def generate_h4(content):
    return '#### ' + content


def generate_h5(content):
    return '##### ' + content


def generate_h6(content):
    return '###### ' + content


def generate_list_item(list_item):
    return '- ' + list_item


def generate_link(content, url):
    return '[' + content + '](' + url + ')'
