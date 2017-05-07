import re
import pyexcel as pe

gate_list = []
gate_list_temp = []
gate_sublist = []
main_li = []
sub_li = []
total = list()
def truth_push(input_result):
    levels.append(input_result[0])
    levels.append(input_result[1])
    levels.append(input_result[2])
    levels.append(input_result[3])

def getheader():
    header_t = ['Gate', 'Controls', 'Target', 'Gate Type']
    return header_t

che = getheader()
with open('../../Desktop/test/converted_image.real', 'r+') as file:
    for line in file:
        if line.strip() == '.begin':
            break
    for line in file:
        if line.strip() == '.end':
            break
        gate_list.append(line)

# print('gates', gate_list)
for i in range(len(gate_list)):
    gate_sublist = (gate_list[i])
    gate_sublist = re.split('\\s', gate_sublist)
    del gate_sublist[-1]
    gate_list_temp.append(gate_sublist)
    # print('gate_sublist', gate_sublist)

for ii in range(len(gate_list_temp)):
    levels = list()

    alpha = gate_list_temp[ii]
    # print('alpha', alpha)
    if len(alpha) == 2:
        d1 = alpha[0]
        if len(d1) == 1:
            if d1 == 'v':
                var1 = alpha
                level=ii+1
                control='NULL'
                target=var1[-1]
                gate_type='V'
                detail = [level, control, target, gate_type]
                truth_push(detail)
                total.append(levels)
        if len(d1) == 2:
            if d1[0] == 'v' and d1[1] == '+':
                var2 = alpha
                level = ii+1
                control = 'NULL'
                target = var2[-1]
                gate_type = 'V+'
                detail=[level,control,target,gate_type]
                truth_push(detail)
                total.append(levels)


    if len(alpha) == 3:
        d2 = alpha[0]
        if len(d2) == 1:
            if d2[0] == 'v':
                e1 = alpha
                level = ii+1
                control = e1[-2]
                target = e1[-1]
                gate_type = 'C-V'
                detail = [level, control, target, gate_type]
                truth_push(detail)
                total.append(levels)
        if len(d2) == 2:
            if d2[0] == 'v' and d2[1] == '+':
                e2 = alpha
                level = ii+1
                control = e2[-2]
                target = e2[-1]
                gate_type = 'C-V+'
                detail = [level, control, target, gate_type]
                truth_push(detail)
                total.append(levels)

            if (d2[0] == 't' and d2[1] == '1') or (d2[0] == 'T' and d2[1] == '1'):
                e3 = alpha
                level = ii+1
                control = 'NULL'
                target = e3[-2]
                gate_type = 'NOT'
                detail = [level, control, target, gate_type]
                truth_push(detail)
                total.append(levels)
    if len(alpha) == 4:
        d2=alpha
        if (d2[0] == 't2') or (d2[0] == 'T2'):
            e3 = alpha
            level = ii + 1
            control = d2[-3]
            target = d2[-2]
            gate_type = 'C-NOT'
            detail = [level, control, target, gate_type]
            truth_push(detail)
            total.append(levels)
total.insert(0, che)
sheet = pe.Sheet(total)
print sheet
sheet.save_as('../../Desktop/test/qc_details.csv')
