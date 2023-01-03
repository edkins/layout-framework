# Generated from Layout.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LayoutParser import LayoutParser
else:
    from LayoutParser import LayoutParser

# This class defines a complete generic visitor for a parse tree produced by LayoutParser.

class LayoutVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LayoutParser#viewport.
    def visitViewport(self, ctx:LayoutParser.ViewportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LayoutParser#filler.
    def visitFiller(self, ctx:LayoutParser.FillerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LayoutParser#grid.
    def visitGrid(self, ctx:LayoutParser.GridContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LayoutParser#cell.
    def visitCell(self, ctx:LayoutParser.CellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LayoutParser#separator.
    def visitSeparator(self, ctx:LayoutParser.SeparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LayoutParser#color.
    def visitColor(self, ctx:LayoutParser.ColorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LayoutParser#dims.
    def visitDims(self, ctx:LayoutParser.DimsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LayoutParser#scroll.
    def visitScroll(self, ctx:LayoutParser.ScrollContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LayoutParser#big.
    def visitBig(self, ctx:LayoutParser.BigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LayoutParser#bounds.
    def visitBounds(self, ctx:LayoutParser.BoundsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LayoutParser#bound.
    def visitBound(self, ctx:LayoutParser.BoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LayoutParser#num.
    def visitNum(self, ctx:LayoutParser.NumContext):
        return self.visitChildren(ctx)



del LayoutParser