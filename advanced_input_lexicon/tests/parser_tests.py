#tests for parser

from nose.tools import *
from ex48 import parser

def test_basic():
	obj=parser.parse_sentence([('verb', 'run'), ('direction', 'north')])
	assert_equal(obj.subject,'player')
	assert_equal(obj.verb,'run')
	assert_equal(obj.object,'north')

def test_advanced():
	obj=parser.parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')])
	assert_equal(obj.subject,'bear')
	assert_equal(obj.verb,'eat')
	assert_equal(obj.object,'honey')

def test_exception():
	assert_raises(parser.ParserError, parser.parse_sentence, ([('noun', 'bear')]))