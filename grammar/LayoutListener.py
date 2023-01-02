# Generated from Layout.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LayoutParser import LayoutParser
else:
    from LayoutParser import LayoutParser

# This class defines a complete listener for a parse tree produced by LayoutParser.
class LayoutListener(ParseTreeListener):

    # Enter a parse tree produced by LayoutParser#viewport.
    def enterViewport(self, ctx:LayoutParser.ViewportContext):
        pass

    # Exit a parse tree produced by LayoutParser#viewport.
    def exitViewport(self, ctx:LayoutParser.ViewportContext):
        pass


    # Enter a parse tree produced by LayoutParser#filler.
    def enterFiller(self, ctx:LayoutParser.FillerContext):
        pass

    # Exit a parse tree produced by LayoutParser#filler.
    def exitFiller(self, ctx:LayoutParser.FillerContext):
        pass


    # Enter a parse tree produced by LayoutParser#grid.
    def enterGrid(self, ctx:LayoutParser.GridContext):
        pass

    # Exit a parse tree produced by LayoutParser#grid.
    def exitGrid(self, ctx:LayoutParser.GridContext):
        pass


    # Enter a parse tree produced by LayoutParser#cell.
    def enterCell(self, ctx:LayoutParser.CellContext):
        pass

    # Exit a parse tree produced by LayoutParser#cell.
    def exitCell(self, ctx:LayoutParser.CellContext):
        pass


    # Enter a parse tree produced by LayoutParser#separator.
    def enterSeparator(self, ctx:LayoutParser.SeparatorContext):
        pass

    # Exit a parse tree produced by LayoutParser#separator.
    def exitSeparator(self, ctx:LayoutParser.SeparatorContext):
        pass


    # Enter a parse tree produced by LayoutParser#color.
    def enterColor(self, ctx:LayoutParser.ColorContext):
        pass

    # Exit a parse tree produced by LayoutParser#color.
    def exitColor(self, ctx:LayoutParser.ColorContext):
        pass


    # Enter a parse tree produced by LayoutParser#dims.
    def enterDims(self, ctx:LayoutParser.DimsContext):
        pass

    # Exit a parse tree produced by LayoutParser#dims.
    def exitDims(self, ctx:LayoutParser.DimsContext):
        pass



del LayoutParser