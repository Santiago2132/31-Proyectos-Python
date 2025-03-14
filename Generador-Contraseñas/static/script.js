function generarContraseña() {
    const longitud = document.getElementById("longitud").value;
    const mayusculas = document.getElementById("mayusculas").checked;
    const minusculas = document.getElementById("minusculas").checked;
    const numeros = document.getElementById("numeros").checked;
    const simbolos = document.getElementById("simbolos").checked;

    fetch("/generar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ longitud, mayusculas, minusculas, numeros, simbolos })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("resultado").value = data.contraseña;
    });
}

function copiarContraseña() {
    const inputContraseña = document.getElementById("resultado");
    inputContraseña.select();
    document.execCommand("copy");

    const mensaje = document.getElementById("mensaje");
    mensaje.style.display = "block";
    setTimeout(() => { mensaje.style.display = "none"; }, 2000);
}
