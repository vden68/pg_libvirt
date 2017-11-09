# -*- coding: utf-8 -*-
__author__ = 'vden'
import pytest


def test_creating_virtual_machine(app):
    conn_open_kvm = app.conn_kvm.connection_open()
    conn_open_kvm2 = app.conn_kvm.connection_open()

    conn_open_kvm.close()
    #conn_open_kvm2.close()