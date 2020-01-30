from __future__ import absolute_import

import six
from jsonschema import ValidationError


def invalid_schema(func):
    def inner(self, *args, **kwargs):
        with self.assertRaises(ValidationError):
            func(self)

    return inner


def invalid_schema_with_error_message(message):
    def decorator(func):
        def inner(self, *args, **kwargs):
            with self.assertRaises(ValidationError) as cm:
                func(self)
            found_message = six.text_type(cm.exception)
            if found_message != message:
                assert found_message == message

        return inner

    return decorator
