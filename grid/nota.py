"""
& flex:
layout lineal
c define horizontal o vertical
flex puede crear cuadrícula, conlleva más esfuerzo
90 95% d layouts en internet

~ propiedades contenedor grid:
c divide dos partes...

& grid:
layout cuadrícular nativo
d forma nativa puede definir columnas, filas
5% d layouts en internet
mover, posicionar elementos d forma compleja o específica

~ propiedades contenedor grid:
c divide dos partes:

propiedades q aplican 'contenedor'
propiedades q aplican 'cada 1 d elementos' 
* generalmente concentra a propiedades que aplica 'contenedor'

.container{
    ~ muestra etiqueta grid en inspector
    display: grid;
    height: 300px;
    width: 600px;

    *fr: fracción del espacio
    *1fr = 100%... 1fr 1fr = 50% + 50%
    *1fr 1fr = repeat(2, 1fr)
    *puede usarse: 1fr 100px 1fr
    *[c1] [c2] ... referencia lineas entre fracción...

    ~grid-template-columns: [c1] 1fr [c2] 1fr [c3] 1fr [c4];
    ~grid-template-rows: [f1] 1fr [f2] 1fr [f3];

    * repeat#1 = rows / repeat#2 = columns
    grid-template: repeat(3,1f)/repeat(4,1fr);

    * establece nombre de cada fracción
    ~ si agrego columnas debo agregar nombres 
    grid-template-areas: 
        "header header header header"
        "main . . sidebar"
        "footer footer footer footer";
 
}


* 3 Columnas: col1 %automático, col2 50px, col3 %automático
grid-template-columns: auto 50px auto;
* 2 Filas, 3 nombres d linea: fila1 100px...
grid-template-rows: [r1] 100px [r2] 100px [r3];

* 3 col d fila 1 = header
* 3 col d fila 2 = footer 
grid-template-areas: 
    "header header header"
    "footer footer footer"

^ FILAS: línea + nombre + tamaño / COLUMNAS: línea + tamaño
grid-template:
    [r1] "h1 h2 h h" 60px
    [r2] "f f f3 f4" 170px [rf]
    /
    [c1] auto
    [c2] 100px
    [c3] 50px 
    [c4] auto [cf]

* significa puede llamarse 1 u otro nombre
[row1 row2]

^unidad "fr":
fracción d espacio disponible en contenedor
c divide espacio restante partes iguales
según cantidad d "fr" especificada

^unidad  "auto":
especifica tamaño elemento determina automáticamente por navegador
en función de su contenido y otros factores
como posición en diseño y las propiedades de elementos vecinos


* primero filas despues columnas
* si el espacio será el mismo
gap: 20px 10px;

*también:
column-gap: 10px;
    row-gap: 10px;

    
^ justify-content:
alinea items dentro contenedor, SI contenedor + grande q items
^ justify-items:
Acomoda elementos dentro d 'fracciones' 

    ^ space-around:
    lineas 1 y final 'diferente' tamaño a lineas entre fracciones
    ^ space-evenly:
    lineas 1 y final mismo tamaño a lineas entre fracciones
    ^ space-between:
    lineas 1 y final mismo tamaño a lineas entre fracciones
    fracciones pegadas en lineas 1 y final y lineas intermedias iguales

* puede ser: 
justify-content: center;
align-content: center;
* también 1 = align, 2 = justify
^ place-content: space-between end;

* puede ser:
justify-items: center;
align-items: center;
* también 1 = align, 2 = justify
^ place-items: start start;

~ border-radius: 9px; bordes redonditos

^ box-sizing: border-box;
controla cómo calcula tamaño total elemento 'ancho, alto, borde, relleno (padding)'
'ancho alto' incluirá 'relleno borde',
en lugar d calcular sólo para contenido
tamaño total d elemento: incluye 'relleno borde' establecido
sin q 'relleno borde' c sumen a tamaño total
definir tamaño incluyendo todo lo que forma parte d su caja
en lugar d tener q ajustar tamaños d cajas individuales para incluir 'relleno borde'
evita elementos c desborden superpongan al añadir 'relleno borde'


^ grid-column-start: 1;
^ grid-column-end: 3;
^ grid-row-start: 1;
^ grid-row-end: 3;
especifica donde comienza termina fraccion

^ grid-column-start: c1;
^ grid-column-end: c1;
^ grid-row-start: c1;
^ grid-row-end: c1;
inicia linea 1 a linea n

^ grid-column: 1 / span 2;
^ grid-row: 1 / span 3;
1 = start y 2 = end
span = abarca n fracciones

^ grid-area: header;
por nombre

^ justify-self: center start end stretch;
^ align-self: center start end stretch;
justifica elemento dentro fracción

^ place-self: center center;
1 = align y 2 = justify

^ min-height: 40px;
^ min-width: 40px;
min = tamaño mínimo

^ overflow: hidden
controlar desbordamiento con tamaño fijo
contenido > contenedor = oculto

^ padding: 0 3em;
espacio entre contenido borde
0 superior inferior
3em izquierdo derecho
em relativo tamaño fuente elemento 
~ 3em '3 veces tamaño fuente'

^ grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
auto-fit: ajusta n columnas quepan ancho
minmax(): ancho mín 300px, máx: 1fr + espacio: distribuirá

^ outline: 3px solid;
borde fuera elemento

^ z-index: 10;
posición eje Z (profundidad)
elementos superpuestos cual aparece encima
valor + alto: parte superior
10 colocará encima de inferiores
! sólo funciona elementos posicionados
! propiedad posición diferente a "static"

^ @media (min-width: 700px){
    ~.contenedor{
        grid-template-columns: repeat(4,1fr);
        grid-template-rows: repeat(4,1fr);

        ~grid-template-areas: 
        "header header header header"
        "main main main sidebar"
        "main main main sidebar"
        "footer footer footer footer";
    }
}
~ @media: regla aplicar estilos
ancho pantalla > 700px
para clase '.contenedor'

^ transform: translate(100%,100%);
mueve 100% derecha/abajo, -100% izquierda/arriba
^ transition: transform .3s;
animación transición, cualquier cambio transform
! cualquier cambio en propiedad transform tardará 0,4 segundos en realizarse
^ transform: translate(0);
0 = posición original

^ *{margin: 0;}
Si no establece: navegador aplica predeterminado margen, relleno
evita espacios no deseados, consistencia

^ figure
contenido multimedia
separar visualmente multimedia d resto
contexto para motor búsqueda 

^ box-shadow: horizontal, vertical, blur, radius, color;
sombras alrededor
^ hsl(212, 86%, 64%, .5) - Hue = 360, Saturation = %, Lightness = %
verde azulado, opacidad 50%


^ .clase:nth-child(n)
selecciona #elemento d elemento,
div con h1 e img, child(2) aplica img

^ em 
c basa tamaño fuente padre inmediato
padre = 16px x secundario = 0.5em: 8px
escale con fuente d padre inmediatos

^ rem
c basa tamaño fuente raíz normalmente <html>
secundario 0.5rem, fuente = mitad fuente raíz
escalen con fuente d página en conjunto

^ display: block;
establece tipo caja, debe renderizarse como bloque
ocupa ancho disponible, comienza en nueva línea
bloques predeterminada <div>, <p>, <h1>-<h6>, <ul>, <ol>, etc.
permite aplicar ancho, alto, margen, padding

^ width: max-content
ancho adapte al contenido sin establecer ancho fijo
ajusta al ancho máximo necesite para mostrar contenido
Por ejemplo, elemento texto, ancho ajustará para todo texto ajuste dentro ancho elemento
ancho real puede ser menor si contenido no requiere ancho máximo

^ background-image: #1 degradado, #2 imagen/url
^ linear-gradient(to bottom, black, white);
^ rgba(rojo, verde, azul, alpha = decimal)

^ background-size: cover
establece tamaño d imagen d fondo
hacerla cubrir completamente sin deformar la imagen

! -- para definir variable personal

! :root{}
buena práctica definir variables global
nivel + alto árbol DOM (Document Object Model)
disponibles para todos, incluyendo descendientes

^ <nav class="nav container" id="nav">
^ <a href="#nav" class="nav__hamburguer">
^ (url) ~ [fragmento url/id=""]:target{}

enlace en barra navegación apunta a #nav
clic = establece fragmento URL #nav
aplica estado ':target' a ETIQUETA nav

propiedad transform .nav__close establece scale(1) 'close aparece'
propiedad transform .nav__hamburguer establece scale(0) 'menu desaparece' y 'slide aparece'

^ scale()
1 = original
0 = desaparece
2 = doble
0.5 = mitad

^ "position":
establecer tipo d posición d elemento en página
^ "absolute":
especifica elemento c posicionará en relación a su primer elemento padre
que tenga posición distinta a "static" (posición predeterminada d elementos en CSS)
^ "position: absolute;
retira el elemento del flujo normal... 
c coloca en 'posición absoluta' en página
coordenadas d su posición c especifican con propiedades "top", "bottom", "left" y "right"

^ unset en @media
establece la propiedad en su valor inicial

^ grid-auto-flow
valor predeterminado de grid-auto-flow es row
row: en filas
column: columnas
row dense: filas, llena fila anterior vacía
column dense: columnas, llena fila anterior vacía

! Cual es la sintaxis general de ... ?
"""