// variables a utilizar
let clave = document.querySelector('#clave');
let nombre = document.querySelector('#nombre');
let des = document.querySelector('#des');
let precio = document.querySelector('#precio');
let tipo = document.querySelector('#tipo');
let edad = document.querySelector('#edad');

// cantidad de planes 
let count =0;
let p = [];

// clase plan 
class Plan {
    constructor(clave, nombre, des, precio, tipo1, edad1) {
        this.clave = clave;
        this.nombre = nombre;
        this.des = des;
        this.precio = precio;
        this.tipo = tipo1;
        this.edad = edad1;
    }
}


// tipo de plan
const tipoPlan = {
    1: 'Básico', 
    2: 'Mantenimiento', 
    3: 'Deporte',
    4: 'Premium',
    5: 'VIP',
    6: 'VIP+',
    7: 'Profecional',
    8: 'Particular',
    9: 'Empresarial',
    10: 'Empresarial+'
}

// edad recomendada
const edadRecomendada = {
    1: '7 años a 13 años',
    2: '14 años a 17 años',
    3: '18 años a 24 años',
    4: '25 años a 35 años',
    5: 'mayores de 35 años'
}


const crear = document.querySelector('#crear');

crear.addEventListener('click', (e) => {
    e.preventDefault();

    let tipo1 = tipoPlan[tipo.value];
    let edad1 = edadRecomendada[edad.value];

    // verificar si ya existe ese plan
    for (let i = 0; i < p.length; i++) {
        if (p[i].clave == clave.value || p[i].nombre == nombre.value) {
            alert('El plan ya existe');
            return;
        }
    }

    // agregar plan
    p[count] = new Plan(clave.value, nombre.value, des.value, precio.value, tipo1, edad1);



    const planes = document.getElementById('planes');

    // mostra los planes
    planes.innerHTML += `
    <table class="table" id="${p[count].clave}">
        <tr>
            <td>${p[count].clave}</td>
        <tr>
        <tr>
            <td>${p[count].nombre}</td>
        <tr>
        <tr>
            <td>${p[count].des}</td>
        <tr>
        <tr>
            <td>${p[count].precio}</td>
        <tr>
        <tr>
            <td>${p[count].tipo}</td>
        <tr>
        <tr>
            <td>${p[count].edad}</td>
        <tr>
    </table>`;



    // resetear 
    clave.value = '';
    nombre.value = '';
    des.value = '';
    precio.value = '';
    document.querySelector('#tipo').value = '';
    document.querySelector('#edad').value = '';
    count += 1; // sumar la cantidad de planes

});



// Buscar plan 

const buscar = document.querySelector('#search');

buscar.addEventListener('click', (e) => {
    e.preventDefault()

    let buscar = document.querySelector('#buscar').value;
    let filtro = document.querySelector('#filtro').value;


    if (filtro == "clave"){
        for (let i = 0; i < p.length; i++) {
            if (p[i].clave == buscar) {
                alert('El plan ya existe');
                return;
            }
        }
    }

    if (filtro == "nombre"){
        for (let i = 0; i < p.length; i++) {
            if (p[i].nombre == buscar) {
                alert('El plan ya existe');
                return;
            }
        }
    }

    if (filtro == "precio"){
        for (let i = 0; i < p.length; i++) {
            if (p[i].precio == buscar) {
                alert('El plan ya existe');
                return;
            }
        }
    }

    if (filtro == "tipo"){
        for (let i = 0; i < p.length; i++) {
            if (p[i].tipo == buscar) {
                alert('El plan ya existe');
                return;
            }
        }
    }

    if (filtro == "edad"){
        for (let i = 0; i < p.length; i++) {
            if (p[i].edad == buscar) {
                alert('El plan ya existe');
                return;
            }
        }
    }
});