def find_common_participants(first_group, second_group, split_type =','):
    first_group_list = first_group.split(split_type)
    second_group_list = second_group.split(split_type)
    first_group_list = set(first_group_list)
    result = list(first_group_list.intersection(second_group_list))
    result.sort()
    return result

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print("Общие участники: ", find_common_participants(participants_first_group, participants_second_group, '|'))