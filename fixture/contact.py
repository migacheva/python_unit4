
class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # fill group firm
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # submit group creation
        wd.find_element_by_name("submit").click()
        # self.return_to_groups_page()

    def modify_first(self, contact):
        wd = self.app.wd
        # Выбрать элемент для изменения (1й) selected[]
        wd.find_element_by_name("selected[]").click()
# Не удается обратиться к элементу иконке
        # Нажать на карандаш title Edit
        wd.find_element_by_css_selector("tbody tr:nth-child(2) td:nth-child(8) a img").click()
        # Изменить имя, фамилию, никнейм
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # Нажать обновить name="update"
        wd.find_element_by_name("update").click()
        # Вернуться на домашнюю страницу

    def delete_first_contact(self):
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
# Не удается выбрать кнопку удаления
        wd.find_element_by_name("Delete").click()
        # Нажать ок на всплывающем окне
# как работать со всплывающим окном?
        # Вернуться на главную