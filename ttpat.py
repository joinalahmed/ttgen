import itertools
import re
from setuptools.package_index import unique_everseen


def checker(liter):
    check_list = list()
    for im in range(len(liter)):
        af = str(liter[im])
        mid_list = af
        for xx in range(len(mid_list)):
            for ro in range(len(mid_list)):
                if mid_list[ro] == mid_list[xx]:
                    continue
                else:
                    alp = str(xx + 1) + str(ro + 1)
                    check_list.append(alp)
            check_list = list(unique_everseen(check_list))
            check_list.sort()
    return check_list


# Compliments The Input Test-Pattern

def compliment_stuck(item):
    d = list()
    for k in range(len(item)):
        copy = list(item[k])
        for l in range(len(copy)):
            if copy[l] == str(1):
                copy[l] = str(0)
                continue
            if copy[l] == str(0):
                copy[l] = str(1)
        copy = ''.join(copy)
        d.append(copy)
    d = ''.join(d)
    return d


# Embeds alternating 1's and 0's

def main_fun(append_list):
    mid_list1 = list()
    for ins in range(len(append_list)):
        appended = str(append_list[ins])
        add0 = appended + '0'
        add1 = appended + '1'
        mid_list1.append(add0)
        mid_list1.append(add1)
    return list(unique_everseen(mid_list1))


def lines_count():
    with open('/home/joy/Desktop/test/rev.tfc', 'r') as datafile:
        # print dis
        for line in datafile:
            line1 = line.strip()
            if '.v' in line1:
                aa = line1
                bb = aa
                bb = bb[3:]
                cc = re.split(',', bb)
                asd = len(cc)
                break
        return asd


def mini(test_patterns):
    #print test_patterns
    test_pattern = list()

    for l in range(len(test_patterns)):
        test_pattern.append(str(test_patterns[l]))

    test_set = []
    permutations = list()
    # Generate possible Faults
    line_num = lines_count()
    for lines in range(1, line_num + 1):
        permutations.append(lines)

    permutations = list(itertools.permutations(permutations, 2))
    for i in range(len(permutations)):
        var1 = str(permutations[i][0])
        for j in range(1, len(permutations[i])):
            var1 += str(permutations[i][j])
        permutations[i] = var1
    permutations = list(unique_everseen(permutations))
    permutations.sort()
    combs = []
    # Generate Sets from Test-Pattern
    for length_pattern in range(len(test_pattern)):
        for combination in range(length_pattern, len(test_pattern) + 1):
            pattern = [list(x) for x in itertools.combinations(test_pattern, combination)]
            combs.extend(pattern)
    # Check Faults Covered By Sets of Test-Pattern
    for combinations in range(len(combs)):
        test_result = checker(combs[combinations])
        test_result.sort()
        if str(test_result) == str(permutations):
            #print test_result

            # If all Faults are covered, Print The Test Set
            test_set = combs[combinations]
            break
    #print test_set
    return test_set


def start(test_patterns):
    cts = list()
    for i in range(len(test_patterns)):
        cts.append(mini(test_patterns[i]))
    return cts
