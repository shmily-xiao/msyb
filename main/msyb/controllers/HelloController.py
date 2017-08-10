#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from flask import render_template, Blueprint, url_for, redirect, session, Response,current_app

from main.msyb.utils.common import response

# 定义蓝图类似于java的controller
hello_blueprint = Blueprint(
    'hello',
    __name__,
    # path.pathdir ==> ..
    # template_folder=path.join(path.pardir, 'templates', 'blog'),
    # Prefix of Route URL
    url_prefix='/hello'
)


@hello_blueprint.route("/world", methods=["GET","POST"])
def hello():
    print "adad"
    return response({"asd":"你好"})