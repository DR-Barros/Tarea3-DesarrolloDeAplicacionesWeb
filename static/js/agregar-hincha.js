let cantDeport = 0;
const DEPORTES = document.getElementsByName("deportes")
DEPORTES.forEach(e =>{
    e.addEventListener("change", function() {
        if(this.checked){
            cantDeport += 1;
            if(cantDeport>=3){
                DEPORTES.forEach(e=>{if(!e.checked) e.disabled=true})
            }
        } else{
            cantDeport -= 1;
            if(cantDeport < 3){
                DEPORTES.forEach(e=>{e.disabled = false})
            }
        }
    })
})

let boton = document.getElementById("Registrar-Hincha");
boton.addEventListener("click", (e)=>{validar(e)});
let comuna = document.getElementById("comuna")
let region =document.getElementById("region");
region.addEventListener("change",(event)=>{
    comuna.disabled = false;
    for (let i = 1; i <= 16; i++) {
        let reg = Array.from(document.getElementsByClassName(i))
        if (i != region.value){
            for(let j = 0; j < reg.length; j++){
                reg[j].style.display = "none"
            }
        } else {
            for(let j = 0; j < reg.length; j++){
                reg[j].style.display = "block"
            }
        }
        
    }
    const I = document.getElementsByClassName
})

function validar(event){
    event.preventDefault()
    let valido = true
    
    //Evaluar condicion de deportes
    let cnt = 0;
    DEPORTES.forEach(e => {if (e.checked) cnt++})
    let deporSpan = document.getElementById("depor-span")
    if (cnt < 1){
        deporSpan.innerText = "Elige al menos 1 deporte"
        valido = false
    } else if (cnt > 3){
        deporSpan.innerText = "Elige maximo 3 deportes"
        valido = false
    } else {
        deporSpan.innerText = ""
    }

    // chequear que ponga region y comuna
    let regionSpan = document.getElementById("region-span")
    let comunaSpan = document.getElementById("comuna-span")
    if (region.value == ""){
        regionSpan.innerText = "Seleccione su región"
        valido = false
    } else if(comuna.value == ""){
        regionSpan.innerText = ""
        comunaSpan.innerText = "Seleccione su comuna"
        valido = false
    } else {
        regionSpan.innerText = ""
        comunaSpan.innerText = ""
    }

    //Nombre
    const NAME = document.getElementById("name")
    let nameSpan = document.getElementById("name-span")
    if(NAME.value.length<3){
        nameSpan.innerText = "Ingrese un nombre de minimo 3 caracteres"
        valido = false
    } else if (NAME.value.length> 80){
        nameSpan.innerText = "El nombre debe ser de maximo 80 caracteres"
        valido = false
    } else {
        nameSpan.innerText = ""
    }

    //Mail
    const EMAIL = document.getElementById("mail")
    const EXP =  /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/
    let emailSpan = document.getElementById("email-span")
    if (!EXP.exec(EMAIL.value)){
        emailSpan.innerText = "Debe ser con el formato de correo"
        valido = false
    } else {
        emailSpan.innerText = ""
    }

    //celular
    const PHONE = document.getElementById("phone");
    const EXPREGPHONE = /^[+]?(56)?9\d{8}$/;
    let phoneSpan = document.getElementById("phone-span");
    if (EXPREGPHONE.exec(PHONE.value) || PHONE.value == ""){
        phoneSpan.innerText = ""
    } else {
        phoneSpan.innerText = "Ingrese un numero chileno ej: +56912345678 o 912345678"
        valido = false
    }


    //comentarios
    const COM = document.getElementById("coment")
    let comSpan = document.getElementById("com-span")
    if (COM.value.length > 80){
        comSpan.innerText = "Tamaño maximo del comentario 80 caracteres"
        valido = false
    } else {
        comSpan.innerText = ""
    }

    if(valido){
        const MSG = document.getElementById("msg")
        let form = document.getElementsByClassName("form")
        form = Array.from(form)
        form.forEach((e) => {e.style.display = "none"})
        let str = "<p>¿Confirma el registro de este hincha?<p>"
        str += "<button id='SI'>Sí, confirmo</button>"
        str += "<button id='NO'>No, quiero volver al formulario</button>"
        MSG.innerHTML = str
        const SI = document.getElementById("SI")
        const NO = document.getElementById("NO")
        // si quiere agregar se avisa que tuvo exito y se grega link a inicio
        //sino vuelve al inventario
        SI.addEventListener("click", e => {
            const FORM = document.getElementById('formulario')
            FORM.submit()
        })
        NO.addEventListener("click", e => {
            FORM.style.display = "block"
            MSG.innerHTML = ""
        })
    }
}