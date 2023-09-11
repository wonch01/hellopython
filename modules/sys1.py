import sys, os

# import mysys
# mysys.clear()

print("SSSSSSS>>", sys.path)
print("__file__ ==>", __file__)
print("dirname ==>", os.path.dirname(__file__))
print("abspath ==>", os.path.abspath(__file__))

dir_name = os.path.dirname(__file__)
a_path = os.path.abspath(dir_name)
print("a_path>>>", a_path)
up_dir = os.path.join(a_path, '..')
# base = os.path.abspath(up_dir)
# print("BASE CAMP>>>>>>>>>:", base)
# sys.path.append(base)
print("up_dir>>",up_dir)

# from mysys import clear
# clear()

print(sys.argv, len(sys.argv))

def print_sys_vars():
    for i in [sys.version, sys.copyright, sys.platform]:
        print("--->", i)

sa = sys.argv
if len(sa) < 2:
    # print_sys_vars()
    sys.exit()

with open(sa[1],'r',encoding='utf-8') as file:
    for line in file:
        print(line)
