using System;

// imprimir "hola mundo" en consola
Console.WriteLine("Hola Mundo");

/*/====================================================
7. Permitir ingresar al usuario un numero de un digito. Controlando se haya ingresado dicho
numero de no mas de 1 digito de longitud, pasarlo a letras y mostrarlo en pantalla.
(Ejemplo: Si ingresa 3, se veria como resultado ”tres”).
====================================================/*/

int digito = Convert.ToInt32(Console.ReadLine());
string[] numLetras = new string[]{"cero","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve"};

if (digito < 10 && digito > -1) {
    Console.WriteLine(numLetras[digito]);
} else {
    Console.WriteLine("Numero no valido");
}




/*/==================================================== 
12. Realizar un programita que le pida ingresar una frase al usuario y coloque cada letra
como elemento de una lista.
====================================================/*/
string frase ="Hola Mundo, esto es csharp";
char [] lista = frase.ToCharArray(0,frase.Length);

/*/
for (int ctr = 0; ctr < lista.Length; ctr++)
{
    Console.WriteLine("   {0}: {1}", ctr, lista[ctr]);
}
/*/



/*/ ====================================================
17. Tirar 20 veces un dado de 6 caras. Mostrar el promedio de esas 20 tiradas. 
=====================================================/*/
Random rnd = new Random();
int[] dado= new int[20];
int i = 0;
float promedio = 0;
int tirada= 0;

while (i < 20) {
    tirada = (int) rnd.Next(1,7);
    dado[i] = tirada;
    i++;
}
promedio = dado.Sum()/20;
Console.WriteLine("El promedio de las 20 tiradas es: {0}", promedio);




/*/ ==================================================== 
6) Permita al usuario ingresar el nombre de un archivo, genere un nuevo nombre donde los
espacios sean reemplazados por guion bajo y la extension por numerales.
==================================================== /*/

string archivo = "archivo algoritmos.pdf";
int final = 0;
string extension ="";

for (int e = 0; e < archivo.Length; e++){

    if (archivo[e] == '.') {
        final = e+1;
    }
}
for (i = 0; i < archivo.Length-final; i++) {
    extension += '#';
}

archivo = archivo.Substring(0,final);
Console.WriteLine(archivo.Replace(' ','_')+extension);



/*/==================================================== 
29. El problema es el siguiente, el usuario deberia poder ingresar la longitud de la base de
una piramide y el algoritmo deberia imprimir en pantalla una piriamide de numerales. 
====================================================/*/

int pisos = Convert.ToInt32(Console.ReadLine());
string piramide = "";
int space = 0;
int line = 0;


for (i = 0; i < pisos; i++) {
    line= i;
    space = pisos-i;
    
    for (i = 0; i < space; i++) {
        piramide += ' ';
    }
    for (i= 0; i < line; i++) {
        piramide += "#" + "#";
    }
    piramide += '\n';

}
Console.WriteLine(piramide);


/*/====================================================
16. Realizar una funcion que tome dos numeros: a, b y devuelva la cantidad de numeros pares
que hay en el intervalo cerrado [a, b]. Controlar que a <= b.
====================================================/*/

int cont = 0;
void contarPares(int a, int b) {
    if (a <= b) {
        for (i = a; i <= b; i++) {
            if (i % 2 == 0) {
                cont++;
            }
        }
    }
    Console.WriteLine(cont);
}
contarPares(1,10);
