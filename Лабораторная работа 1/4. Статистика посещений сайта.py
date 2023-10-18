users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

statistics = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

quantity = len(users)
unique = len(set(users))

statistics["Общее количество"] = quantity
statistics["Уникальные посещения"] = unique

print(statistics)
