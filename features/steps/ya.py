"""ya.ru feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('e2e/ya.feature', 'посещаю фронт')
def test_посещаю_фронт():
    """посещаю фронт."""


@when('я ya.ru')
def _():
    """я ya.ru."""
    # raise NotImplementedError


@when('я смотрю на картику')
def _():
    """я смотрю на картику."""
    # raise NotImplementedError

