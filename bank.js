// const prompt = require('prompt-sync')();

// let data = [];

// let option;

// while (option !== 5) {
//     let option = prompt('What is your need?  \n1.Create account\n2.Deposit money\n3.Withdrew money\n4.Delete money\nEnter your option: ');

//     if (option == 1) {
//         let account = {};

//         let name = prompt('Enter your name: ');
//         account.acc_name = name;


//         let id = prompt('Enter your ID: ');
//         let yes = Unique(id);

//         function Unique(id) {
//             for (let i = 0; i < data.length; i++) {
//                 if (data[i].acc_id == id) {
//                     return true; 
//                 }
//             }
//             return false; 
//         }

//         if (id < 0 || yes == true) {
//             console.log('Invalid ID!! Try again!');
//             continue;
//         } else {
//             account.acc_id = id;
//         }

//         let balance = prompt('Enter your initial Deposit: ');
//         if (balance <= 0) {
//             console.log('Enter valid amount!!');
//             continue;
//         } else {
//             account.acc_bal = balance;
//         }

//         data.push(account);
//         console.log("Account created successfully!");



//     }
//     else if (option == 2) {
//         let id = prompt('Enter your ID: ');
        
//         let dep=prompt('Enter the amount you want to deposit: ');

//         let yess=Unique(id);
//         // if (dep < 0 || yess == true) {
//         //     console.log('Invalid ID!! Try again!');
//         //     continue;
//         // } else {
//             account.acc_bal+=dep;
//         }


//     }
    
    
    
    
    
//     else if (option == 3) {
//         console.log(data);
//     }
// }