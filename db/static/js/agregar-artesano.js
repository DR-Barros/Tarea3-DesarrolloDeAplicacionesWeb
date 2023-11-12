let boton = document.getElementById("Registrar-Artesano");
boton.addEventListener("click", (event)=>agregarArtesano(event));
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

const ARTESANIAS = document.getElementsByName("artesania")
let cantArtesanias = 0;
ARTESANIAS.forEach(e =>{
    e.addEventListener("change", function() {
        if(this.checked){
            cantArtesanias += 1;
            if(cantArtesanias>=3){
                ARTESANIAS.forEach(e=>{if(!e.checked) e.disabled=true})
            }
        } else{
            cantArtesanias -= 1;
            if(cantArtesanias < 3){
                ARTESANIAS.forEach(e=>{e.disabled = false})
            }
        }
    })
})


const FOTO1 = document.getElementById("photo");
const FOTO2 = document.getElementById("foto2");
let photo2;
const FOTO3 = document.getElementById("foto3");
let photo3;
FOTO1.addEventListener("change",(e) => changeFoto1(e));
const FOTOS = []
function changeFoto1(e){
    if (FOTO1.value == ""){
        FOTO2.innerHTML ="";
        photo2 ="";
        FOTO3.innerHTML ="";
        photo3 ="";
    } else {
        FOTO2.innerHTML = "<input name='photo2' id='photo2' type='file' accept='image/png, image/jpeg'></input>"
        photo2 = document.getElementById("photo2")
        photo2.addEventListener("change",(e) => changeFoto2(e));
    }
    
}

function changeFoto2(e){
    if (FOTO2.value == ""){
        FOTO3.innerHTML ="";
        photo3 ="";
    } else {
        FOTO3.innerHTML = "<input name='photo3' id='photo3' type='file' accept='image/png, image/jpeg'></input>"
        photo3 = document.getElementById("photo3")
    }
}


function agregarArtesano(event){
    event.preventDefault()
    let valido = true

    let regionSpan = document.getElementById("region-span")
    let comunaSpan = document.getElementById("comuna-span")
    //Chequea que se introduzca la region y la comuna
    if(region.value == ""){
        regionSpan.innerText = "Seleccione su región";
        valido = false
    } else if(comuna.value == ""){
        comunaSpan.innerText = "Seleccione su comuna";
        valido = false
    } else {
        regionSpan.innerText = "";
        comunaSpan.innerText = "";
    }

    //chequear el tipo artesania
    let cantArt = 0
    let artesaniaSpan = document.getElementById("artesania-span");
    ARTESANIAS.forEach(e=>{if(e.checked) cantArt+=1})
    if(cantArt == 0){
        artesaniaSpan.innerText ="Seleccione al menos una artesania";
        valido = false;
    } else if (cantArt > 3){
        artesaniaSpan.innerText ="Seleccione maximo 3 artesanias";
        valido = false;
    } else{
        artesaniaSpan.innerText = "";
    }


    //Fotos artesania
    let fotosSpan = document.getElementById("fotos-span");
    if (FOTO1.value == ""){
        fotosSpan.innerText = "Agregue al menos una foto"
        valido = false;
    } else {
        fotosSpan.innerText = "";
    }
    


    //Nombre
    const NAME = document.getElementById("name");
    let nameSpan = document.getElementById("name-span");
    if(NAME.value.length<3 || NAME.value.length> 80){
        nameSpan.innerText ="Ingrese un nombre de entre 3 y 80 caracteres";
        valido = false
    } else{
        nameSpan.innerText = "";
    }

    //Mail
    const EMAIL = document.getElementById("mail")
    let mailSpan = document.getElementById("mail-span")
    const EXP =  /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/
    if (!EXP.exec(EMAIL.value)){
        mailSpan.innerText ="Debe ser con el formato de correo";
        valido = false
    } else {
        mailSpan.innerText ="";
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
    if(valido){
        const MSG = document.getElementById("msg")
        let form = document.getElementsByClassName("form")
        form = Array.from(form)
        form.forEach((e) => {e.style.display = "none"})
        let str = "<p>¿Confirma el registro de este artesano?<p>"
        str += "<button id='SI'>Sí, confirmo</button>"
        str += "<button id='NO'>No, quiero volver al formulario</button>"
        MSG.innerHTML = str
        const SI = document.getElementById("SI")
        const NO = document.getElementById("NO")
        // si quiere agregar se avisa que tuvo exito y se grega link a inicio
        //sino vuelve al inventario
        SI.addEventListener("click", e => {
            const FORM = document.getElementById('form')
            FORM.submit()
        })
        NO.addEventListener("click", e => {
            form.style.display = "block"
            MSG.innerHTML = ""
        })
    }
}