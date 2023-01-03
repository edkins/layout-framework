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
        4,1,12,93,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,0,1,
        0,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,5,2,39,8,2,10,2,12,2,42,
        9,2,1,2,1,2,1,3,1,3,1,3,5,3,49,8,3,10,3,12,3,52,9,3,1,3,1,3,1,4,
        1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,7,5,7,65,8,7,10,7,12,7,68,9,7,1,7,
        1,7,1,8,1,8,1,9,1,9,1,9,5,9,77,8,9,10,9,12,9,80,9,9,1,9,1,9,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,0,0,12,0,2,4,6,8,10,
        12,14,16,18,20,22,0,1,1,0,10,11,87,0,24,1,0,0,0,2,32,1,0,0,0,4,34,
        1,0,0,0,6,45,1,0,0,0,8,55,1,0,0,0,10,57,1,0,0,0,12,59,1,0,0,0,14,
        61,1,0,0,0,16,71,1,0,0,0,18,73,1,0,0,0,20,83,1,0,0,0,22,90,1,0,0,
        0,24,25,5,1,0,0,25,26,5,2,0,0,26,27,3,2,1,0,27,28,5,3,0,0,28,1,1,
        0,0,0,29,33,3,4,2,0,30,33,3,10,5,0,31,33,3,14,7,0,32,29,1,0,0,0,
        32,30,1,0,0,0,32,31,1,0,0,0,33,3,1,0,0,0,34,35,5,4,0,0,35,40,5,2,
        0,0,36,39,3,6,3,0,37,39,3,8,4,0,38,36,1,0,0,0,38,37,1,0,0,0,39,42,
        1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,43,1,0,0,0,42,40,1,0,0,0,
        43,44,5,3,0,0,44,5,1,0,0,0,45,46,3,12,6,0,46,50,5,2,0,0,47,49,3,
        2,1,0,48,47,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,
        53,1,0,0,0,52,50,1,0,0,0,53,54,5,3,0,0,54,7,1,0,0,0,55,56,5,5,0,
        0,56,9,1,0,0,0,57,58,7,0,0,0,58,11,1,0,0,0,59,60,5,8,0,0,60,13,1,
        0,0,0,61,62,5,6,0,0,62,66,5,2,0,0,63,65,3,16,8,0,64,63,1,0,0,0,65,
        68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,69,1,0,0,0,68,66,1,0,0,
        0,69,70,5,3,0,0,70,15,1,0,0,0,71,72,3,18,9,0,72,17,1,0,0,0,73,74,
        5,7,0,0,74,78,5,2,0,0,75,77,3,20,10,0,76,75,1,0,0,0,77,80,1,0,0,
        0,78,76,1,0,0,0,78,79,1,0,0,0,79,81,1,0,0,0,80,78,1,0,0,0,81,82,
        5,3,0,0,82,19,1,0,0,0,83,84,3,22,11,0,84,85,3,22,11,0,85,86,3,12,
        6,0,86,87,5,2,0,0,87,88,3,2,1,0,88,89,5,3,0,0,89,21,1,0,0,0,90,91,
        5,9,0,0,91,23,1,0,0,0,6,32,38,40,50,66,78
    ]

class LayoutParser ( Parser ):

    grammarFileName = "Layout.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'viewport'", "'{'", "'}'", "'grid'", 
                     "'--'", "'scroll'", "'bounds'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "DIMS", "NUM", "COLOR3", "COLOR6", "WS" ]

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

    ruleNames =  [ "viewport", "filler", "grid", "cell", "separator", "color", 
                   "dims", "scroll", "big", "bounds", "bound", "num" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    DIMS=8
    NUM=9
    COLOR3=10
    COLOR6=11
    WS=12

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
            self.state = 24
            self.match(LayoutParser.T__0)
            self.state = 25
            self.match(LayoutParser.T__1)
            self.state = 26
            self.filler()
            self.state = 27
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
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.grid()
                pass
            elif token in [10, 11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.color()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
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
            self.state = 34
            self.match(LayoutParser.T__3)
            self.state = 35
            self.match(LayoutParser.T__1)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==8:
                self.state = 38
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8]:
                    self.state = 36
                    self.cell()
                    pass
                elif token in [5]:
                    self.state = 37
                    self.separator()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 43
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
            self.state = 45
            self.dims()
            self.state = 46
            self.match(LayoutParser.T__1)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 3152) != 0:
                self.state = 47
                self.filler()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
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
            self.state = 55
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
            self.state = 57
            _la = self._input.LA(1)
            if not(_la==10 or _la==11):
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
            self.state = 59
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
            self.state = 61
            self.match(LayoutParser.T__5)
            self.state = 62
            self.match(LayoutParser.T__1)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 63
                self.big()
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 69
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
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.bounds()
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
            self.state = 73
            self.match(LayoutParser.T__6)
            self.state = 74
            self.match(LayoutParser.T__1)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 75
                self.bound()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 81
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
            self.state = 83
            self.num()
            self.state = 84
            self.num()
            self.state = 85
            self.dims()
            self.state = 86
            self.match(LayoutParser.T__1)
            self.state = 87
            self.filler()
            self.state = 88
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
            self.state = 90
            self.match(LayoutParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





