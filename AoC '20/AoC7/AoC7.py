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
contains_gold = []
for bag in bag_list:
    for contain in bag[1]:
        if "shiny gold" in contain:
            contains_gold.append(bag[0])
for bag in bag_list:
    for contain in bag[1]:
        if contain[1] in contains_gold and bag[0] not in contains_gold:
            contains_gold.append(bag[0])
for bag in bag_list:
    for contain in bag[1]:
        if contain[1] in contains_gold and bag[0] not in contains_gold:
            contains_gold.append(bag[0])
for bag in bag_list:
    for contain in bag[1]:
        if contain[1] in contains_gold and bag[0] not in contains_gold:
            contains_gold.append(bag[0])
for bag in bag_list:
    for contain in bag[1]:
        if contain[1] in contains_gold and bag[0] not in contains_gold:
            contains_gold.append(bag[0])
for bag in bag_list:
    for contain in bag[1]:
        if contain[1] in contains_gold and bag[0] not in contains_gold:
            contains_gold.append(bag[0])
print(len(contains_gold))

