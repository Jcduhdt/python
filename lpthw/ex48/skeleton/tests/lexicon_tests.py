'''
开始的时候很多错误，scan打成了sacn
还有就是识别数字哪里，我要匹配的数字加了引号，导致匹配失败
'''
from nose.tools import *
from ex48 import lexicon

def test_directions():
    # assert_equal 是在nose.tools导入的 似乎不匹配就会报错吧
    # 就是之前没写def stop函数 就会显示字段不匹配
    assert_equal(lexicon.scan('north'),[('direction','north')])
    result = lexicon.scan('north south east')
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east')])

def test_verbs():
    assert_equal(lexicon.scan('go'),[('verb','go')])
    result = lexicon.scan('go kill eat')
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb', 'eat')])

def test_stops():
    assert_equal(lexicon.scan('the'),[('stop','the')])
    result = lexicon.scan('the in of')
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'of')])

def test_nouns():
    assert_equal(lexicon.scan('bear'),[('noun','bear')])
    result = lexicon.scan('bear princess')
    assert_equal(result, [('noun', 'bear'),
                          ('noun', 'princess')])

def test_numbers():
    assert_equal(lexicon.scan('1234'),[('number',1234)])
    result = lexicon.scan('3 91234')
    assert_equal(result, [('number', 3),
                          ('number', 91234)])

def errors():
    assert_equal(lexicon.scan('ASDFADFASDF'),[('error','ASDFADFASDF')])
    result = lexicon.scan('bear IAS princess')
    assert_equal(result, [('noun', 'bear'),
                          ('error', 'IAS'),
                          ('noun', 'princess')])
