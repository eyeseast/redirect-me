#!/usr/bin/env python
"""
Simple redirection from one host to another
"""
import os
import sys

from flask import Flask, redirect, request

app = Flask(__name__)

REDIRECT_HOST = os.environ.get('REDIRECT_HOST', 'http://example.com')
REDIRECT_CODE = int(os.environ.get('REDIRECT_CODE', 302))


@app.route('/')
@app.route('/<path:path>')
def root(path=None):
    """
    join REDIRECT_HOST to path
    """
    dest = REDIRECT_HOST + request.path
    return redirect(dest, REDIRECT_CODE)


if __name__ == '__main__':
    app.run(debug=True)