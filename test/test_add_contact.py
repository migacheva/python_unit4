# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
  app.contact.create(Contact(firstname="Атабек", lastname="Бердыбердыев", nickname="АРБУЗ"))
  app.contact.create(Contact(firstname="Атабек2", lastname="Бердыбердыев2", nickname="АРБУЗ2"))
  app.contact.create(Contact(firstname="Атабек333", lastname="Бердыбердыев333", nickname="АРБУЗ33"))
