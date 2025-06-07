my_dict = {
    "tuple": (1, 2, 3, 4, 5),
    "list": ["dog", "cat", "mouse", "monkey", "lion"],
    "dict": {
        "human": "Ivan",
        "cat": "Mashka",
        "dog": "Kemal",
        "monkey": "Nik",
        "lion": "Simba"
    },
    "set": {10, 20, 30, 40, 50}
}

print(f'последний элемент что хранится под ключом "tuple" : {my_dict["tuple"][-1]}')
my_dict["list"].append("tiger")
print(f'добавлен последний элемент в спискок что хранится под ключом "list" : {my_dict["list"]}')
my_dict["list"].pop(1)
print(f'Удален второй элемент списка что хранится под ключом "list" : {my_dict["list"]}')
my_dict["dict"][('i am a tuple',)] = "Добавил значение"
print(f'Добавил ключ и значение {my_dict["dict"]}')
del my_dict["dict"]["dog"]
print(f'удалил эллемент dog {my_dict["dict"]}')
my_dict["set"].add(60)
print(f'Добавил новый элемент в множество {my_dict["set"]}')
my_dict["set"].discard(60)
print(f'удалил новый элемент в множестве {my_dict["set"]}')
