from model.group import Group

def test_mod_first_group(app):
  app.session.login(username="admin", password="secret")
  app.group.mod_first_group(Group(name="1", header="1", footer="1"))
  app.session.logout()