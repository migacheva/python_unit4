from model.group import Group

def test_modify_group_name(app):
  app.group.modify_first_group(Group(name="New group"))

def test_mod_first_header(app):
  app.group.modify_first_group_header(Group(header="New header"))
