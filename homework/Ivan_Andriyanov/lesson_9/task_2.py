temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
                22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]


def good_temp(d):
    if d < 29:
        return True


new_list = list(filter(good_temp, temperatures))

print(sorted(new_list))

print("Самая высокая температура", max(new_list), "градусов")
print("Самая низкая температура", min(new_list), "градусов")
print(f"Средняя температура, {int(sum(new_list) / len(new_list))} градусов")
