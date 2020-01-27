# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
  app.session.login(username="admin", password="secret")
  app.contact.create(Contact(firstname="Атабек", lastname="Бердыбердыев", nickname="АРБУЗ"))
  app.session.logout()
