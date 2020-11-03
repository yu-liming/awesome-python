# https://www.jianshu.com/p/505fd455ba43

# getopt
# 说明
# 1. arg1: sys.argv[1:], fixed
# 2. arg2: 固定短参数类型, Unix getopt格式: 'x:'
# 3. args: 固定长参数类型, 默认'[]', 格式: 'xxx=', 当类型首字母唯一可缩写, 即'--x'='--xxx'

# import sys
# import getopt
# print(sys.argv[0])
# try:
#     opts, args = getopt.getopt(sys.argv[1:], 'l:t:', ['list=', 'len=', 'target=', 'help='])
#     print(opts)
#     print(args)
# except getopt.GetoptError:
#     print('usage: ')
#     getopt.error


# argparse
# https://blog.csdn.net/mou_it/article/details/81782386
# 官网： https://docs.python.org/3.8/library/argparse.html
# TODO 获取命令行参数个数
import argparse
parser = argparse.ArgumentParser(
    description='mock-app testting'
)

# 有选项时才填Default生效，无选项时不生效

parser.add_argument('-l', '--list', dest='AAA', metavar='test', nargs='+', type=str, help='列出所有可执行功能')
# parser.add_argument('list', nargs='+', type=str, help='列出所有可执行功能')

parser.add_argument('-a', '--all', dest='all', help='一次执行所有功能')

args = parser.parse_args()

print(args)
print(args.list)


# fire
# import fire