# -*- coding: utf-8 -*-
__author__ = 'vden'
import os
import pytest
from fixture.fixlib.lib import Lib_helper

class Image_helper:
    def __init__(self, app):
        self.app = app
        self.flib = Lib_helper(self)


    def clone_an_image(self):

        with pytest.allure.step('Подключаемся к KVM'):
            conn_open_kvm = self.flib.connection_open()

        with pytest.allure.step('Проверяем на наличие образ %s' % self.app.pgl_kvm.name_sourse_image):
            lib_domain = self.flib.domain_check_for_availability(check_domain=self.app.pgl_kvm.name_sourse_image,
                                                                 conn=conn_open_kvm)
        if lib_domain is None:
            print('Cannot find image %s to be clone.' %self.app.pgl_kvm.name_sourse_image)
            exit(0)

        #if the domain is enabled we finish work domain
        if lib_domain.ID() != -1:
            self.flib.domain_shutdown_name(conn=conn_open_kvm, lib_name=lib_domain.name())

        with pytest.allure.step('Формируем название новой виртуальной машины'):
            clone_name = self.flib.create_clone_name(pgl_kvm=self.app.pgl_kvm, conn=conn_open_kvm)

        with pytest.allure.step('Клонируем образ %s в новый клон %s' %(self.app.pgl_kvm.name_sourse_image, clone_name)):
            self.flib.clone_image(clone_name=clone_name, name_image=self.app.pgl_kvm.name_sourse_image, conn=conn_open_kvm)

        conn_open_kvm.close()

        return clone_name


    def start_image(self, name_image):

        with pytest.allure.step('Подключаемся к KVM'):
            conn_open_kvm = self.flib.connection_open()

        with pytest.allure.step('Проверяем на наличие образ %s' % name_image):
            lib_domain = self.flib.domain_check_for_availability(check_domain=name_image,
                                                             conn=conn_open_kvm)
        if lib_domain is None:
            print('Cannot find image %s to be clone.' % name_image)
            exit(0)

        with pytest.allure.step('Стартуем виртуальную машину %s' % name_image):
            lib_domain= self.flib.start_image(lib_domain=lib_domain, conn=conn_open_kvm)

        conn_open_kvm.close()

        return lib_domain


    def rename_image(self, name_image, name_image_new):

        with pytest.allure.step('Подключаемся к KVM'):
            conn_open_kvm = self.flib.connection_open()

        with pytest.allure.step('Проверяем на наличие образ %s' % name_image):
            lib_domain = self.flib.domain_check_for_availability(check_domain=name_image,
                                                             conn=conn_open_kvm)

        if lib_domain is None:
            print('Cannot find image %s to be clone.' % name_image)
            exit(0)

        #if the domain is enabled we finish work domain
        if lib_domain.ID() != -1:
            self.flib.domain_shutdown_name(conn=conn_open_kvm, lib_name=lib_domain.name())

        with pytest.allure.step('Переименовываем виртуальную машину %s в %s' % (name_image, name_image_new)):
            self.flib.rename_image(name_image=name_image, name_image_new=name_image_new, conn=conn_open_kvm)



        conn_open_kvm.close()





