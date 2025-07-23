let employee=[
    {name: 'Shein', age: 28},
    {name: 'Priya', age: 38},
    {name: 'Merlyn', age: 30},
]
let a=employee[0].age;
// console.log(a);
for (let i=0;i<employee.length;i++){
    if (employee[i].age < a){
        a=employee[i].age 
        console.log(employee[i])
    }
}
