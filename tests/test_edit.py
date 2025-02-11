from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


@pytest.mark.parametrize('oldname, newname, oldprice, newprice, info, url', [
    ('Кукуруза', 'Кукуруза', '200', '240', 'Вкусно и точка',
     'https://cdn.100sp.ru/pictures/949697343'),
    ('БУ Кукуруза', 'БУ Кукуруза', '300', '290', 'Уже была использована',
     'https://nn.zenmod.shop/image/cache/catalog/Liquid/Capella/popcorn-800x800.jpg?1470746552'),
    ('Огурец', 'Огурец гладкий', '70', '90', 'Слегка залежался',
     'https://main-cdn.sbermegamarket.ru/hlr-system/703/963/118/221/18/100048551482b0.jpg')
])
def test_edit_item(start_page, oldname, newname, oldprice, newprice, info, url):
    start_page.navigate()
    start_page.finditem(oldname)
    start_page.page.wait_for_timeout(500)
    start_page.page.locator('.css-1n43xc7').get_by_text(oldprice).click()
    start_page.edititem(newname, newprice, info, url)
    start_page.navigate()
    start_page.finditem(newname)
    start_page.page.wait_for_timeout(500)
    expect(start_page.page.locator('.css-1n43xc7').get_by_text(newprice), "Не найдено").to_contain_text(newprice)
