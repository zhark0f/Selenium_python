import pytest

# если тест неожиданно пройдет с пометкой xfail, при установке параметра strict=True, в консоль выведется сообщение failed


@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False
