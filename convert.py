import argparse
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener
from grammar.LayoutLexer import LayoutLexer
from grammar.LayoutParser import LayoutParser
from grammar.LayoutListener import LayoutListener

class Tag:
    def __init__(self, name):
        self.name = name
        self.clazz = None
        self.style = {}

    def set_style(self, key, value):
        if key in self.style:
            raise Exception(f"Already have style for {key}")
        self.style[key] = value

    def set_class(self, clazz):
        if self.clazz != None:
            raise Exception("Already have class")
        self.clazz = clazz

    def render(self, indent, empty):
        attrs = {}
        if self.clazz != None:
            attrs['class'] = self.clazz
        if len(self.style) != 0:
            attrs['style'] = ''.join(f'{key}:{value};' for key,value in self.style.items())
        return ('  ' * indent) + f'<{self.name}' + ''.join(f' {key}="{value}"' for key,value in attrs.items()) + (f'></{self.name}>\n' if empty else '>\n')

class HtmlBuilder:
    def __init__(self):
        self._text = ['<!DOCTYPE html>\n<html>\n<head>\n<style>\n']
        self._text.append("""
body {
    margin: 0;
}
.entire {
    width: 100vw;
    height: 100vh;
}
.grid {
    display: grid;
    width: 100%;
    height: 100%;
}
.cell {
}
""")
        self._text.append('</style>\n</head>\n')
        self._stack = []
        self._pending = None

    def push(self, tag):
        if self._pending is not None:
            self._text.append(self._pending.render(len(self._stack), False))
            self._stack.append(self._pending.name)
        self._pending = Tag(tag)

    def pop(self, tag):
        if self._pending is not None:
            if self._pending.name != tag:
                raise Exception(f"Popping wrong tag. Expecting {self._pending}, got {tag}")
            self._text.append(self._pending.render(len(self._stack), True))
            self._pending = None
        else:
            if self._stack[-1] != tag:
                raise Exception(f"Popping wrong tag. Expecting {self._stack[-1]}, got {tag}")
            self._stack.pop()
            self._text.append('  ' * len(self._stack))
            self._text.append(f'</{tag}>\n')

    def set_style(self, key, value):
        self._pending.set_style(key, value)

    def set_class(self, clazz):
        self._pending.set_class(clazz)

    def finish(self):
        if len(self._stack) != 0:
            raise Exception(f"Stack should be empty, got {self._stack}")
        self._text.append('</html>\n')
        return ''.join(self._text)

class GridContext:
    def __init__(self):
        self.x = 1
        self.y = 1

class ViewportContext:
    def push_divs(self, html, want_scroll):
        if not want_scroll:
            html.push('div')
            html.set_class('entire')

    def pop_divs(self, html, want_scroll):
        if not want_scroll:
            html.pop('div')

class BoundsContext:
    def __init__(self):
        self.x = None
        self.y = None
        self.w = None
        self.h = None

    def push_num(self, num):
        if self.x == None:
            self.x = num
        elif self.y == None:
            self.y = num
        else:
            raise Exception("Too many numbers")

    def push_dims(self, w, h):
        if self.w == None:
            self.w = w
            self.h = h
        else:
            raise Exception("Already have dims")

    def push_divs(self, html, want_scroll):
        html.push('div')
        html.set_style('left', f'{self.x}px')
        html.set_style('top', f'{self.y}px')
        html.set_style('width', f'{self.w}px')
        html.set_style('height', f'{self.h}px')
        if want_scroll:
            html.set_style('overflow', 'scroll')

    def pop_divs(self, html, want_scroll):
        html.pop('div')

class CellContext:
    def push_divs(self, html, want_scroll):
        html.set_style('overflow', 'scroll')

    def pop_divs(self, html, want_scroll):
        pass

    def push_dims(self, w, h):
        # TODO: implement cells bigger than 1x1
        pass


class Converter(LayoutListener):
    def __init__(self):
        self.html = HtmlBuilder()
        self.contexts = []

    # Top level

    def enterViewport(self, ctx):
        self.html.push('body')
        self.contexts.append(ViewportContext())

    def exitViewport(self, ctx):
        self.html.pop('body')

    def finish(self):
        return self.html.finish()

    # Fillers

    def enterColor(self, ctx):
        self.contexts[-1].push_divs(self.html, False)
        self.html.set_style('background', ctx.getText())

    def exitColor(self, ctx):
        self.contexts[-1].pop_divs(self.html, False)

    def enterGrid(self, ctx):
        self.contexts[-1].push_divs(self.html, False)
        self.html.push('div')
        self.html.set_class('grid')
        self.contexts.append(GridContext())

    def exitGrid(self, ctx):
        self.contexts.pop()
        self.html.pop('div')
        self.contexts[-1].pop_divs(self.html, False)

    def enterScroll(self, ctx):
        self.contexts[-1].push_divs(self.html, True)

    def exitScroll(self, ctx):
        self.contexts[-1].pop_divs(self.html, True)

    # Bigs

    def enterBounds(self, ctx):
        self.contexts.append(BoundsContext())

    def exitBounds(self, ctx):
        self.contexts.pop()

    # Cells

    def enterCell(self, ctx):
        self.html.push('div')
        self.html.set_class('cell')
        self.html.set_style('grid-column', str(self.contexts[-1].x))
        self.html.set_style('grid-row', str(self.contexts[-1].y))
        self.contexts[-1].x += 1
        self.contexts.append(CellContext())

    def exitCell(self, ctx):
        self.contexts.pop()
        self.html.pop('div')

    def enterSeparator(self, ctx):
        self.contexts[-1].x = 1
        self.contexts[-1].y += 1

    # Values

    def enterNum(self, ctx):
        self.contexts[-1].push_num(int(ctx.getText()))

    def enterDims(self, ctx):
        w, h = ctx.getText().split('x')
        self.contexts[-1].push_dims(int(w), int(h))


class MyErrorListener(ErrorListener):
    def __init__(self):
        self.has_error = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.has_error = True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('-o', type=str)
    args = parser.parse_args()

    input_stream = FileStream(args.filename)
    lexer = LayoutLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LayoutParser(stream)
    error_listener = MyErrorListener()
    parser.addErrorListener(error_listener)
    tree = parser.viewport()
    if error_listener.has_error:
        raise Exception()
    listener = Converter()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    with open(args.o, 'w') as f:
        f.write(listener.finish())

if __name__ == '__main__':
    main()
