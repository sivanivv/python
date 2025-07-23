// ARRAYS

// let fruits=["apple","fig","cherry"];
// console.log(fruits);


//accessing array elements

// console.log(fruits[1]);


//updating array elements

// let fruits=["apple","fig","cherry"];
// fruits[2]="pear"
// console.log(fruits);

// -----------------------------------------------------------------


// ARRAY METHODS

// 1. adding and removing

// PUSH(adds to the end):

// let fruits=["apple","fig","cherry"];
// fruits.push("orange")
// console.log(fruits);

// POP(removes from  end):
// fruits.pop()
// console.log(fruits);

// UNSHIFT(adds to the beginning):

// let fruits=["apple","fig","cherry"];
// fruits.unshift("strawberry")
// console.log(fruits);

// SHIFT(removes from the beginning):
// let fruits=["apple","fig","cherry"];
// fruits.shift()
// console.log(fruits);

//--------------------------------------------------------------------

//for 
// let fruits=["apple","fig","cherry"];
// for(let i=0;i<fruits.length;i++){
//     console.log(fruits[i]);
// }

// forEeach

// fruits.forEach(fruit=>console.log(fruit));

// write a program to print only fruits with more than 5 letters using loop

// let fruits=['Apple','Pineapple','Peach','Grapes','Strawberry'];
//  for(let i=0;i<fruits.length;i++){
//     if (fruits[i].length>5){
//         console.log(fruits[i])
//     }
//  }


//-----------------------------------------------------------------------------------------------------

// OBJECTS 

// let person={
//     name:'Alondra',
//     age:42,
//     isStudent:true
// };
// console.log(person);

//Write a program to find the name of the youngest employee in an array of objects

let employee=[
    {name: 'Shein', age: 28},
    {name: 'Priya', age: 38},
    {name: 'Merlyn', age: 20},
];
let a=employee[0];
// console.log(a);
for (let i=0;i<employee.length;i++){
    if (employee[i].age < a.age){
        a=employee[i];
    }
}
console.log(a);