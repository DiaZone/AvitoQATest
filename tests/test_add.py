from playwright.sync_api import Playwright, sync_playwright, expect

import pytest


@pytest.mark.parametrize('name, price, info, url', [
    ('Кукуруза', '200', 'Вкусно и точка',
     'https://cdn.100sp.ru/pictures/949697343'
     '.jpg_1622735939741/orig'),
    ('БУ кукуруза', '300', 'Уже была использована',
     'https://nn.zenmod.shop/image/cache/catalog/Liquid/Capella/popcorn-800x800.jpg?1470746552'),
    ('Огурец', '70', 'Свежий, только сорванный с грядки',
     'https://main-cdn.sbermegamarket.ru/hlr-system/703/963/118/221/18/100048551482b0.jpg')
])
def test_adding_new_item(start_page, name, price, info, url):
    start_page.navigate()
    start_page.addnewitem(name, price, info, url)
    start_page.navigate()
    start_page.finditem(name)
    expect(start_page.page.locator('.css-1n43xc7').get_by_text(price), "Не найдено").to_contain_text(price)
