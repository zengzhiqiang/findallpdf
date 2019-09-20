import os

path = r'F:\曾志强\实验报告\已完成\报告'

file_names = os.walk(path)

with open(r'F:\曾志强\实验报告\已完成\报告数据.txt', 'w') as f:
    for parent, dir, files in file_names:
        for file in files:
            file_dir = file[0:4] + '//' + file[5:7] + '//' + file
            print(file + ', ' + file_dir)
            s = file[0:11] + ', ' + file_dir
            f.write(s + '\n')
