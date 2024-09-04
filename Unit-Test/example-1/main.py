def some_function(num):
    try:
        return int(num) + 5
    except ValueError as e:
        print(f'ValueError:\n{e}')
        return e
    except TypeError as e:
        print(f'TypeError:\n{e}')
        return e