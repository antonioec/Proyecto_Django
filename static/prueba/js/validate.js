function validar(){

    var nombre = document.getElementById("txtNombre");
    var apellido = document.getElementById("txtApellido");

    var errorName = document.getElementById("errorName");
    var errorSur = document.getElementById("errorSur");

    if (nombre.value.length < 1){

        errorName.innerHTML = "Tienes que introducir un nombre";
        return false;
    }
    else
        errorName.innerHTML = ""

    if (apellido.value.length < 1){

        errorSur.innerHTML = "Tienes que introducir un apellido";
        return false;
    }
    else
        errorSur.innerHTML = ""

    return true;

}