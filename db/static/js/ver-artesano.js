let artesano = document.getElementsByClassName("artesano")
artesano = Array.from(artesano)
artesano.forEach(element => {
    element.addEventListener("click", e => {
        window.location.href = "./informacion-artesano-"+ String(element.id);
    })
});