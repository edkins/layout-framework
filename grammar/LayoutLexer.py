# Generated from Layout.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,9,69,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,
        2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,5,4,5,40,8,5,11,5,12,5,41,1,
        5,1,5,4,5,46,8,5,11,5,12,5,47,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,8,4,8,64,8,8,11,8,12,8,65,1,8,1,8,0,0,9,1,1,
        3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,1,0,5,1,0,48,57,1,0,120,120,
        1,0,35,35,2,0,48,57,97,102,3,0,9,10,13,13,32,32,71,0,1,1,0,0,0,0,
        3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,
        1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,1,19,1,0,0,0,3,26,1,0,0,0,5,28,
        1,0,0,0,7,30,1,0,0,0,9,35,1,0,0,0,11,39,1,0,0,0,13,49,1,0,0,0,15,
        54,1,0,0,0,17,63,1,0,0,0,19,20,5,119,0,0,20,21,5,105,0,0,21,22,5,
        110,0,0,22,23,5,100,0,0,23,24,5,111,0,0,24,25,5,119,0,0,25,2,1,0,
        0,0,26,27,5,123,0,0,27,4,1,0,0,0,28,29,5,125,0,0,29,6,1,0,0,0,30,
        31,5,103,0,0,31,32,5,114,0,0,32,33,5,105,0,0,33,34,5,100,0,0,34,
        8,1,0,0,0,35,36,5,45,0,0,36,37,5,45,0,0,37,10,1,0,0,0,38,40,7,0,
        0,0,39,38,1,0,0,0,40,41,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,43,
        1,0,0,0,43,45,7,1,0,0,44,46,7,0,0,0,45,44,1,0,0,0,46,47,1,0,0,0,
        47,45,1,0,0,0,47,48,1,0,0,0,48,12,1,0,0,0,49,50,7,2,0,0,50,51,7,
        3,0,0,51,52,7,3,0,0,52,53,7,3,0,0,53,14,1,0,0,0,54,55,7,2,0,0,55,
        56,7,3,0,0,56,57,7,3,0,0,57,58,7,3,0,0,58,59,7,3,0,0,59,60,7,3,0,
        0,60,61,7,3,0,0,61,16,1,0,0,0,62,64,7,4,0,0,63,62,1,0,0,0,64,65,
        1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,67,1,0,0,0,67,68,6,8,0,0,
        68,18,1,0,0,0,4,0,41,47,65,1,6,0,0
    ]

class LayoutLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    DIMS = 6
    COLOR3 = 7
    COLOR6 = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'window'", "'{'", "'}'", "'grid'", "'--'" ]

    symbolicNames = [ "<INVALID>",
            "DIMS", "COLOR3", "COLOR6", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "DIMS", "COLOR3", 
                  "COLOR6", "WS" ]

    grammarFileName = "Layout.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


