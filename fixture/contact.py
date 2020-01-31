
class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_create_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        # fill group firm
        self.fill_contact_form(contact)
        # submit group creation
        wd.find_element_by_name("submit").click()
        # self.return_to_groups_page()

    def select_first_contact(self):
        wd = self.app.wd
        # Выбрать элемент для изменения (1й) selected[]
        wd.find_element_by_name("selected[]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
# Не удается выбрать кнопку удаления
        wd.find_element_by_css_selector("div:nth-child(8) > input[type=button]").click()
        # Нажать ок на всплывающем окне
        # 19 | assertConfirmation | Delete 1 addresses? |  |
        obj = wd.switch_to.alert
        obj.accept()

    def modify_first(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        # Нажать на карандаш title Edit
        wd.find_element_by_css_selector("tbody tr:nth-child(2) td:nth-child(8) a img").click()
        # Изменить имя, фамилию, никнейм
        self.fill_contact_form(new_contact_data)
        # Нажать обновить name="update"
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
