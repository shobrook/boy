import statcode.statcode
import pytest


def test_valid_numeric_param():
    content = None
    code_descriptions, num, status_code = statcode.statcode.get_yaml_dictionary("200")
    content = statcode.statcode.get_content(code_descriptions, status_code)
    assert content is not None
    return


def test_invalid_numeric_param():
    content = None
    code_descriptions, num, status_code = statcode.statcode.get_yaml_dictionary("999")
    try:
        content = statcode.statcode.get_content(code_descriptions, status_code)
    except KeyError:
        assert content is None
    return


def test_header_param():
    content = None
    code_descriptions, num, status_code = statcode.statcode.get_yaml_dictionary("Content-Length")
    content = statcode.statcode.get_content(code_descriptions, status_code)
    assert content is not None
    return


def test_lower_case_header_param():
    content = None
    code_descriptions, num, status_code = statcode.statcode.get_yaml_dictionary("content-md5")
    content = statcode.statcode.get_content(code_descriptions, status_code)
    assert content is not None
    return


def test_case_insensitive_header_params():
    code_descriptions, num, status_code = statcode.statcode.get_yaml_dictionary("cache-control")
    first_content = statcode.statcode.get_content(code_descriptions, status_code)

    code_descriptions, num, status_code = statcode.statcode.get_yaml_dictionary("Cache-Control")
    second_content = statcode.statcode.get_content(code_descriptions, status_code)

    assert first_content == second_content
    return


def test_invalid_header_param():
    content = None
    code_descriptions, num, status_code = statcode.statcode.get_yaml_dictionary("invalid_parameter")
    try:
        content = statcode.statcode.get_content(code_descriptions, status_code)
    except KeyError:
        assert content is None
    return

