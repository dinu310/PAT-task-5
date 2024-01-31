data = [10, 501, 22, 37, 100, 999, 87, 351, 'hello', 'world']
result = all(lambda x: isinstance(x, (int, str)) for x in data)
print(result)
result = [i for i, x in enumerate(data) if isinstance(x, (int))]
print(result,"elements are integers")
result = [i for i, x in enumerate(data) if isinstance(x, (str))]
print(result,"elements are string")
