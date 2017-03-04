#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import sys
import subprocess


def get_color(c, s):
    return "\033[3%sm%s\033[0m" % (c, s)


def red(s):
    return get_color(1, s)


def green(s):
    return get_color(2, s)


def print_ok(check_status):
    fmt = green("[  OK  ]    %s" % check_status)
    print fmt


def print_error(check_status, recomm=''):
    if not check_status.endswith("."):
        check_status += "."
    fmt = red("[  ERROR  ]    %s %s" % (check_status, recomm))
    print fmt


def print_title(title):
    print "\n"
    t = "%s  %s  %s" % ("=" * 30, title, "=" * 30)
    print t


def get_logger():
    logging.basicConfig(filename='build_doc.log',
                        level=logging.DEBUG,
                        mode="w",
                        format='%(asctime)s %(levelname)s  %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        )
    _logger = logging.getLogger()
    _logger.setLevel(logging.INFO)
    return _logger


def run(cmd):
    logging.info("cmd: %s" % cmd)
    p = subprocess.Popen(cmd,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell=True)
    std_out, std_err = p.communicate()
    if std_err:
        logger.info("cmd std_err: %s" % std_err)
        raise Exception("cmd: %s, std_err: %s" % (cmd, std_err))
    else:
        logger.info("cmd result: %s" % std_out)
        return std_out


if __name__ == '__main__':
    logger = get_logger()
    print_title("开始生成html")
    try:
        run("raml2html -i raml/api.raml -o index.html")
    except Exception as e:
        print_error("文档生成失败", e.message)
        sys.exit(1)

    print_ok("生成成功，开始替换静态资源")
    try:
        a = open("index.html", "r").read()
        a = a.replace("https://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/", "static/")
        a = a.replace("https://cdnjs.cloudflare.com/ajax/libs/highlight.js/8.1/styles/", "static/")
        a = a.replace("https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.3.0/styles/", "static/")
        a = a.replace("https://code.jquery.com/", "static/")
        a = a.replace("https://netdna.bootstrapcdn.com/bootstrap/3.1.1/js/", "static/")
        a = a.replace("https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.3.0/", "static/")
        # 替换数据类型
        a = a.replace("boolean", "object")
        a = a.replace("file", "array")
        print_ok("静态资源替换成功，开始写入到html中")
        b = open("index.html", "w")
        b.write(a)
        b.close()
        print_ok("写入成功！")
    except Exception as e:
        print_error("替换失败", e.message)
    print_title("生成html结束")
