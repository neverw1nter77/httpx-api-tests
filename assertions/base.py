from typing import Any, Sized

def assert_status_code(actual: int, expected: int):
    """
    Verifies that the actual response status code matches the expected one.

    :param actual: Actual response status code.
    :param expected: Expected status code.
    :raises AssertionError: If status codes do not match.
    """

    assert actual == expected, (
        f'Incorrect response status code.'
        f'Expected status code: {expected}.'
        f'Actual status code: {actual}'
    )


def assert_equal(actual: Any, expected: Any, name: str):
    """
    Verifies that the actual value matches the expected one.

    :param name: Name of the checked value.
    :param actual: Actual value.
    :param expected: Expected value.
    :raises AssertionError: If values do not match.
    """
    assert actual == expected, (
        f'Incorrect value: "{name}".'
        f'Expected value: {expected}.'
        f'Actual value: {actual}'
    )