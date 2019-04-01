# cd lpthw
# python
# import ex25

# from ex25 import *  我要把ex25中的所有东西导入进来
def break_words(stuff):
    """This function will break up words for us."""
    # """  """中的内容为文档注释
    # 比如执行 help(ex25.break_words) 就会显示三个引号中的字符串
    words = stuff.split(' ')
    # .split(' ')  ''中有空格 意思是制定分隔符为空格
    return words
    # 返回列表
def sort_words(words):
    """Sorts the words."""
    return sorted(words)
    #按字母排序

def print_first_word(words):
    """Prints the first word after poping it off."""
    word = words.pop(0)
    #用于移除列表中的第一个元素，并且返回该元素的值
    print(word)

def print_last_word(words):
    """Prints the last words after poping it off."""
    word = words.pop(-1)
    #用于移除列表中的最后一个元素，并且返回该元素的值
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
