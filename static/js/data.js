const HTTP = new XMLHttpRequest()
HTTP.open("GET", 'artesano-data')
HTTP.onload = function() {
    if (HTTP.status === 200) {
        let data = JSON.parse(HTTP.responseText)
        console.log(data)
        graficar(data)
    } else {
        console.error('Error:', HTTP.statusText)
    }
}
HTTP.onerror = function() {
    console.error('Error de red')
}
HTTP.send()

function graficar(data) {
    let  tipos = [], cant = []
    data.forEach(element => {
        tipos.push(element[0])
        cant.push(element[1])
    });
    const CHART = Highcharts.chart('artesanos', {
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Número de Artesanos según el tipo de artesania'
        },
        xAxis: {
            categories: tipos
        },
        yAxis: {
            title: {
                text: 'Cantidad de Artesanos'
            }
        },
        series: [{
            name: '',
            data: cant
        }]
    });
}

const HTTPHincha = new XMLHttpRequest()
HTTPHincha.open("GET", 'hincha-data')
HTTPHincha.onload = function() {
    if (HTTPHincha.status === 200) {
        let data = JSON.parse(HTTPHincha.responseText)
        
        console.log(data)
        graficarHincha(data)
    } else {
        console.error('Error:', HTTPHincha.statusText)
    }
}
HTTPHincha.onerror = function() {
    console.error('Error de red')
}
HTTPHincha.send()

function graficarHincha(data) {
    let  tipos = [], cant = []
    data.forEach(element => {
        tipos.push(element[0])
        cant.push(element[1])
    });
    const CHART = Highcharts.chart('hinchas', {
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Número de Hinchas por deporte'
        },
        xAxis: {
            categories: tipos
        },
        yAxis: {
            title: {
                text: 'Cantidad de Hinchas'
            }
        },
        series: [{
            name: '',
            data: cant
        }]
    });
}

