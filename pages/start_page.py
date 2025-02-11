from playwright.sync_api import Page, expect


class StartPage:
    def __init__(self, page: Page):
        self.page = page
        self.name_input = page.locator("[placeholder='Название']")
        self.price_input = page.locator("[placeholder='Цена']")
        self.info_input = page.locator("[placeholder='Описание']")
        self.url_input = page.locator("[placeholder='URL изображения']")
        self.find_input = page.locator("[placeholder='Поиск по объявлениям']")

        self.new_name_input = self.page.locator("[name='name']")
        self.new_price_input = self.page.locator("[name='price']")
        self.new_info_input = self.page.locator("[name='description']")
        self.new_url_input = self.page.locator("[name='imageUrl']")

    def navigate(self):
        self.page.goto("http://tech-avito-intern.jumpingcrab.com/advertisements/")

    def addnewitem(self, name: str, price: str, info: str, url: str):
        self.page.get_by_role("button", name="Создать").click()
        self.name_input.fill(name)
        self.price_input.fill(price)
        self.info_input.fill(info)
        self.url_input.fill(url)
        self.page.get_by_role("button", name='Сохранить').click()

    def finditem(self, item_to_find: str):
        self.find_input.fill(item_to_find)
        self.find_input.press("Enter")
        # self.page.get_by_role("button", name="Найти").click()

    def edititem(self, name: str, price: str, info: str, url: str):
        self.page.locator(".css-nb383z > svg").click()
        self.new_name_input.fill(name)
        self.new_price_input.fill(price)
        self.new_info_input.fill(info)
        self.new_url_input.fill(url)
        self.page.locator(".css-nb383z > svg").click()

    def assert_finding_items(self):
        # counts = int(self.page.get_by_text("Найдено").text_content().split()[-1])
        expect(self.page.get_by_text("Найдено"), "Ошибка при поиске")
