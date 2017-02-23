## Parser tests
from nose.tools import *
from ex48 import parser

def test_subject():
    x = parser.parse_sentence([('verb','run'), ('direction','north')])
    assert_equal(x.subject, 'player')
    result = parser.parse_sentence([('noun', 'Tim'), ('verb', 'jogged'), ('direction', 'south')])
    assert_equal(result.subject, 'Tim')

def test_parser_verbs():
    x = parser.parse_sentence([('verb','run'), ('direction','north')])
    assert_equal(x.verb, 'run')
    result = parser.parse_sentence([('noun', 'Tim'), ('verb', 'jogged'), ('direction', 'south')])
    assert_equal(result.verb, 'jogged')

def test_parser_objects():
    x = parser.parse_sentence([('verb','run'), ('direction','north')])
    assert_equal(x.object, 'north')
    result = parser.parse_sentence([('noun', 'Tim'), ('verb', 'jogged'), ('direction', 'south')])
    assert_equal(result.object, 'south')

def test_parser_errors():
    assert_raises(parser.ParserError, parser.parse_sentence, ('number', '3'))
