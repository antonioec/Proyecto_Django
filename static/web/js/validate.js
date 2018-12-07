
$('#ContactForm').submit(function (event) {

    if ($('#txtNombre').val()==''){

        $('#errorName').html("Tiene que introducir su Nombre y Apellidos.");
        event.preventDefault();
        return false;
    }
    else
        $('#errorName').html("");

    if ($('#txtEmail').val()==''){

        $('#errorEmail').html("Tiene que introducir su Email.");
        event.preventDefault();
        return false;
    }

    else
        $('#errorEmail').html("")

    var email = $('#txtEmail').val();
    if (email.indexOf("@") == -1 || email.indexOf(".") == -1) {

        errorEmail.innerHTML = "Tiene que introducir un Email válido.";
        event.preventDefault();
        return false;
    }

    else
        errorEmail.innerHTML = ""

    if ($('textarea#txtArea').val()==''){

        $('#errorArea').html("Tiene que introducir su Mensaje.");
        event.preventDefault();
        return false;
    }
    else
        $('#errorArea').html("");

    if ($('#privacy').is(':checked')==false){

        $('#errorPrivacy').html("Tiene que aceptar nuestras políticas de privacidad.");
        event.preventDefault();
        return false;
    }
    else
        $('#errorPrivacy').html("");

    return true;

});
