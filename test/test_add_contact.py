# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Атабек", lastname="Бердыбердыев",
                               homephone="homephone1", workphone="work2",
                               mobilephone="mobile3", secondaryphone="secondary4"))
