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
        4,1,9,51,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        1,0,1,0,1,0,1,0,1,0,1,1,1,1,3,1,22,8,1,1,2,1,2,1,2,1,2,5,2,28,8,
        2,10,2,12,2,31,9,2,1,2,1,2,1,3,1,3,1,3,5,3,38,8,3,10,3,12,3,41,9,
        3,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,1,
        1,0,7,8,47,0,14,1,0,0,0,2,21,1,0,0,0,4,23,1,0,0,0,6,34,1,0,0,0,8,
        44,1,0,0,0,10,46,1,0,0,0,12,48,1,0,0,0,14,15,5,1,0,0,15,16,5,2,0,
        0,16,17,3,2,1,0,17,18,5,3,0,0,18,1,1,0,0,0,19,22,3,4,2,0,20,22,3,
        10,5,0,21,19,1,0,0,0,21,20,1,0,0,0,22,3,1,0,0,0,23,24,5,4,0,0,24,
        29,5,2,0,0,25,28,3,6,3,0,26,28,3,8,4,0,27,25,1,0,0,0,27,26,1,0,0,
        0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,32,1,0,0,0,31,29,
        1,0,0,0,32,33,5,3,0,0,33,5,1,0,0,0,34,35,3,12,6,0,35,39,5,2,0,0,
        36,38,3,2,1,0,37,36,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,
        0,0,0,40,42,1,0,0,0,41,39,1,0,0,0,42,43,5,3,0,0,43,7,1,0,0,0,44,
        45,5,5,0,0,45,9,1,0,0,0,46,47,7,0,0,0,47,11,1,0,0,0,48,49,5,6,0,
        0,49,13,1,0,0,0,4,21,27,29,39
    ]

class LayoutParser ( Parser ):

    grammarFileName = "Layout.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'window'", "'{'", "'}'", "'grid'", "'--'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "DIMS", "COLOR3", "COLOR6", 
                      "WS" ]

    RULE_win = 0
    RULE_filler = 1
    RULE_grid = 2
    RULE_cell = 3
    RULE_separator = 4
    RULE_color = 5
    RULE_dims = 6

    ruleNames =  [ "win", "filler", "grid", "cell", "separator", "color", 
                   "dims" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    DIMS=6
    COLOR3=7
    COLOR6=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class WinContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def filler(self):
            return self.getTypedRuleContext(LayoutParser.FillerContext,0)


        def getRuleIndex(self):
            return LayoutParser.RULE_win

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWin" ):
                listener.enterWin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWin" ):
                listener.exitWin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWin" ):
                return visitor.visitWin(self)
            else:
                return visitor.visitChildren(self)




    def win(self):

        localctx = LayoutParser.WinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_win)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(LayoutParser.T__0)
            self.state = 15
            self.match(LayoutParser.T__1)
            self.state = 16
            self.filler()
            self.state = 17
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
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.grid()
                pass
            elif token in [7, 8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.color()
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
            self.state = 23
            self.match(LayoutParser.T__3)
            self.state = 24
            self.match(LayoutParser.T__1)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==6:
                self.state = 27
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 25
                    self.cell()
                    pass
                elif token in [5]:
                    self.state = 26
                    self.separator()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
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
            self.state = 34
            self.dims()
            self.state = 35
            self.match(LayoutParser.T__1)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 400) != 0:
                self.state = 36
                self.filler()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
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
            self.state = 44
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
            self.state = 46
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
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
            self.state = 48
            self.match(LayoutParser.DIMS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





