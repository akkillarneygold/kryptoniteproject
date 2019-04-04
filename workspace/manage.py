#!/usr/bin/env python
import os
import sys
from flask import Flask
from flask_pymongo import PyMongo
from flask import Flask, render_template
import json


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "visualdata.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                
            )
        raise
    execute_from_command_line(sys.argv)
