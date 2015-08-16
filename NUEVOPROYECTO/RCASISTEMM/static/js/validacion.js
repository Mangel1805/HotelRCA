/**
 * Created by Eduardo on 24/02/2015.
 */
$(function() {

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

};

});