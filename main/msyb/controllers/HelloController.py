#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from os  import path
from flask import render_template, Blueprint, url_for, redirect, session, Response,current_app

from main.msyb.utils.common import response

# 定义蓝图类似于java的controller
hello_blueprint = Blueprint(
    'hello',
    __name__,
    # path.pathdir ==> ..
    template_folder=path.join(path.pardir,path.pardir, 'webapp', 'templates'),
    # Prefix of Route URL
    url_prefix='/hello'
)


@hello_blueprint.route("/world", methods=["GET","POST"])
def hello():
    print "adad"
    return response({"asd":"你好"})


@hello_blueprint.route("/ticket", methods=["GET"])
def ticket():

    from search_ticket import SearchTicket
    ticket = SearchTicket()
    data = ticket.do()
    # return response(data)
    # print path.join(path.pardir, 'templates', 'webapp', 'main')


    return render_template('chepiao.html',
                           data=data)