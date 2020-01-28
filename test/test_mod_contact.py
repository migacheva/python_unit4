# -*- coding: utf-8 -*-
from model.contact import Contact

def test_mod_contact(app):
  app.session.login(username="admin", password="secret")
  app.contact.modify_first(Contact(firstname="Иван", lastname="Иванов", nickname="ПОМИДОР"))
  app.session.logout()
