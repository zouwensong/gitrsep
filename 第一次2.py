###这个会报错，想到了用堆栈，但是用的不熟练，所以暂时没找到解决办法###
import re
stack=[]
# 读取目标文件，以列表形式返回，去除符号
# 输入文件的相对路径，输出去除所有符号并以换行符分割文件内容的列表
def read_text(path):# path为传入的c,cpp路径
    try:
        fp = open(path, 'r', encoding='utf-8')
        str_str = '~`!#$%^&*()_+-=|\';":/.,?><~·！@#￥%……&*（）——+-=“：’；、。，？》《{}'
        file_text = re.sub(r"[%s]+" % str_str, " ", fp.read()) # 通过正则化原文本内容，去除所有符号
        file_text = file_text.split('\n')   # 按换行符分割文本
        fp.close()
    except:
        print("文件打开错误")
    return file_text

# 将read_text处理的文件内容中空格删除，并进一步细化关键词
def split_text(file_text):
    key_list = []
    for text_line in file_text:
        text_word = text_line.split(' ')  #删除多余空格
        text_word = filter(None, text_word)   #放入一个新列表
        for str1 in text_word:
            if str1 != '':
                key_list.append(str1)    #将字符串放入列表
    return key_list

# 传入read_text()处理后返回的列表，返回以重要关键词组成的列表
def get_key_list(file_text):
    list_str = []
    for i in file_text:  # 提取文件中重要关键词
        if 'else if' in i:
            list_str.append('else if')
        elif 'if' in i:
            list_str.append('if')
        elif 'case' in i:
             list_str.append('case')
        elif 'else' in i:
            list_str.append('else')
        elif 'switch' in i:
            list_str.append('switch')
    return list_str

# 传入read_text()处理文件后返回的列表，返回关键词的个数
def key_word(key_list):
    key_word0= {'else if', 'char', 'double', 'enum', 'float', 'int', 'long',
                'short', 'signed', 'struct','void', 'for', 'do', 'while', 'break',
                'continue',  'union', 'unsigned', 'const', 'sizeof', 'typedef', 'volatile' ,
                'if', 'else', 'goto', 'switch', 'case', 'default', 'return', 'auto', 'extern',
                'register', 'static'
                }    #创建包含所有c++内置关键字的字典
    key_num= 0
    for word in key_list:
        if word in key_word0:
            key_num += 1
    return key_num   # 返回文件中C、CPP关键词的总数


#查找if-else和if-else-if结构
def count_ifelse(key_list):
    l=key_list
    flag=0
    if l[0] == 'i' and l[1] == 'f':#判断if
        stack.append(1)
    if l[0] == 'e' and l[4] == 'i':#判断elseif
        stack.append(3)
    elif l[0] == 'e' and l[1] == 'l':#判断else
        while (stack[-1] != 1):
            if (stack[-1] == 3):
                flag=1
            stack.pop()
        stack.pop()
        if flag == 0:
            count_ifelse+=1
        if flag ==1:
            count_ifelseif+=1




# 返回case数目为元素的列表
# 传入关键词组成的列表，输出每组switch内的case数目
def case_num(ed_key_list):# 文件中有switch才能统计case
    length = len(ed_key_list)
    if ed_key_list.count('switch'):#从索引0位置查找switch个数且找到就执行
        num_case = []
        for i in range(length):
            if ed_key_list[i] == 'switch':
                if (i + 1) == length or ed_key_list[i + 1] != 'case':  #switch是列表最后的元素或下一位置不是case
                    num_case.append(0)
                elif i < length - 1:  #switch是列表中间元素
                    flag = 1  #标记查找时步长
                    if ed_key_list[i + flag] == 'case': #下一位置为case
                        case_cnt = 0  #标记case个数
                        while i + flag < length: #在列表元素中查找，避免越界，系统报错
                            if ed_key_list[flag + i] == 'case':
                                case_cnt += 1
                                flag += 1
                            else:
                                break
                        num_case.append(case_cnt)
                    else:
                        num_case.append(0)
        return num_case
    else:
        return [0]

if __name__ == '__main__':
    print("text.cpp放在text.py同一目录下")
    path_level = input("请输入text.cpp 名称和等级")
    path_level_list = path_level.split(' ')   #删除多余空格，避免输入
    path = str(path_level_list[0])
    level = int(path_level_list[-1])
    if level > 4 or level < 1:
        print('等级输入错误！')
    file_text = read_text(path)
    key_list = split_text(file_text)
    if level == 1:
        print('total num: ', key_word(key_list))
    elif level == 2:
        print('total num: ', key_word(key_list))
        print('switch num: ', key_list.count('switch'))
        ed_key_list = get_key_list(key_list)
        print('case num: ', end='')
        print(*case_num(ed_key_list), sep=' ')
    elif level == 3:
        print('total num: ', key_word(key_list))
        print('switch num: ', key_list.count('switch'))
        ed_key_list = get_key_list(key_list)
        print('case num: ', end='')
        print(*case_num(ed_key_list), sep=' ')
        print('if-else num: ',count_ifelse)
    elif level == 4:
        print('total num: ', key_word(key_list))
        print('switch num: ', key_list.count('switch'))
        ed_key_list = get_key_list(key_list)
        print('case num: ', end='')
        print(*case_num(ed_key_list), sep=' ')
        print('if-else num: ',count_ifelse)
        print('if-elseif-else num: ',count_ifelself)














