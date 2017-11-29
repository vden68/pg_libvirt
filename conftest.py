# -*- coding: utf-8 -*-
import json
import os.path
import pytest

from model.pgl_kvm import Pgl_kvm
from model.pgl_ssh import Pgl_ssh

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
    global target

    if target is None:
        pgl_kvm_config= load_config(request.config.getoption("--target"))["pgl_kvm"]
        pgl_kvm= Pgl_kvm(name_sourse_image=pgl_kvm_config["name_sourse_image"],
                          prefix=pgl_kvm_config["prefix"],
                          number_test_set=pgl_kvm_config["number_test_set"])

        pgl_ssh_config= load_config(request.config.getoption("--target"))["pgl_ssh"]
        pgl_ssh= Pgl_ssh(ip=pgl_ssh_config["ip"], username=pgl_ssh_config["username"],
                         password=pgl_ssh_config["password"], password_root=pgl_ssh_config["password_root"])

    if fixture is None :
        fixture = Application(pgl_kvm, pgl_ssh)

    request.addfinalizer(fixture.destroy)
    return fixture



def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="target.json")