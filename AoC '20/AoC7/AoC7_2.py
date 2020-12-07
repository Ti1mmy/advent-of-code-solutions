with open("AoC7.txt", 'r') as File1:
    info = []
    for line in File1:
        info.append(line.split("\n")[0])
bag_list = []
for bag_info in info:
    if bag_info.split(" contain ")[1::] == ['no other bags.']:
        bags = ['no other bags.']
    else:
        bags = []
        for bag in bag_info.split(" contain ")[1::]:
            for thing in bag.split(", "):
                bags.append([int(thing[0]),
                            thing.split("bag")[0][2:-1]])
    contains = [
        bag_info.split(' bags')[0],
        bags
    ]
    bag_list.append(contains)
gold = 0
gold_contains = []
for bag in bag_list:
    if "shiny gold" in bag[0]:
        gold_contains.append(bag[1])
to_add = []
for bag in bag_list:
    for colour in gold_contains[0]:
        if bag[0] == colour[1]:
            to_add.append(bag[1])
    for add in to_add:
        if add not in gold_contains:
            gold_contains.append(add)
print(gold_contains)
for bag in bag_list:
    for individual in gold_contains:
        for colour in individual:
            if bag[0] == colour[1]:
                to_add.append(bag[1])
        for add in to_add:
            if add not in gold_contains:
                gold_contains.append(add)
print(gold_contains)
for bag in bag_list:
    for individual in gold_contains:
        for colour in individual:
            if bag[0] == colour[1]:
                to_add.append(bag[1])
        for add in to_add:
            if add not in gold_contains:
                gold_contains.append(add)
print(gold_contains)
for bag in bag_list:
    for individual in gold_contains:
        for colour in individual:
            if bag[0] == colour[1]:
                to_add.append(bag[1])
        for add in to_add:
            if add not in gold_contains:
                gold_contains.append(add)
print(gold_contains)
for bag in bag_list:
    for individual in gold_contains:
        for colour in individual:
            if bag[0] == colour[1]:
                to_add.append(bag[1])
        for add in to_add:
            if add not in gold_contains:
                gold_contains.append(add)
print(gold_contains)
print(bag_list)
bags = 1
level = 0
for gold in gold_contains:
    print(gold)
print(bags)
# for bag in bag_list:
#     for contain in bag[1]:
#         if contain[1] in contains_gold and bag[0] not in contains_gold:
#             contains_gold.append(bag[0])
# for bag in bag_list:
#     for contain in bag[1]:
#         if contain[1] in contains_gold and bag[0] not in contains_gold:
#             contains_gold.append(bag[0])
# for bag in bag_list:
#     for contain in bag[1]:
#         if contain[1] in contains_gold and bag[0] not in contains_gold:
#             contains_gold.append(bag[0])
# for bag in bag_list:
#     for contain in bag[1]:
#         if contain[1] in contains_gold and bag[0] not in contains_gold:
#             contains_gold.append(bag[0])
# for bag in bag_list:
#     for contain in bag[1]:
#         if contain[1] in contains_gold and bag[0] not in contains_gold:
#             contains_gold.append(bag[0])
# print(contains_gold)

