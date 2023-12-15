

try:
    raise ValueError('oops')
except ValueError as error:
    print(f'hola \t {error}')
    error_str = f'Could not find file, initializing empty dataframe It {error}'
    print(error_str)
