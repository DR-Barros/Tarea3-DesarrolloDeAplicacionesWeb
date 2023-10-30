let hincha = document.getElementsByClassName("hincha")
hincha = Array.from(hincha)
hincha.forEach(element => {
    element.addEventListener("click", e => {
        window.location.href = "./informacion-hincha-"+ String(element.id);
    })
});