# -*- coding: utf-8 -*-
from model.contact import Contact

def test_mod_contact(app):
  app.contact.modify_first(Contact(firstname="Иван", lastname="Иванов", nickname="ПОМИДОР"))
