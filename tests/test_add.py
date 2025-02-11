from playwright.sync_api import Playwright, sync_playwright, expect

import pytest


@pytest.mark.parametrize('name, price, info, url', [
    ('Бэтмобиль', '300000', 'Совсем как настоящий',
     'https://avatars.mds.yandex.net/get-vertis-journal/4469561/2019-10-03-61eb0625626a4f379b15b42b50acdc56'
     '.jpg_1622735939741/orig'),
    ('Бэтмобиль', '5000', 'А вот этот уже не совсем настоящий',
     'https://main-cdn.sbermegamarket.ru/big2/hlr-system/1657928/100000377360b0.jpg'),
    ('RTX 5080', '160000', 'Точно не сгорит',
     'https://avatars.mds.yandex.net/get-mpic/2017233/2a00000194d1ca1993d378c741a79bea88e4/orig')
])
def test_adding_new_item(start_page, name, price, info, url):
    start_page.navigate()
    start_page.addnewitem(name, price, info, url)
    start_page.navigate()
    start_page.finditem(name)
    expect(start_page.page.locator('.css-1n43xc7').get_by_text(price), "Не найдено").to_contain_text(price)
