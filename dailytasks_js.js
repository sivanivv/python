//day_37

// let name = 'Sivani';
// let age = 20;
// let hobby = 'Drawing';
// console.log(`Hi, I'm ${name}, ${age} years old, and I love ${hobby}. `);

// let n = 122;
// let o = 1;
// console.log(n + o);

//-------------------------------------------------------------------------------------

//day_38

// const prompt = require('prompt-sync')();
// let a = prompt("Enter a number: ")
// if (a == 0) {
//     console.log("The number is ZERO!!");
// }
// else if (a < 0) {
//     console.log("The number is NEGATIVE!!");
// }
// else {
//     console.log("The number is POSITIVE!!");
// }


// const prompt = require('prompt-sync')();
// let mark = prompt("Enter the Mark: ")

// switch (true) {
//     case mark >= 90 && mark <= 100:
//         console.log('Grade is A');
//         break;
//     case mark >= 80 && mark < 90:
//         console.log('Grade is B');
//         break;
//     case mark >= 70 && mark < 80:
//         console.log('Grade is C');
//         break;
//     case mark >= 60 && mark < 70:
//         console.log('Grade is D');
//         break;
//     case mark >= 0 && mark < 60:
//         console.log('Grade is F');
//         break;

//     default:
//         console.log('Invalid mark')
// }
//------------------------------------------------------

//day_39

// let fruits = ['Peach', 'Kiwi', 'Banana', 'Apple', 'Blueberry'];
// for (let i = 0; i < fruits.length; i++) {
//     if (fruits[i].length > 5) {
//         console.log(fruits[i])
//     }
// }


// let employee = [
//     { name: 'Mary', age: 63 },
//     { name: 'Supriya', age: 46 },
//     { name: 'Harry', age: 27 },
// ];
// let a = employee[0];
// for (let i = 0; i < employee.length; i++) {
//     if (employee[i].age < a.age) {
//         a = employee[i];
//     }
// }
// console.log(a.name);

//---------------------------------------------------------

//day_40
const button = document.getElementById("addButton"); 
button.addEventListener("click", () => { const newItem = document.createElement("li");
 newItem.innerText = "New Item"; 
 document.querySelector("ul").appendChild(newItem); });
