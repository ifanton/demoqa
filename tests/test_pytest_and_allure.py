import pytest


# Принудительный пропуск теста.
# Декоратор устанавливается перед функцией теста.
# Тест пропускается, в PyTest и Allure помечается как “skipped - тест пропущен”
@pytest.mark.skip(reason='Причина пропуска')
def test_skip():
    assert True


# condition - условие для пометки тестовой функции как xfail
# reason - причина, по которой тестовая функция помечена как xfail
# такой тест будет помечен как ожидаемый сбой:
#     Если тест упадет он пометится как skipped - тест пропущен
#     Если тест пройдет он пометится как passed - тест пройден
#     в обоих случаях в отчет добавится тег ожидаемый сбой
@pytest.mark.xfail(condition=True, reason='Причина, по которой тестовая функция помечена как xfail')
def test_xfail_1():
    assert False


@pytest.mark.xfail(condition=True, reason='Причина, по которой тестовая функция помечена как xfail')
def test_xfail_2():
    assert True


# Пропуск теста, по условию
# если условие булево (True, False), то обязателен второй параметр
@pytest.mark.skipif(condition='2 + 2 != 5')
def test_skip_by_triggered_condition():
    pass


# Запуск тестов по параметрам
@pytest.mark.parametrize('param', [1, 2, 3, 4, 6])
def test_parametrize(param):
    assert (param % 2) == 0
