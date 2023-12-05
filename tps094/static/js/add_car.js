document.addEventListener('DOMContentLoaded', function() {

    var lineasPorMarca = {
        'Toyota': ['Corolla', 'Camry', 'Prius',],
        'Mazda': ['Mazda3', 'Mazda6', 'CX-5',],
    };

    var marcaSelect = document.getElementById('id_marca');
    var lineaSelect = document.getElementById('id_linea');

    document.getElementById('id_marca').addEventListener('change', function() {
        var marcaSeleccionada = this.value;
        var lineas = lineasPorMarca[marcaSeleccionada];
        var lineaSelect = document.getElementById('id_linea');
        lineaSelect.innerHTML = '';

        lineas.forEach(function(linea) {
            var option = new Option(linea, linea);
            lineaSelect.options.add(option);
        });
    });

    if (marcaSelect.value) {
        marcaSelect.dispatchEvent(new Event('change'));
    }
    
});
