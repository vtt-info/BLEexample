"""
    Mocks creating module
"""

class Mock:
    def __init__(self):
        self._calls_matching = {}
        self._actual_calls = []
        self._actual_parameters = []

    def when(self, method_name, required_args=None, return_value=None, raise_exception=None):
        if method_name not in self._calls_matching.keys():
            self._calls_matching[method_name] = {'params': [], 'return_values': [], 'raise_exception': []}
        self._calls_matching[method_name]['params'].append(required_args)
        self._calls_matching[method_name]['return_values'].append(return_value)
        self._calls_matching[method_name]['raise_exception'].append(raise_exception)

    def has_been_called(self, times=1, method=None):
        if method is None:
            if self._actual_calls and len(self._actual_calls) == times:
                return True
        else:
            if self._actual_calls and self._actual_calls.count(method) == times:
                return True
        return False

    def has_been_called_with(self, method_name, args, times=None):
        if self._actual_calls:
            indices = [i for i, m in enumerate(self._actual_calls) if m == method_name]
            if indices:
                found = [self._actual_parameters[j] for j in indices]
                if args in found:
                    count = found.count(args)
                    if times is not None:
                        return count == times
                    else:
                        return True
        return False

    def reset(self):
        self.__init__()

    def _wrapper(self, method_name):
        def func(*args, **kwargs):
            self._actual_calls.append(method_name)
            if args:
                self._actual_parameters.append(args)
            elif kwargs:
                self._actual_parameters.append(kwargs)
            else:
                self._actual_parameters.append(())
            if method_name in self._calls_matching.keys():
                if args:
                    return self._get_return_value_or_raise_exception(method_name, args)
                elif kwargs:
                    return self._get_return_value_or_raise_exception(method_name, kwargs)
                else:
                    return self._get_return_value_or_raise_exception(method_name, None)
            return None
        return func

    def _get_return_value_or_raise_exception(self, method_name, parameters):
        if parameters in self._calls_matching[method_name]['params']:
            return self._on_parameters_get_return_value_or_raise(method_name, parameters)
        elif None in self._calls_matching[method_name]['params']:
            return self._on_parameters_get_return_value_or_raise(method_name, None)

    def _on_parameters_get_return_value_or_raise(self, method_name, parameters):
        index = self._calls_matching[method_name]['params'].index(parameters)
        if self._calls_matching[method_name]['raise_exception'][index] is not None:
            raise self._calls_matching[method_name]['raise_exception'][index]
        return self._calls_matching[method_name]['return_values'][index]


def create_mock(cls=None):
    newMock = Mock()
    if cls is not None:
        for attr in dir(cls):
            if callable(getattr(cls, attr)):
                setattr(newMock, attr, newMock._wrapper(attr))
    return newMock
