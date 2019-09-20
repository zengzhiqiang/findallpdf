import os
import re
import os.path
import shutil

need_find_pdf_dir = r'J:\原材料（按类型分类）'

path_all = []
def find_path(path):
    dir_list = os.listdir(path)
    for dir in dir_list:
        sub_dir = os.path.join(path, dir)
        if os.path.isdir(sub_dir):
            find_path(sub_dir)
        else:
            path_all.append(sub_dir)

find_path(need_find_pdf_dir)
for file in path_all:
    if file[-4:] == '.xls' or file[-4:] == '.doc'or file[-5:] == '.docx' or file[-4:] == '.wps':
        if re.search(r'20\d\d[-]\d\d[-]\d\d\d', file):
            with open(file, 'r') as f:
                path2 = r'I:\报告2'
                reportname = re.search(r'20\d\d[-]\d\d[-]\d\d\d', file).group()
                path3 = reportname[0:4] + '\\' + reportname[5:7] + '\\' + reportname
                path4 = os.path.join(path2, path3)
                print(reportname)
                if os.path.exists(path4):
                    shutil.copy(file, path4)
                else:
                    os.makedirs(path4)
                    shutil.copy(file, path4)