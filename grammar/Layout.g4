grammar Layout;
viewport: 'viewport' '{' filler '}';
filler: grid
       | color
       ;
grid: 'grid' '{' (cell | separator)* '}';
cell: dims '{' filler* '}';
separator: '--';
color: COLOR3 | COLOR6;
dims: DIMS;

DIMS: [0-9]+[x][0-9]+;
COLOR3: [#][0-9a-f][0-9a-f][0-9a-f];
COLOR6: [#][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f];
WS: [ \r\n\t]+ -> skip;
