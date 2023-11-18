window.onload = function () {
    let out_div = document.getElementById("out_value");
    let age = prompt("How old are you?");
    let years = age * 10;
    let result = "Result is " + years + " years old";
    out_div.innerHTML = result;
}
