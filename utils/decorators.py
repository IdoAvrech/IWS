"""
 Author: Ido
 Date: 27/08/21
 Purpose: Create fancy decorators to make
"""
from functools import wraps


def inject_variables(arg_parser):
    """ Decorator factory. """


    def variable_injector(func):
        """ Decorator. """
        @wraps(func)
        def decorator(*args, **kwargs):
            func_globals = func.__globals__

            # Save copy of any global values that will be replaced.
            saved_values = {key: func_globals[key] for key in context
                                                        if key in func_globals}
            func_globals.update(context)
            try:
                result = func(*args, **kwargs)
            finally:
                func_globals.update(saved_values)  # Restore replaced globals.

            return result

        return decorator

    return variable_injector


