# coding=utf-8
import os
import re
from collections import Counter


def scan_case_name():
    # len_case = {0: [], 1: []}
    case_attr = []
    list_case_id = {}
    rootdir = r"./src/testcase"  # 指明被遍历的文件夹
    if os.path.exists(r"./config/") is False:
        os.makedirs(r"./config/")

    scan_paths = map(lambda x: os.path.join(rootdir, x, "case"),
                     [i for i in os.listdir(rootdir) if "_" in i and "__init__" not in i])

    with open(u"./config/自动化测试用例对照表.yaml", "w") as cast_title:
        cast_title.write(u"#自动化测试用例对照表:\n".encode("utf-8"))
        cast_title.write("case_table:\n")
        for scan_path in scan_paths:
            case_attr.append([])
            for parent, dirnames, filenames in os.walk(scan_path):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
                for filename in (i for i in filenames if "pyc" not in i and "__init__" not in i
                                                         and "input_case" not in os.path.join(parent, i)):
                    with open(os.path.join(parent, filename), "r") as files:
                        file = files.read()
                        case_module = re.findall(r'self.case_module = u"(.+)"', file)[0]
                        case_name = re.findall(r"self.case_title = u'(.+)'", file)[0]
                        zentao_id = re.findall(r'self.zentao_id = (\d+)', file)[0]
                        case_id = re.findall(r"class (.+)\(", file)[0]
                        list_case_id[filename] = case_id
                        case_attr[scan_paths.index(scan_path)].append(
                            [zentao_id, case_module, case_id, case_name,
                             os.path.join(parent, filename).replace("\\", "/")])
                        # len_case[0].append(len(case_module))
                        # len_case[1].append(len(case_id))
            # len_case_module = tuple(len_case[0])
            # len_case_id = tuple(len_case[1])
            # max_case_module = max(len_case_module)
            # max_case_len = max(len_case_id)
        repetition = Counter(list_case_id.values())  # 计算list内部参数个数
        scan_paths = map(lambda x: x.split("\\")[-2], scan_paths)
        if len(set(repetition.values())) == 1:
            for x in case_attr:
                cast_title.write('''  %s:\n''' % scan_paths[case_attr.index(x)])
                for i in x:
                    # module_zen = max_case_module - len(i[0]) - 1 * (max_case_module - len(i[0])) / 3
                    # case_zen = max_case_len - len(i[2])
                    cast_title.write('''    %s:\n''' % i[0])
                    cast_title.write('''      'CASE_MODULE': ['%s']\n''' % i[1])
                    cast_title.write('''      'CODE_ID': ['%s']\n''' % i[2])
                    cast_title.write('''      'CASE_NAME': ['%s']\n''' % i[3])
                    cast_title.write('''      'CODE_PATH': ['%s']\n''' % i[4])
        else:
            tmp = ""
            dump = ""
            for k, v in repetition.items():
                if v != 1:
                    tmp = k
            for k, v in list_case_id.items():
                if v == tmp:
                    dump = dump + "%s:%s," % (k, v)
            raise ValueError(u"%s重复" % dump[:-1])
    print(u"《自动化测试用例对照表.log》创建完成")
