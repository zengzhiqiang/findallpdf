import os
import re
import os.path
import shutil


def find_path(path, path_all=[]):
    dir_list = os.listdir(path)
    for dir in dir_list:
        sub_dir = os.path.join(path, dir)
        if os.path.isdir(sub_dir):
            find_path(sub_dir, path_all)
        else:
            path_all.append(sub_dir)
    return path_all


def move_report(path_all, path_to, suffixs):

    if suffixs == [""]:
        suffixs = ['.xls', '.doc', '.docx', '.wps']
    for file in path_all:
        is_report = False
        for suffix in suffixs:
            if suffix in file[-10:]:
                is_report = True
        if is_report:
            if re.search(r'20\d\d[-]\d\d[-]\d\d\d', file):
                with open(file, 'r') as f:
                    reportname = re.search(r'20\d\d[-]\d\d[-]\d\d\d', file).group()
                    path3 = reportname[0:4] + '\\' + reportname[5:7] + '\\' + reportname
                    path4 = os.path.join(path_to, path3)
                    print("正在移动：" + file)
                    if os.path.exists(path4):
                        # try:
                        #     shutil.copy(file, path4)
                        # except shutil.SameFileError as err:
                        #     print(err)
                        shutil.copy(file, path4)
                    else:
                        os.makedirs(path4)
                        shutil.copy(file, path4)

if __name__ == "__main__":

    # need_find_pdf_dir = r'C:\工作\曾志强\实验报告'
    # path_all_ = find_path(need_find_pdf_dir)
    # path_to_ = r'C:\工作\曾志强\实验报告\整理'
    # move_report(path_all_, path_to_)

    print("版权所有：@浙江金固股份有限公司 @检测中心 @曾志强\n")
    print("欢迎使用报告整理工具！\n")
    print("注意！待整理的报告文件夹和整理后报告存放的文件夹必须是不同文件夹，且待整理报告文件夹不是整理后报告存放文件夹的父文件夹。否者将引起严重错误，导致程序奔溃甚至报告文件损坏！")
    print("------------------------我是分割线------------------------------")
    print("\n")
    unorganized_report_path = input("请输入未整理的报告所在文件夹，按回车键结束输入：")
    organized_report_path = input("请输入已整理的报告所在文件夹，按回车键结束输入：")
    while unorganized_report_path in organized_report_path:
        print("已整理的报告所在文件夹是未整理的报告所在文件夹的子文件夹，无法进行整理，请重新输入已整理的报告所在文件夹！")
        organized_report_path = input("请输入已整理的报告所在文件夹，按回车键结束输入：")
    report_suffixs = input("\n请输入报告中标题中含有的文字信息（比如 '.pdf' 就是将所有报告名中含有 '.pdf' 的报告整理，默认状态下只"
                           "整理以'.xls', '.doc', '.docx', '.wps'结尾的文件），输入多个条件请以空格隔开：").split(" ")
    print("\n开始整理！。。。。\n")
    path_all_ = find_path(unorganized_report_path)
    move_report(path_all_, organized_report_path, report_suffixs)
    input("\n整理完成！按回车退出程序")
