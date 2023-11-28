function addition() {

    var inputValue1 = document.getElementById('value1').value;
    var inputValue2 = document.getElementById('value2').value;
    var resultat = document.getElementById('resultat');
    resultat.innerText = +inputValue1 + +inputValue2;

}

function substraction() {

    var inputValue1 = document.getElementById('value1').value;
    var inputValue2 = document.getElementById('value2').value;
    var resultat = document.getElementById('resultat');
    resultat.innerText = +inputValue1 - +inputValue2;

}

function multiplication() {

    var inputValue1 = document.getElementById('value1').value;
    var inputValue2 = document.getElementById('value2').value;
    var resultat = document.getElementById('resultat');
    resultat.innerText = +inputValue1 * +inputValue2;

}

function division() {

    var inputValue1 = document.getElementById('value1').value;
    var inputValue2 = document.getElementById('value2').value;
    var resultat = document.getElementById('resultat');
    resultat.innerText = +inputValue1 / +inputValue2;

}