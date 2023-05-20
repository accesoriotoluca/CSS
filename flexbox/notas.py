"""
! type="text/css" 'Para que quede aún mas claro...'

^ div vs section
agrupar organizar contenido

~ div:
etiqueta genérica divide contenido en 'secciones lógicas'
crea contenedores, agrupa elementos relacionados, aplica estilos 
* no transmite información semántica sobre contenido q contiene
~ principalmente fines diseño, estilo

~ section:
divide contenido en secciones 'temáticas + grandes y significativas'
agrupar contenido q comparte 'tema común'
y puede contener encabezados, subencabezados y otros elementos relacionados con temática
* transmite información semántica sobre contenido q contiene
* ayuda a motores d búsqueda, programas a entender estructura de página

*float: left; 
elemento c coloque a izquierda contenedor
otros elementos 'floten' a derecha
*elementos colocan 1 a lado d otro, en lugar d apilarse

^ align-items: baseline;
alinea a margen texto
*line-height: 120px;
altura cada línea texto dentro elemento
~ si se aplica margen a 1 item:
 ~ baseline alinea todos los item a ese margen

*width: 80%;
ancho elemento 80% ancho contenedor
elemento ajusta ancho contenedor
elementos 'floten' a su lado

*margin: 0 auto;
establece márgenes elemento
margen superior inferior 0
margen izquierdo derecho auto
centrado horizontalmente dentro contenedor

^ flex direction filas o columnas
flex-direction: row;
flex-direction: row-reverse
flex-direction: column;
flex-direction: column-reverse;
^ flex-wrap: wrap; y flex-wrap: wrap-reverse;
* si no espacio: nueva fila + elementos
how items arrange, isn't enough container space fit single line
will wrap onto new line when run out horizontal space
By default, try fit single line, overflowing container
~ 1 = direction y 2 = wrap
^ flex-flow: row wrap;

! justify-items no funciona con flex
justify-items: alinear elementos secundarios eje principal
aplica contenedores bloque, grid
! flex usa justify-content para alinear elementos secundarios eje principal
controlar espacio entre elementos secundarios y bordes contenedor

^ flex-grow 'valor numérico'
si 1 = "2" y 2 = "1":
1 crecerá en proporción 'doble' a 2
^ flex-shrink
Que tan rápido se hara mas pequeño un item que otro
^ flex-basis
! si contenedor mayor llega a límite deja de estirar
! si contenedor menor se encoge
tamaño inicial elemento
container = 800px, basis: 50%: flex item = 400px
basis starting point but adjusted by flex properties flex-grow/flex-shrink
^ flex: 0 1 auto;
~ flex: ; [grow] [shrink] [basis]

^ object-fit: cover;
imagen ajuste a contenedor, cubra superficie, sin deformar
si imagen + pequeña: expandirá
si imagen + grande: recortará

!flex: 1;
elemento puede estirar contraer ajustarse contenedor
! transition: .5s flex;
transición aplicará cuando surja cambio en propiedad flex
! .contenedor_imagen:hover{ flex: 10; }
regla cursor sobre elemento
propiedad flex cambia a 10
contenedor estire 10 veces tamaño original


"""