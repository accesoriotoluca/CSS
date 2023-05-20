console.log('hola')
const titleviewport = document.createElement('h1')
const element = document.querySelector('.imagen')
const container = document.querySelector('.container')

showElementWidth()

window.addEventListener('resize',showElementWidth)

function showElementWidth(){

    const widthElement = element.clientWidth
    titleviewport.innerText = `Ancho ${widthElement}px`
    titleviewport.style.margin = '10px 0'
    titleviewport.style.border = '1px dotted rgba(0, 0, 0, .2)'
    container.append(titleviewport)
}