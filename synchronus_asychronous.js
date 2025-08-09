// console.log("Start");
// setTimeout(()=>console.log("Middle"),2000);     // excutes middile after 2 seconds
// console.log("End");

// ----------------------------------------------- asynchronous execution

// USING setTimeout

// setTimeout(()=>{
//   console.log("This runs  after 10  seconds");      
// },10000);

// setInterval(()=>{
//  console.log("This runs  after 10  seconds");      
// },10000);                                    


// ------------------------------------------------------------------------


// PROMISE

// const myPromise= new Promise((resolve,reject)=>{
//     const success=true;
//     if (success){
//         resolve('Task completed successfully!');

//     }
//     else{
//         reject("Task failed.");
//     }
// });

// myPromise
// .then(message=>console.log(message))
// .catch(error=>console.error(error));

// -------------------------------------------------------------------------------------

// USING THE FETCH API (api - server user connection )

// fetch("https://jsonplaceholder.typicode.com/posts")
// .then(response=>response.json())
// .then(data=>console.log(data))
// .catch(error=>console.error("Error:",error));



// try

// try{
//     let result=10/0;
//     console.log("Result:",result);

// }catch(error){
//     console.error("An error occurred:",error.message);

// }finally{
//     console.log("Execution finished");
// }

// ------------------------------------------------------------------------

// function divide(a,b){
//     if(b===0){
//         throw new Error("Cannot devide by zero");

//     }
//     return a/b;
// }

// try{
//     console.log(divide(10,0));

// }catch(error){
//     console.error(error.message);
// }
