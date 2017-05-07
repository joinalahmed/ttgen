import re

# GLOBAL VARIABLES AND FILES
temp_var = open('../../Desktop/test/converted.real', 'w')
temp_var.close()
cora = open('../../Desktop/test/converted_image.real', 'w')
cora.close()
state_list = []
state_list_temp = []
list_1 = []

# QUANTUM CONVERSION FUNCTIONS


def t_general(temp_gate, venus, iter_counter):
    alpha_centuri = re.split(' ', temp_gate)
    alpha_centuri = re.split(',', str(alpha_centuri[-1]))
    alpha_centuri_temp = re.split('\n', str(alpha_centuri[-1]))
    alpha_centuri[-1] = alpha_centuri_temp[0]
    with open('../../Desktop/test/converted.real', 'a') as lake:
        tora = open('../../Desktop/test/converted_image.real', 'a')
        lake.write('\n' + '# LEVEL UNDER CONVERSION- ' + str(iter_counter) + ', START' + '\n')

        # STAGE - 1
        lake.write('v ' + str(alpha_centuri[0]) + '\n')
        tora.write('v ' + str(alpha_centuri[0]) + '\n')

        # STAGE - 2
        proxima_centuri = alpha_centuri[:-1]
        var1 = 1
        canatrus_centuri = []
        for i in range(len(proxima_centuri)):
            canatrus = proxima_centuri[i] + proxima_centuri[var1]
            canatrus_centuri.append(canatrus)
            var1 += 1
            if var1 == len(proxima_centuri):
                break
        for emo in range(len(canatrus_centuri)):
            gi_joe = canatrus_centuri[emo]
            lake.write('v ' + gi_joe[0] + ' ' + gi_joe[1] + '\n')
            tora.write('v ' + gi_joe[0] + ' ' + gi_joe[1] + '\n')

        # STAGE - 3
        lake.write(str(venus) + str(2) + ' ' + alpha_centuri[-2] + ' ' + alpha_centuri[-1] + '\n')
        tora.write(str(venus) + str(2) + ' ' + alpha_centuri[-2] + ' ' + alpha_centuri[-1] + '\n')

        # STAGE - 4
        canatrus_centuri.reverse()
        for cario in range(len(canatrus_centuri)):
            amigo = canatrus_centuri[cario]
            lake.write('v+ ' + amigo[0] + ' ' + amigo[1] + '\n')
            tora.write('v+ ' + amigo[0] + ' ' + amigo[1] + '\n')

        # STAGE - 5
        lake.write('v+ ' + alpha_centuri[0] + '\n')
        tora.write('v+ ' + alpha_centuri[0] + '\n')

        lake.write(''
                   '# END' + '\n')
        tora.close()

with open('../../Desktop/test/a.tfc', 'r+') as file_alpha:
    for line in file_alpha:
        if '.v' in line:
            list_1 = str(line)
            list_1 = re.split(' ', list_1)
            # del list_1[0]
            list_1 = str(list_1)
            list_1 = re.split(',', list_1)
            list_1_12 = []
            list_1_1 = list_1[0]
            for ii in range(len(list_1_1)):
                list_1_12.append(list_1_1[ii])
            list_1[0] = list_1_12[-1]
            list_1_123 = []
            list_1_1_1 = list_1[-1]
            for ii in range(len(list_1_1_1)):
                list_1_123.append(list_1_1_1[ii])
            list_1[-1] = list_1_123[0]
        if line.strip() == 'BEGIN':
            break

    for line in file_alpha:
        if line.strip() == 'END':
            break
        if '#' in line:
            continue
        state_list.append(line)

with open('../../Desktop/test/converted.real', 'a') as cosmos:
    if "'" in list_1:
        mon = list_1.index("'")
        del list_1[mon]
        # print('list_1 :', list_1)
    for io in range(len(list_1)):
        myu = str(list_1[io])
        if "'" in myu:
            myu_1 = re.split("'", myu)
            list_1[io] = myu_1[-1]
    grape = open('../../Desktop/test/converted_image.real', 'a')
    cosmos.write('.version 1.0' + '\n')
    grape.write('.version 1.0' + '\n')
    cosmos.write('.numvars ' + str(len(list_1)) + '\n')
    grape.write('.numvars ' + str(len(list_1)) + '\n')
    cosmos.write('.variables ')
    grape.write('.variables ')
    for ii in range(len(list_1)):
        cosmos.write(str(list_1[ii]) + ' ')
        grape.write(str(list_1[ii]) + ' ')
    cosmos.write('\n')
    grape.write('\n')
    cosmos.write('.inputs ')
    grape.write('.inputs ')
    for ii in range(len(list_1)):
        cosmos.write(str(list_1[ii]) + ' ')
        grape.write(str(list_1[ii]) + ' ')
    cosmos.write('\n')
    grape.write('\n')
    cosmos.write('.outputs ')
    grape.write('.outputs ')
    for ii in range(len(list_1)):
        cosmos.write(str(list_1[ii]) + ' ')
        grape.write(str(list_1[ii]) + ' ')
    cosmos.write('\n')
    grape.write('\n')
    cosmos.write('.begin' + '\n')
    grape.write('.begin' + '\n')
    grape.close()


for ii in range(len(state_list)):
    if state_list[0] == '\n':
        continue
    state_list_temp = str(state_list[ii])
    state_list_temp = re.split(' ', state_list_temp)
    state_list_temp = state_list_temp[0]
    captain = re.compile("([a-zA-Z]+)([0-9]+)")
    captain_aplha = captain.match(state_list_temp)
    captain_beta = captain_aplha.group(1)
    captain_gamma = int(captain_aplha.group(2))
    cosmos_1 = open('../../Desktop/test/converted.real', 'a')
    cosmos_2 = open('../../Desktop/test/converted_image.real', 'a')
    if captain_beta is 't' or 'T':
        if captain_gamma is 1:
            cosmos_1.write(str(state_list[ii]))
            cosmos_2.write(str(state_list[ii]))

    if captain_beta is 't' or 'T':
        if captain_gamma is 2:
            jam = state_list[ii]
            jam = re.split(',', jam)
            jam_x = str(jam[0])
            jam_x = re.split(' ', jam_x)
            jam_y = str(jam[-1])
            jam_y = re.split('\n', jam_y)
            jam_x.append(jam_y[0])
            jam_x.insert(1, ' ')
            jam_x.insert(3, ' ')
            for iii in range(len(jam_x)):
                cosmos_1.write(jam_x[iii])
                cosmos_2.write(jam_x[iii])
            cosmos_1.write('\n')
            cosmos_2.write('\n')
    cosmos_1.close()
    cosmos_2.close()

    if captain_beta is 't' or 'T':
        if captain_gamma > 2:
            t_general(str(state_list[ii]), str(captain_beta), ii)

with open('../../Desktop/test/converted.real', 'a') as neptune:
    neptune.write('.end')

with open('../../Desktop/test/converted_image.real', 'a') as neptune:
    neptune.write('.end')
