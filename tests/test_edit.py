from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


@pytest.mark.parametrize('oldname, newname, oldprice, newprice, info, url', [
    ('Бэтмобиль', 'Бэтмобиль', '300000', '30000', 'Совсем как настоящий и точно не битый',
     'https://avatars.mds.yandex.net/get-vertis-journal/4469561/2019-10-03-61eb0625626a4f379b15b42b50acdc56'
     '.jpg_1622735939741/orig'),
    ('Бэтмобиль', 'Бэтмобиль', '2600', '5000', 'А вот этот уже не совсем настоящий',
     'https://main-cdn.sbermegamarket.ru/big2/hlr-system/1657928/100000377360b0.jpg'),
    ('RTX 5080', 'БУ RTX 5080', '160000', '16000', 'Уже сгорела',
     'https://17.img.avito.st/image/1/1.CI4Mgba6pGc6KGZiEPErxNQiomO4oqylvSKgb7gqpg.pU_wkoC3T2'
     '-Zx6TOV3hMWa288E_WNZao0ClKi9wNK0w')
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
