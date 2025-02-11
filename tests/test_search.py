import pytest


@pytest.mark.parametrize('name', [
    'Бэтмобиль',
    '5080'
])
def test_finding_items(start_page, name):
    start_page.navigate()
    start_page.finditem(name)
    start_page.page.wait_for_timeout(500)
    start_page.assert_finding_items()
