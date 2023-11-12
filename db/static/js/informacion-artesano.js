function agrandarFoto(){
    const FOTOS = document.getElementsByClassName("fotos")
    for (let i = 0; i < FOTOS.length; i++) {
        FOTOS[i].style.width = "640px";
        FOTOS[i].style.height = "480px";
        FOTOS[i].addEventListener("click", e =>{fixSize(i)});
    }
}
function fixSize(i){
    const FOTOS = document.getElementsByClassName("fotos")
    for (let j = 0; j < FOTOS.length; j++) {
        if (j == i){
            if (FOTOS[i].style.width == "1280px"){
                FOTOS[j].style.width = "640px";
                FOTOS[j].style.height = "480px";
            } else {
                FOTOS[i].style.width = "1280px"
                FOTOS[i].style.height = '1024px';
            } 
        } else {
            FOTOS[j].style.width = "640px";
            FOTOS[j].style.height = "480px";
        }
    }
}
agrandarFoto()