# Generated from Layout.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,116,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,3,1,39,8,1,1,2,1,2,1,2,
        1,2,5,2,45,8,2,10,2,12,2,48,9,2,1,2,1,2,1,3,1,3,1,3,5,3,55,8,3,10,
        3,12,3,58,9,3,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,7,5,7,71,
        8,7,10,7,12,7,74,9,7,1,7,1,7,1,8,1,8,3,8,80,8,8,1,9,1,9,1,9,5,9,
        85,8,9,10,9,12,9,88,9,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,11,1,11,1,12,1,12,1,12,5,12,104,8,12,10,12,12,12,107,9,12,1,
        12,1,12,1,13,1,13,1,14,1,14,1,14,1,14,0,0,15,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,0,1,1,0,12,13,109,0,30,1,0,0,0,2,38,1,0,0,0,
        4,40,1,0,0,0,6,51,1,0,0,0,8,61,1,0,0,0,10,63,1,0,0,0,12,65,1,0,0,
        0,14,67,1,0,0,0,16,79,1,0,0,0,18,81,1,0,0,0,20,91,1,0,0,0,22,98,
        1,0,0,0,24,100,1,0,0,0,26,110,1,0,0,0,28,112,1,0,0,0,30,31,5,1,0,
        0,31,32,5,2,0,0,32,33,3,2,1,0,33,34,5,3,0,0,34,1,1,0,0,0,35,39,3,
        4,2,0,36,39,3,10,5,0,37,39,3,14,7,0,38,35,1,0,0,0,38,36,1,0,0,0,
        38,37,1,0,0,0,39,3,1,0,0,0,40,41,5,4,0,0,41,46,5,2,0,0,42,45,3,6,
        3,0,43,45,3,8,4,0,44,42,1,0,0,0,44,43,1,0,0,0,45,48,1,0,0,0,46,44,
        1,0,0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,46,1,0,0,0,49,50,5,3,0,0,
        50,5,1,0,0,0,51,52,3,12,6,0,52,56,5,2,0,0,53,55,3,2,1,0,54,53,1,
        0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,59,1,0,0,0,58,
        56,1,0,0,0,59,60,5,3,0,0,60,7,1,0,0,0,61,62,5,5,0,0,62,9,1,0,0,0,
        63,64,7,0,0,0,64,11,1,0,0,0,65,66,5,10,0,0,66,13,1,0,0,0,67,68,5,
        6,0,0,68,72,5,2,0,0,69,71,3,16,8,0,70,69,1,0,0,0,71,74,1,0,0,0,72,
        70,1,0,0,0,72,73,1,0,0,0,73,75,1,0,0,0,74,72,1,0,0,0,75,76,5,3,0,
        0,76,15,1,0,0,0,77,80,3,18,9,0,78,80,3,24,12,0,79,77,1,0,0,0,79,
        78,1,0,0,0,80,17,1,0,0,0,81,82,5,7,0,0,82,86,5,2,0,0,83,85,3,20,
        10,0,84,83,1,0,0,0,85,88,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,
        89,1,0,0,0,88,86,1,0,0,0,89,90,5,3,0,0,90,19,1,0,0,0,91,92,3,22,
        11,0,92,93,3,22,11,0,93,94,3,12,6,0,94,95,5,2,0,0,95,96,3,2,1,0,
        96,97,5,3,0,0,97,21,1,0,0,0,98,99,5,11,0,0,99,23,1,0,0,0,100,101,
        5,8,0,0,101,105,5,2,0,0,102,104,3,26,13,0,103,102,1,0,0,0,104,107,
        1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,108,1,0,0,0,107,105,
        1,0,0,0,108,109,5,3,0,0,109,25,1,0,0,0,110,111,3,28,14,0,111,27,
        1,0,0,0,112,113,5,9,0,0,113,114,3,22,11,0,114,29,1,0,0,0,8,38,44,
        46,56,72,79,86,105
    ]

