from pytest import fixture


@fixture
def translator():
    from googletranslate import Translator
    return Translator()