let str = "<tr><td>Nombre</td><td>Comuna</td><td>Deportes</td><td>Modo Transporte</td><td>Numero celular</td></tr>"
const LISTADOHINCHAS = document.getElementById("tabla");
fetch("./static/datos/hinchas.json")
.then(response => response.json())
.then(data => {
    data.hinchas.forEach(e =>{
        str += "<tr><td><a href='./informacion-hincha.html?Nombre="+e.Nombre+"'>"+e.Nombre+"</a></td>"
        str += "<td>"+e.Comuna+"</td><td>"
        e.Deportes.forEach(e =>{str += " "+ e + "<br>"})
        str += "</td><td>"+e.Transporte+"</td>"
        str += "<td>"+e.Celular+"</td><tr>"
    })
    LISTADOHINCHAS.innerHTML = str
})