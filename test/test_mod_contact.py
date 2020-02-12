from model.contact import Contact
from random import randrange

# Не работает
def test_mod_contact_firstname(app):
    if app.contact.count() == 0:
       app.contact.create(Contact(firstname="Создан чтобы измениться"))
     # app.contact.modify_first(Contact(firstname="Иван"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Иван")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
