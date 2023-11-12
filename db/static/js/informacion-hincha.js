const urlParams = new URLSearchParams(window.location.search)
const NAME = urlParams.get("Nombre");
const nombre = document.getElementById('nombre')
const region = document.getElementById('region')
const comuna = document.getElementById('comuna')
const transporte = document.getElementById('transporte')
const deportes = document.getElementById('deportes')
const mail = document.getElementById('mail')
const phone = document.getElementById('phone')
const comentarios = document.getElementById('comentarios')
fetch("./datos/hinchas.json")
.then(response => response.json())
.then(data => {
    data.hinchas.forEach(e => {
        if (e.Nombre == NAME) {
            nombre.innerText = e.Nombre
            region.innerText = e.Region
            comuna.innerText = e.Comuna
            transporte.innerText = e.Transporte
            let depor = ""
            e.Deportes.forEach(d => depor+="<br>"+d+" ")
            deportes.innerHTML = depor
            mail.innerText = e.Email
            phone.innerText = e.Celular
            if (Object.keys(e).some(x => x == "Comentario")){
                comentarios.innerText = e.Comentario
            }
        }
    });
})