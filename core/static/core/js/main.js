// $(function(){

//     $("#Registrate").click(function(){
//        window.open('sesioniniciada.html') 
//     });
// });
$(document).ready(main)
function main() {
    $(function () {
        $(".formulario ").validate({
            rules:{
                Nombre:{
                    required: true,
                    minlenght: 4,
                    maxlength: 10
                },
                Apellido:{
                    required: true,
                    minlength: 3,
                    maxlength: 20
                },
                Email:{
                    required: true,
                    email: true
                },
                Contraseña:{
                    required: true,
                    minlength: 8,
                    maxlength: 10
                }
            },
            messages:{
                Nombre:{
                    required: 'Ingrese un nombre',
                    minlenght: 'Largo menor al minimo aceptado',
                    maxlength: 'Largo maximo es de 10'
                },
                Apellido:{
                    required: 'Ingrese Apellido',
                    minlenght: 'Largo menor al minimo aceptado',
                    maxlength: 'Largo maximo es de 20'
                },
                Email:{
                    required: 'Ingrese un email',
                    email: 'Formato de email incorrecto'
                },
                Contraseña:{
                    required: 'Ingrese la contraseña',
                    minlength: 'Largo insuficiente de la contraseña',
                    maxlength: 'Largo excedido de contraseña,Max 3 caracteres'
                },
            },
            errorElement: "div"
        });
    });
};


