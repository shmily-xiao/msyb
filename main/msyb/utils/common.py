#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from flask import Response

def response(content):
    return Response(json.dumps(content, ensure_ascii=False), mimetype='application/json')