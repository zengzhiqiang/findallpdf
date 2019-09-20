import os
import re

path = r'I:\检测中心试验报告总备份'

file_names = os.walk(path)

alldirs = []
with open(r'I:\检测中心试验报告总备份\已有报告.txt', 'w') as f:
    for parents, dirs, files in file_names:
        for dir in dirs:
            if re.search(r'20\d\d[-]\d\d[-]\d\d\d', dir):
                s = dir
                alldirs.append(s)
                f.write(s + '\n')

sum = 0
i = 1
reportnames = []
with open(r'I:\检测中心试验报告总备份\缺失的报告.txt', 'w') as fw:

    for alldir in alldirs:
        if sum != int(alldir[5:7]):
            if int(alldir[8:11]) != 1:
                s = alldir[0:8] + str(1).zfill(3)
                fw.write(s + '\n')
                reportnames.append(s)
            sum = int(alldir[5:7])
            i = 1
        if int(alldir[8:11]) == i:
            pass
        elif int(alldir[8:11]) - i == 1:
            i = int(alldir[8:11])
        elif int(alldir[8:11]) - i >= 2:
            for j in range(i + 1, int(alldir[8:11])):
                s = alldir[0:8] + str(j).zfill(3)
                fw.write(s + '\n')
                i = int(alldir[8:11])
                reportnames.append(s)
        reportnames.append(alldir)

with open(r'I:\检测中心试验报告总备份\所有编号.txt', 'w') as fe:
    for reportname in reportnames:
        fe.write(reportname + '\n')