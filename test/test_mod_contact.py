# -*- coding: utf-8 -*-
from model.contact import Contact

def test_mod_contact_firstname(app):
  app.contact.modify_first(Contact(firstname="Иван"))

def test_mod_contact_lastname(app):
  app.contact.modify_first(Contact(lastname="Иванов"))