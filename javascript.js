// imprimir "hola mundo" en consola
console.log('Hola Mundo');

/* ====================================================
7. Permitir ingresar al usuario un numero de un digito. Controlando se haya ingresado dicho numero de no mas de 1 digito de longitud, pasarlo a letras y mostrarlo en pantalla.
(Ejemplo: Si ingresa 3, se veria como resultado ”tres”).
==================================================== */

let digito = prompt('Ingrese un numero de un digito');
let numLetras = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve'];

if (digito < 10 && digito > -1) {
    console.log(numLetras[digito]);
}
else{
    console.log('Numero no valido');
}




/* ==================================================== 
12. Realizar un programita que le pida ingresar una frase al usuario y coloque cada letra como elemento de una lista.
==================================================== */

let frase =  "Hola Mundo, esto es javascript" //prompt('Ingrese una frase');
let lista = [];

for (let i = 0; i < frase.length; i++) {
    lista.push(frase[i]);
}
console.log(lista);




/* ====================================================
17. Tirar 20 veces un dado de 6 caras. Mostrar el promedio de esas 20 tiradas. 
===================================================== */


let dado= [];
let i = 0;
let tirada= 0;
let promedio = 0;
while (i < 20) {
    tirada = Math.floor(Math.random() * 6) + 1;
    dado.push(tirada);
    i++;
}
// arrow function
promedio = dado.reduce((a, b) => a + b);
console.log(promedio/20);

/*/
for (let i = 0; i < dado.length; i++) {
    promedio += dado[i];
    
}
/*/

/*/
promedio = dado.reduce(function (a, b) {
    return a + b;});
console.log(promedio/20);
/*/ 




/* ==================================================== 
6) Permita al usuario ingresar el nombre de un archivo, genere un nuevo nombre donde los espacios sean reemplazados por guion bajo y la extension por numerales.
==================================================== */

let archivo = "archivo algoritmos.pdf";
let ext = 0;
let final = 0;
let extension='';

for (let e = 0; e < archivo.length; e++) {
    if (archivo[e] == ' ') {
       archivo= archivo.replace(archivo[e], '_');
    }

    if (archivo[e] == '.') {
        ext = archivo.substring(e+1);
        final = e +1  
    }
}
for (let i = 0; i < ext.length; i++) {
    extension += '#';
}
console.log(archivo.substring(0, final) + extension);




/* ==================================================== 
29. El problema es el siguiente, el usuario deberia poder ingresar la longitud de la base de una piramide y el algoritmo deberia imprimir en pantalla una piriamide de numerales. 
==================================================== */

let pisos = prompt('Ingrese la longitud de la piramide');
let base = Math.round(pisos/2);
const estilo = '#'
let piramide = '';
let space = 0;
let line = 0;

console.log(base);
for (let p = 0; p < base; p++) {
    line= p+1
    space = base-p

    for (let s = 0; s < space; s++) {
        piramide += ' ';
    }
    for (let l = 0; l < line; l++) {
        piramide += estilo + estilo;
    }
    piramide += '\n';
}
console.log(piramide);




/* ====================================================
16. Realizar una funcion que tome dos numeros: a, b y devuelva la cantidad de numeros pares que hay en el intervalo cerrado [a, b]. Controlar que a <= b.
==================================================== */

cont = 0;
function contarPares(a, b) {
    if (a <= b) {
        for (let i = a; i <= b; i++) {
            if (i % 2 == 0) {
                cont++;
            }
        }
    }return cont
}console.log(contarPares(1, 10));





