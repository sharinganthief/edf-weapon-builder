import filecmp
import json
import py_linq

import helpers
import main
import shutil
import os
import math

import sys

def testWeapons(**kwargs):
    sgoDir = kwargs['sgoDir']
    if sgoDir is None or not os.path.isdir(sgoDir):
        return

    # values = []
    main_window = main.init(False)
    for file in os.listdir(sgoDir):
        if file.startswith('AI'):
            continue
        if file.endswith('.SGO'):
            filePath = os.path.join(sgoDir, file)
            bak_sgo = filePath + '.bak'
            if os.path.exists(bak_sgo):
                # processed, skip cor now
                continue
            shutil.copy(filePath, bak_sgo)
            main_window.reset_weapon_data()
            main_window.loadWeaponFromJsonFile(filePath)
            main_window.writeWeaponToJsonFile(filePath, False)
            # same = open(filePath, "rb").read() == open(bak_sgo, "rb").read()
            same = filecmp.cmp(filePath + '.base.json', filePath + '.new.json', shallow=False)
            if not same:
                print(filePath)
                raise ValueError(filePath)

if __name__ == '__main__':
    testWeapons(**dict(arg.split('=') for arg in sys.argv[1:]))

# unique_data = [list(x) for x in set(tuple(x) for x in values)]
#
# for value in unique_data:
#     radius = 1
#     # X = radius * math.sin(theta) * math.cos(phi);
#     # y = radius * math.cos(theta) * math.sin(phi);
#
#     X = radius * math.sin(theta) * math.cos(phi)
#     y = radius * math.cos(theta) * math.sin(phi)
#
#     print(value + ' - %d & %d'.format(h, v))

# with open(filePath, encoding='utf-8') as fh:
#     data = json.load(fh)
#     FireVector = main.get_variable(data['variables'], 'FireVector')
#     if FireVector is not None:
#         FireVectorVal = FireVector['value']
#         if FireVectorVal is not None:
#             vector = [FireVectorVal[0]['value'], FireVectorVal[1]['value'], FireVectorVal[2]['value']]
#             values.append(vector)