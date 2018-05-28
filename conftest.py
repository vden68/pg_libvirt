# -*- coding: utf-8 -*-
import json
import os.path
import pytest

from model.pgl_kvm import Pgl_kvm
from model.pgl_ssh import Pgl_ssh
from model.conn_mmts import Conn_mmts
from model.mmts_data import Mmts_data

from fixture.application import Application
from fixture.mmts import Mmts

fixture = None
mmts_fixture = None
target = None
target_mmts = None


def load_target(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


def load_target_mmts(file):
    global target_mmts
    if target_mmts is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target_mmts = json.load(f)
    return target_mmts


def reading_parameters_from_jenkins(jen_param=None):

    try:
        name_sourse_image_j= os.environ["name_sourse_image"]
        prefix_J= os.environ["prefix"]
        number_test_set_J= os.environ["number_test_set"]
        path_meta_json_J= os.environ["path_meta_json"]

        jen_param.name_sourse_image= name_sourse_image_j
        jen_param.prefix= prefix_J
        jen_param.number_test_set= number_test_set_J
        jen_param.path_meta_json= path_meta_json_J
        print('jen_param=', jen_param)
    except:
        pass

    return jen_param


@pytest.fixture(scope = 'session')
def app(request):
    global fixture
    global target

    if target is None:
        pgl_kvm_config= load_target(request.config.getoption("--target"))["pgl_kvm"]
        pgl_kvm= Pgl_kvm(name_source_image=pgl_kvm_config["name_source_image"],
                         prefix=pgl_kvm_config["prefix"],
                         number_test_set=pgl_kvm_config["number_test_set"],
                         path_meta_json=pgl_kvm_config['path_meta_json'])

        pgl_kvm= reading_parameters_from_jenkins(jen_param=pgl_kvm)

        pgl_ssh_config= load_target(request.config.getoption("--target"))["pgl_ssh"]
        pgl_ssh= Pgl_ssh(ip=pgl_ssh_config["ip"], username=pgl_ssh_config["username"],
                         password=pgl_ssh_config["password"], password_root=pgl_ssh_config["password_root"])


    if fixture is None :
        fixture = Application(pgl_kvm, pgl_ssh)

    request.addfinalizer(fixture.destroy)
    return fixture


@pytest.fixture(scope = 'session')
def mmts(request):
    global mmts_fixture
    global target_mmts

    if target_mmts is None:
        conn_mmts_config = load_target_mmts(request.config.getoption("--target_mmts"))["conn_mmts"]
        conn_mmts = Conn_mmts(dbname=conn_mmts_config["dbname"], user=conn_mmts_config["user"],
                              password=conn_mmts_config["password"], conn_strings=conn_mmts_config["conn_strings"],
                              max_nodes=conn_mmts_config["max_nodes"], arbiter_port=conn_mmts_config["arbiter_port"],
                              heartbeat_send_timeout=conn_mmts_config["heartbeat_send_timeout"],
                              heartbeat_recv_timeout=conn_mmts_config["heartbeat_recv_timeout"],
                              min_recovery_lag=conn_mmts_config["min_recovery_lag"],
                              max_recovery_lag=conn_mmts_config["max_recovery_lag"],
                              ignore_tables_without_pk=conn_mmts_config["ignore_tables_without_pk"],
                              cluster_name=conn_mmts_config["cluster_name"],
                              referee_connstring=conn_mmts_config["referee_connstring"],
                              monotonic_sequences=conn_mmts_config["monotonic_sequences"])

        mmts_data_config = load_target_mmts(request.config.getoption("--target_mmts"))["mmts_data"]
        mmts_data=[]
        for mmts_data_c in mmts_data_config:
            mmts_data.append(Mmts_data(images=mmts_data_c["images"], images_ip=mmts_data_c["images_ip"],
                                       host=mmts_data_c["host"], node_id=mmts_data_c["node_id"],
                                       break_connection=mmts_data_c["break_connection"], major_node=mmts_data_c["major_node"],
                                       max_workers=mmts_data_c["max_workers"], trans_spill_threshold=mmts_data_c["trans_spill_threshold"]))


    if mmts_fixture is None :
        mmts_fixture = Mmts(conn_mmts, mmts_data)

    request.addfinalizer(mmts_fixture.destroy)
    return mmts_fixture



def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--target_mmts", action="store", default="target_mmts.json")