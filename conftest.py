# -*- coding: utf-8 -*-
import pytest
import os.path
import json
from fixture.application import Application



fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture(scope = 'session')
def app(request):
    global fixture

    if fixture is None :
        fixture = Application()


    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="target.json")