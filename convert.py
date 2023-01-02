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
.grid {
    display: grid;
    height: 100vh;
    width: 100vw;
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

class Converter(LayoutListener):
    def __init__(self):
        self.html = HtmlBuilder()
        self.x = 1
        self.y = 1

    def enterWin(self, ctx):
        self.html.push('body')

    def exitWin(self, ctx):
        self.html.pop('body')

    def enterColor(self, ctx):
        self.html.set_style('background', ctx.getText())

    def enterGrid(self, ctx):
        self.html.push('div')
        self.html.set_class('grid')

    def exitGrid(self, ctx):
        self.html.pop('div')

    def enterCell(self, ctx):
        self.html.push('div')
        self.html.set_class('cell')
        self.html.set_style('grid-column', str(self.x))
        self.html.set_style('grid-row', str(self.y))
        self.x += 1

    def exitCell(self, ctx):
        self.html.pop('div')

    def enterSeparator(self, ctx):
        self.x = 1
        self.y += 1

    def finish(self):
        return self.html.finish()

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
    tree = parser.win()
    if error_listener.has_error:
        raise Exception()
    listener = Converter()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    with open(args.o, 'w') as f:
        f.write(listener.finish())

if __name__ == '__main__':
    main()
