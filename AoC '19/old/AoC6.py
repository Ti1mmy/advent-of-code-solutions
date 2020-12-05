
list = []
newlist = []
planets = []
visited = []
indirect_orbits = 0
exit = True
while True:
    x = input()
    if x == "":
        break
    else:
        list.append(x)
print(list)
for orbit in list:
    newlist.append(orbit.split(")"))
print(newlist)
for i in range(len(newlist)):
    if newlist[i][0] not in planets:
        planets.append([newlist[i][0]])
print(planets)
for j in range(len(planets)):
    for i in newlist:
        if planets[j][0] == i[0]:
            planets[j].append(i[1])
newplanets = []
for i in range(len(planets)):
    if planets[i] not in newplanets:
        newplanets.append(planets[i])
print(newplanets)
direct_orbits = 0
for i in range(len(newplanets)):
    for k in range(len(newplanets[i])):
        direct_orbits += 1
direct_orbits -= len(newplanets)
print(direct_orbits)
for i in range(len(newplanets)):
    if 'C' in newplanets[i]:
        print(newplanets[i].index('C'))
points = []
for i in range(len(newplanets)):
    for q in range(len(newplanets[i])):
        if newplanets[i][q] not in points:
            points.append(newplanets[i][q])
print(points)
for l in range(len(points)):
    check = []
    for i in range(len(newplanets)):
        if points[l] in newplanets[i]:
            indirect_orbits += 1

# while exit:
#     for i in range(len(newplanets)):
#         check = []
#         for l in range(len(newplanets)):
#             if newplanets[i][-1] in newplanets[l] and newplanets[i][-1] not in visited and indirect_orbits not in visited:
#                 indirect_orbits += 1
#             if newplanets[i][-1] in newplanets[i]:
#                 check.append(newplanets[i].index(newplanets[i][-1]))
#             if len(check) < 2 and len(visited) > len(newplanets):
#                 exit = False
#         visited.append((newplanets[i][-1], indirect_orbits))
print(indirect_orbits)
print(direct_orbits)
print(indirect_orbits + direct_orbits)

    