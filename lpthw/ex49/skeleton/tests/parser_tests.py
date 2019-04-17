from nose.tools import *
from ex49.parser import *

# 为什么skip不对，讲道理应该是跳过stop is 啊，但是会出现 parser、中的报错
def test_sentence():
    sentence = parse_sentence([('noun','bear'),('stop','is'),('verb','running'),('direction','east')])
    assert_equal(sentence.subject,'bear')
    assert_equal(sentence.verb,'running')
    assert_equal(sentence.object,'east')

def test_peek():
    peek1 = peek([('noun','bear'),('stop','is'),('verb','running'),('direction','east')])
    peek2 = peek([('verb','running')])
    peek3 = peek([])
    assert_equal(peek1,'noun')
    assert_equal(peek2,'verb')
    assert_equal(peek3,None)

def test_match():
    match1 = match([('noun','bear'),('stop','is'),('verb','running'),('direction','east')],'noun')
    #match2 = match([('noun','bear'),('stop','is'),('verb','running'),('direction','east')],'direction')
    assert_equal(match1,('noun','bear'))
    # assert_raises(match2,)

def test_parse_subject():
    #last_sentence = Sentence(('',''),('',''),('',''),('',''))
    last_sentence = parse_sentence([('verb','running'),('stop','is'),('direction','east'),('noun','bear')])
    assert_equal(last_sentence.object,'east')