class LayoutParser ( Parser ):

    grammarFileName = "Layout.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'viewport'", "'{'", "'}'", "'grid'", 
                     "'--'", "'scroll'", "'bounds'", "'column'", "'lorem'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "DIMS", "NUM", "COLOR3", 
                      "COLOR6", "WS" ]

    RULE_viewport = 0
    RULE_filler = 1
    RULE_grid = 2
    RULE_cell = 3
    RULE_separator = 4
    RULE_color = 5
    RULE_dims = 6
    RULE_scroll = 7
    RULE_big = 8
    RULE_bounds = 9
    RULE_bound = 10
    RULE_num = 11
    RULE_column = 12
    RULE_paragraph = 13
    RULE_lorem = 14

    ruleNames =  [ "viewport", "filler", "grid", "cell", "separator", "color", 
                   "dims", "scroll", "big", "bounds", "bound", "num", "column", 
                   "paragraph", "lorem" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    DIMS=10
    NUM=11
    COLOR3=12
    COLOR6=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ViewportContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def filler(self):
            return self.getTypedRuleContext(LayoutParser.FillerContext,0)


        def getRuleIndex(self):
            return LayoutParser.RULE_viewport

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterViewport" ):
                listener.enterViewport(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitViewport" ):
                listener.exitViewport(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitViewport" ):
                return visitor.visitViewport(self)
            else:
                return visitor.visitChildren(self)




    def viewport(self):

        localctx = LayoutParser.ViewportContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_viewport)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(LayoutParser.T__0)
            self.state = 31
            self.match(LayoutParser.T__1)
            self.state = 32
            self.filler()
            self.state = 33
            self.match(LayoutParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FillerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def grid(self):
            return self.getTypedRuleContext(LayoutParser.GridContext,0)


        def color(self):
            return self.getTypedRuleContext(LayoutParser.ColorContext,0)


        def scroll(self):
            return self.getTypedRuleContext(LayoutParser.ScrollContext,0)


        def getRuleIndex(self):
            return LayoutParser.RULE_filler

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFiller" ):
                listener.enterFiller(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFiller" ):
                listener.exitFiller(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFiller" ):
                return visitor.visitFiller(self)
            else:
                return visitor.visitChildren(self)




    def filler(self):

        localctx = LayoutParser.FillerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_filler)
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.grid()
                pass
            elif token in [12, 13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.color()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.scroll()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GridContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cell(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LayoutParser.CellContext)
            else:
                return self.getTypedRuleContext(LayoutParser.CellContext,i)


        def separator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LayoutParser.SeparatorContext)
            else:
                return self.getTypedRuleContext(LayoutParser.SeparatorContext,i)


        def getRuleIndex(self):
            return LayoutParser.RULE_grid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGrid" ):
                listener.enterGrid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGrid" ):
                listener.exitGrid(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrid" ):
                return visitor.visitGrid(self)
            else:
                return visitor.visitChildren(self)




    def grid(self):

        localctx = LayoutParser.GridContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_grid)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(LayoutParser.T__3)
            self.state = 41
            self.match(LayoutParser.T__1)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==10:
                self.state = 44
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [10]:
                    self.state = 42
                    self.cell()
                    pass
                elif token in [5]:
                    self.state = 43
                    self.separator()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self.match(LayoutParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CellContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dims(self):
            return self.getTypedRuleContext(LayoutParser.DimsContext,0)


        def filler(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LayoutParser.FillerContext)
            else:
                return self.getTypedRuleContext(LayoutParser.FillerContext,i)


        def getRuleIndex(self):
            return LayoutParser.RULE_cell

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCell" ):
                listener.enterCell(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCell" ):
                listener.exitCell(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCell" ):
                return visitor.visitCell(self)
            else:
                return visitor.visitChildren(self)




    def cell(self):

        localctx = LayoutParser.CellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_cell)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.dims()
            self.state = 52
            self.match(LayoutParser.T__1)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 12368) != 0:
                self.state = 53
                self.filler()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
            self.match(LayoutParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LayoutParser.RULE_separator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeparator" ):
                listener.enterSeparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeparator" ):
                listener.exitSeparator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeparator" ):
                return visitor.visitSeparator(self)
            else:
                return visitor.visitChildren(self)




    def separator(self):

        localctx = LayoutParser.SeparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_separator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(LayoutParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLOR3(self):
            return self.getToken(LayoutParser.COLOR3, 0)

        def COLOR6(self):
            return self.getToken(LayoutParser.COLOR6, 0)

        def getRuleIndex(self):
            return LayoutParser.RULE_color

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColor" ):
                listener.enterColor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColor" ):
                listener.exitColor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColor" ):
                return visitor.visitColor(self)
            else:
                return visitor.visitChildren(self)




    def color(self):

        localctx = LayoutParser.ColorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_color)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            _la = self._input.LA(1)
            if not(_la==12 or _la==13):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIMS(self):
            return self.getToken(LayoutParser.DIMS, 0)

        def getRuleIndex(self):
            return LayoutParser.RULE_dims

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDims" ):
                listener.enterDims(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDims" ):
                listener.exitDims(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDims" ):
                return visitor.visitDims(self)
            else:
                return visitor.visitChildren(self)




    def dims(self):

        localctx = LayoutParser.DimsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_dims)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(LayoutParser.DIMS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScrollContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def big(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LayoutParser.BigContext)
            else:
                return self.getTypedRuleContext(LayoutParser.BigContext,i)


        def getRuleIndex(self):
            return LayoutParser.RULE_scroll

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScroll" ):
                listener.enterScroll(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScroll" ):
                listener.exitScroll(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScroll" ):
                return visitor.visitScroll(self)
            else:
                return visitor.visitChildren(self)




    def scroll(self):

        localctx = LayoutParser.ScrollContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_scroll)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(LayoutParser.T__5)
            self.state = 68
            self.match(LayoutParser.T__1)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 69
                self.big()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 75
            self.match(LayoutParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BigContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bounds(self):
            return self.getTypedRuleContext(LayoutParser.BoundsContext,0)


        def column(self):
            return self.getTypedRuleContext(LayoutParser.ColumnContext,0)


        def getRuleIndex(self):
            return LayoutParser.RULE_big

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBig" ):
                listener.enterBig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBig" ):
                listener.exitBig(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBig" ):
                return visitor.visitBig(self)
            else:
                return visitor.visitChildren(self)




    def big(self):

        localctx = LayoutParser.BigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_big)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.bounds()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.column()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoundsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bound(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LayoutParser.BoundContext)
            else:
                return self.getTypedRuleContext(LayoutParser.BoundContext,i)


        def getRuleIndex(self):
            return LayoutParser.RULE_bounds

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBounds" ):
                listener.enterBounds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBounds" ):
                listener.exitBounds(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBounds" ):
                return visitor.visitBounds(self)
            else:
                return visitor.visitChildren(self)




    def bounds(self):

        localctx = LayoutParser.BoundsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_bounds)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(LayoutParser.T__6)
            self.state = 82
            self.match(LayoutParser.T__1)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 83
                self.bound()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self.match(LayoutParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoundContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LayoutParser.NumContext)
            else:
                return self.getTypedRuleContext(LayoutParser.NumContext,i)


        def dims(self):
            return self.getTypedRuleContext(LayoutParser.DimsContext,0)


        def filler(self):
            return self.getTypedRuleContext(LayoutParser.FillerContext,0)


        def getRuleIndex(self):
            return LayoutParser.RULE_bound

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBound" ):
                listener.enterBound(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBound" ):
                listener.exitBound(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBound" ):
                return visitor.visitBound(self)
            else:
                return visitor.visitChildren(self)




    def bound(self):

        localctx = LayoutParser.BoundContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_bound)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.num()
            self.state = 92
            self.num()
            self.state = 93
            self.dims()
            self.state = 94
            self.match(LayoutParser.T__1)
            self.state = 95
            self.filler()
            self.state = 96
            self.match(LayoutParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(LayoutParser.NUM, 0)

        def getRuleIndex(self):
            return LayoutParser.RULE_num

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum" ):
                listener.enterNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum" ):
                listener.exitNum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)




    def num(self):

        localctx = LayoutParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(LayoutParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paragraph(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LayoutParser.ParagraphContext)
            else:
                return self.getTypedRuleContext(LayoutParser.ParagraphContext,i)


        def getRuleIndex(self):
            return LayoutParser.RULE_column

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn" ):
                listener.enterColumn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn" ):
                listener.exitColumn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn" ):
                return visitor.visitColumn(self)
            else:
                return visitor.visitChildren(self)




    def column(self):

        localctx = LayoutParser.ColumnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_column)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(LayoutParser.T__7)
            self.state = 101
            self.match(LayoutParser.T__1)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 102
                self.paragraph()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
            self.match(LayoutParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParagraphContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lorem(self):
            return self.getTypedRuleContext(LayoutParser.LoremContext,0)


        def getRuleIndex(self):
            return LayoutParser.RULE_paragraph

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParagraph" ):
                listener.enterParagraph(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParagraph" ):
                listener.exitParagraph(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParagraph" ):
                return visitor.visitParagraph(self)
            else:
                return visitor.visitChildren(self)




    def paragraph(self):

        localctx = LayoutParser.ParagraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_paragraph)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.lorem()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoremContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num(self):
            return self.getTypedRuleContext(LayoutParser.NumContext,0)


        def getRuleIndex(self):
            return LayoutParser.RULE_lorem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLorem" ):
                listener.enterLorem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLorem" ):
                listener.exitLorem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLorem" ):
                return visitor.visitLorem(self)
            else:
                return visitor.visitChildren(self)




    def lorem(self):

        localctx = LayoutParser.LoremContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_lorem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(LayoutParser.T__8)
            self.state = 113
            self.num()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





