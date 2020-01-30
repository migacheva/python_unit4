# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="dfgdfg", header="dfgdfgghjghj", footer="dfgdfggdfgdfgghjghjghj"))
    # для проверки умного логина и логаута
    # app.session.logout()

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
