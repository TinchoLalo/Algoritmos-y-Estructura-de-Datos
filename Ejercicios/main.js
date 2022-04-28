/*/ 1) Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos/*/

const max = (num1, num2) => {
    if(num1 > num2) return num1
    else return num2   
}
console.log(max(10, 20));

/*/ 2) Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos. /*/

const max3 = (n1,n2,n3) => {
    if(n1 >= n2 && n1 >= n3) return n1
    if(n2>=n1 && n2>= n3) return n2
    else return n3
}
console.log(max3(2,5,4));

/*/ 3) Definir una función que calcule la longitud de una lista o una cadena dada. /*/

let cadena ='Hola mundo, esto es JavaScript';
let lista = [1,'hola',30,'mundo'];

const longitud = (cadena,lista)=>{
    cont =0;
    for (i=0;i < cadena.length; i++){
        cont+=1
    }
    return 'cadena: '+cont + ' lista: '+ lista.length

}
console.log(longitud(cadena,lista));


/*/ 4) Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False. /*/
let ct = 'c';
ct = ct.toLocaleLowerCase()
const vocal = (ct) => {
    if (ct == 'a' || ct =='e' || ct=='i' || ct == 'o' || ct=='u'){
        return true
    }
    else return false
}
console.log(vocal(ct))

/*/ 5) Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.  /*/ 

let liste = [1,2,3,4]
// sumar
const sum = (liste)=> {
    let suma = 0;
    for(i=0; i<liste.length; i++){
        suma += liste[i]
    }
    return suma
}
console.log(sum(liste))
// multiplicar
const multi = (liste)=> {
    let mult = 1;
    for(i=0; i<liste.length; i++){
        mult *= liste[i]
    }
    return mult
}
console.log(multi(liste))


/*/ 6) Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse /*/
const inversa= ()=>{
    let cadena = 'estoy probando'
    let cadena2 = ''
    for(i=cadena.length-1; i>=0; i--){
        cadena2 += cadena[i]
    }
    return cadena2
}
console.log(inversa())

/*/ 7) Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True. /*/

const es_palindromo=()=>{
    let cadena = 'neuquen'
    let cadena2 = ''
    for(i=cadena.length-1; i>=0; i--){
        cadena2 += cadena[i]
    }
    if (cadena==cadena2)return 'es palindromo'
    else return 'No es palindromo'
}
console.log(es_palindromo());

/*/ 8) Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado. /*/


const superposicion=()=>{
    let lista1 = [1,2,3,4,5]
    let lista2 = [6,7,8,4,10]
    let lista3 = []
    for (i=0; i<lista1.length; i++){
        for(j=0; j<lista2.length; j++){
            if(lista1[i]==lista2[j]){
                lista3.push(lista1[i])
            }
        }
    }
    if(lista3.length>0){
        return true
    }
    else return false
}
console.log(superposicion())


/*/ 9)  Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx"
/*/

function caracter(){
    let n = 5
    let caracter = '+'
    let cadena = ''
    for(i=0; i<n; i++){
        cadena += caracter
    }
    return cadena
}
console.log(caracter())


/*/ 10)  Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. /*/

const procedimiento=()=>{
    let lista = [1,4,6]
    let lista2=[]
    for(i=0; i<lista.length; i++){
        lista2[i]= ''
        for(j=0; j<lista[i]; j++){
            lista2[i] += '*'
        }
        console.log(lista2[i])
    }
};procedimiento()

