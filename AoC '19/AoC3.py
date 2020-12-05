first = "R997,D443,L406,D393,L66,D223,R135,U452,L918,U354,L985,D402,R257,U225,R298,U369,L762,D373,R781,D935,R363,U952,L174,D529,L127,D549,R874,D993,L890,U881,R549,U537,L174,U766,R244,U131,R861,D487,R849,U304,L653,D497,L711,D916,R12,D753,R19,D528,L944,D155,L507,U552,R844,D822,R341,U948,L922,U866,R387,U973,R534,U127,R48,U744,R950,U522,R930,U320,R254,D577,L142,D29,L24,D118,L583,D683,L643,U974,L683,U985,R692,D271,L279,U62,R157,D932,L556,U574,R615,D428,R296,U551,L452,U533,R475,D302,R39,U846,R527,D433,L453,D567,R614,U807,R463,U712,L247,D436,R141,U180,R783,D65,L379,D935,R989,U945,L901,D160,R356,D828,R45,D619,R655,U104,R37,U793,L360,D242,L137,D45,L671,D844,R112,U627,R976,U10,R942,U26,L470,D284,R832,D59,R97,D9,L320,D38,R326,U317,L752,U213,R840,U789,L152,D64,L628,U326,L640,D610,L769,U183,R844,U834,R342,U630,L945,D807,L270,D472,R369,D920,R283,U440,L597,U137,L133,U458,R266,U91,R137,U536,R861,D325,R902,D971,R891,U648,L573,U139,R951,D671,R996,U864,L749,D681,R255,U306,R154,U706,L817,D798,R109,D594,R496,D867,L217,D572,L166,U723,R66,D210,R732,D741,L21,D574,L523,D646,R313,D961,L474,U990,R125,U928,L58,U726,R200,D364,R244,U622,R823,U39,R918,U549,R667,U935,R372,U241,L56,D713,L735,U735,L812,U700,L408,U980,L242,D697,L580,D34,L266,U190,R876,U857,L967,U493,R871,U563,L241,D636,L467,D793,R304,U103,L950,D503,R487,D868,L358,D747,L338,D273,L485,D686,L974,D724,L534,U561,R729,D162,R731,D17,R305,U712,R472,D158,R921,U827,L944,D303,L526,D782,R575,U948,L401,D142,L48,U766,R799,D242,R821,U673,L120".split(",")
second = "L991,D492,L167,D678,L228,U504,R972,U506,R900,U349,R329,D802,R616,U321,R252,U615,R494,U577,R322,D593,R348,U140,L676,U908,L528,D247,L498,D79,L247,D432,L569,U206,L668,D269,L25,U180,R181,D268,R655,D346,R716,U240,L227,D239,L223,U760,L10,D92,L633,D425,R198,U222,L542,D790,L596,U667,L87,D324,R456,U366,R888,U319,R784,D948,R641,D433,L519,U950,L689,D601,L860,U233,R21,D214,L89,U756,L361,U258,L950,D483,R252,U206,L184,U574,L540,U926,R374,U315,R357,U512,R503,U917,R745,D809,L94,D209,R616,U47,R61,D993,L589,D1,R387,D731,R782,U771,L344,U21,L88,U614,R678,U259,L311,D503,L477,U829,R861,D46,R738,D138,L564,D279,L669,U328,L664,U720,L746,U638,R790,D242,R504,D404,R409,D753,L289,U128,L603,D696,L201,D638,L902,D279,L170,D336,L311,U683,L272,U396,R180,D8,R816,D904,L129,D809,R168,D655,L459,D545,L839,U910,L642,U704,R301,D235,R469,D556,L624,D669,L174,D272,R515,D60,L668,U550,L903,D881,L600,D734,R815,U585,R39,D87,R198,D418,L150,D964,L818,D250,L198,D127,R521,U478,L489,D676,L84,U973,R384,D167,R372,D981,L733,D682,R746,D803,L834,D421,R153,U752,L381,D990,R216,U469,L446,D763,R332,D813,L701,U872,L39,D524,L469,U508,L700,D382,L598,U563,R652,D901,R638,D358,L486,D735,L232,U345,R746,U818,L13,U618,R881,D647,R191,U652,R358,U423,L137,D224,R415,U82,R778,D403,R661,D157,R393,D954,L308,D986,L293,U870,R13,U666,L232,U144,R887,U364,L507,U520,R823,D11,L927,D904,R618,U875,R143,D457,R459,D755,R677,D561,L499,U267,L721,U274,L700,D870,L612,D673,L811,D695,R929,D84,L578,U201,L745,U963,L185,D687,L662,U313,L853,U314,R336".split(",")
# first = input().split(",")
# second = input().split(",")
to_search = [[-1158, -655], [-995, -655], [-995, -434], [-995, -253], [-991, -434], [-991, -253], [-991, -61], [-845, -61], [-688, -227], [-688, -224], [-669, -666], [-480, -666], [-414, -417], [-414, -253], [-4, -228], [154, -228], [154, -160], [213, 769], [213, 803], [227, 446], [227, 485], [227, 566], [227, 769], [227, 803], [278, 1577], [293, 436], [412, 592], [472, 183], [472, 436], [486, 0], [486, 183], [629, -173], [629, 0], [629, 183], [738, 183], [738, 436], [738, 592], [783, 597], [783, 804], [783, 1076], [815, -443], [815, -173], [815, 0], [815, 183], [842, 597], [842, 804], [857, -613], [896, 100], [896, 101], [896, 373], [961, 183], [1053, -613], [1060, 1133], [1060, 1666], [1104, 340], [1104, 373], [1138, 804], [1138, 1029], [1196, 705], [1318, -382], [1318, -356], [1431, -382], [1431, -356], [1539, -292], [1539, -144], [1643, 1210], [1683, 301], [1706, -577], [1888, 1355], [2122, 323], [2171, 448], [2171, 1025], [2177, 448], [2288, 900]]
step_hist = []
first_history = []
second_history = []
loc = [0, 0]
x = 0
y = 1
steps = 0
for i in range(len(first)):
    if first[i][0] == "R":
        for i in range(int(first[i][1:])):
            loc[x] += 1
            first_history.append([loc[x], loc[y]])
    elif first[i][0] == "L":
        for i in range(int(first[i][1:])):
            loc[x] -= 1
            first_history.append([loc[x], loc[y]])
    elif first[i][0] == "U":
        for i in range(int(first[i][1:])):
            loc[y] += 1
            first_history.append([loc[x], loc[y]])
    else:
        for i in range(int(first[i][1:])):
            loc[y] -= 1
            first_history.append([loc[x], loc[y]])
loc = [0, 0]

for i in range(len(second)):
    if second[i][0] == "R":
        for i in range(int(second[i][1:])):
            loc[x] += 1
            second_history.append([loc[x], loc[y]])
    elif second[i][0] == "L":
        for i in range(int(second[i][1:])):
            loc[x] -= 1
            second_history.append([loc[x], loc[y]])
    elif second[i][0] == "U":
        for i in range(int(second[i][1:])):
            loc[y] += 1
            second_history.append([loc[x], loc[y]])
    else:
        for i in range(int(second[i][1:])):
            loc[y] -= 1
            second_history.append([loc[x], loc[y]])

print(len(first_history))
print(len(second_history))
intersections = []
to_search = intersections
for i in range(len(first_history)):
    if first_history[i] in second_history:
        intersections.append(first_history[i])
        print(first_history[i])
intersections.sort()
print(intersections)

for i in range(len(to_search)):
    indexfirst = first_history.index(to_search[i])
    indexsecond = second_history.index(to_search[i])
    step_hist.append(indexfirst + indexsecond + 2)
print(step_hist)
step_hist.sort()
print(step_hist)
"""
Part 2:
[486, 0] = first intersection point
use step count, increment by 1 in all for loops, iterate through all of the intersection points, sort list
"""