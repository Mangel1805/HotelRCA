
/**
 * Created by Danny on 07/02/2015.
 */
$(function ()
{


String.prototype.capitalize = function()
{
    return this.replace(/\w+/g, function(a)
    {
        return a.charAt(0).toUpperCase() + a.slice(1).toLowerCase();
    });
};

$.soloDireccion=function validarDireccion(e) { // 1
    tecla = (document.all) ? e.keyCode : e.which;
        if (tecla==9) return true; //tab
        if (tecla==8) return true; // backspace
		if (tecla==32) return true; // espacio
		if (e.ctrlKey && tecla==86) { return true;} //Ctrl v
		if (e.ctrlKey && tecla==67) { return true;} //Ctrl c
		if (e.ctrlKey && tecla==88) { return true;} //Ctrl x

		patron = /^[a-zA-Z\.0-9]+$/i; //patron


		te = String.fromCharCode(tecla);
		return patron.test(te); // prueba de patron
	}

$.soloChasis=function validarChasis(e) { // 1
    tecla = (document.all) ? e.keyCode : e.which;
        if (tecla==9) return true; //tab
        if (tecla==8) return true; // backspace
		if (e.ctrlKey && tecla==86) { return true;} //Ctrl v
		if (e.ctrlKey && tecla==67) { return true;} //Ctrl c
		if (e.ctrlKey && tecla==88) { return true;} //Ctrl x
		patron = /^[a-zA-Z0-9]+$/i; //patron
        te = String.fromCharCode(tecla);
		return patron.test(te); // prueba de patron
	}

$.soloPlaca=function validarPlaca(e)
{ // 1
    tecla = (document.all) ? e.keyCode : e.which;
        if (tecla==9) return true; //tab
        if (tecla==8) return true; // backspace
		if (e.ctrlKey && tecla==86) { return true;} //Ctrl v
		if (e.ctrlKey && tecla==67) { return true;} //Ctrl c
		if (e.ctrlKey && tecla==88) { return true;} //Ctrl x

		patron = /^[a-zA-Z\-0-9]+$/i; //patron


		te = String.fromCharCode(tecla);
		return patron.test(te); // prueba de patron
	}

$.soloLetras=function validarLetras(e) { // 1
    tecla = (document.all) ? e.keyCode : e.which;
        if (tecla==9) return true; //tab
        if (tecla==8) return true; // backspace
		if (tecla==32) return true; // espacio
		if (e.ctrlKey && tecla==86) { return true;} //Ctrl v
		if (e.ctrlKey && tecla==67) { return true;} //Ctrl c
		if (e.ctrlKey && tecla==88) { return true;} //Ctrl x

		patron = /[a-zA-Z]/; //patron

		te = String.fromCharCode(tecla);
		return patron.test(te); // prueba de patron
	}


$.soloNumDecimales=function validar_numeros_decimales(e, field) {
  key = e.keyCode ? e.keyCode : e.which
  // backspace
  if (key == 8) return true
  // 0-9
  if (key > 47 && key < 58) {
    if (field.value == "") return true
    regexp = /,[0-9]{2}$/
    return !(regexp.test(field.value))
  }
  // . --> 46  , -->44
  if (key == 44) {
    if (field.value == "") return false
    regexp = /^[0-9]+$/
    return regexp.test(field.value)
  }
  // other key
  return false

}

$.soloNumeros=function validar_numeros(e, field) {
  key = e.keyCode ? e.keyCode : e.which
  // backspace
  if (key == 8) return true
  // 0-9
  if (key > 47 && key < 58) {
    if (field.value == "") return true
    regexp = /.[0-9]{*}$/
    return !(regexp.test(field.value))
  }

  return false

}



    $.calcular_edad=function(fecha)
    {
        //var fechaActual = new Date()
        var diaActual = new Date().getDate();
        var mmActual = new Date().getMonth() + 1;
        var yyyyActual = new Date().getFullYear();
        FechaNac = fecha.split("/");
        var diaCumple = FechaNac[0];
        var mmCumple = FechaNac[1];
        var yyyyCumple = FechaNac[2];
        //retiramos el primer cero de la izquierda
        if (mmCumple.substr(0,1) == 0)
        {
            mmCumple= mmCumple.substring(1, 2);
        }
        //retiramos el primer cero de la izquierda
        if (diaCumple.substr(0, 1) == 0)
        {
        diaCumple = diaCumple.substring(1, 2);
        }
        var edad = yyyyActual - yyyyCumple;

        //validamos si el mes de cumpleaños es menor al actual
        //o si el mes de cumpleaños es igual al actual
        //y el dia actual es menor al del nacimiento
        //De ser asi, se resta un año
        if ((mmActual < mmCumple) || (mmActual == mmCumple && diaActual < diaCumple))
        {
            edad--;
        }
        return edad;
    };







});



