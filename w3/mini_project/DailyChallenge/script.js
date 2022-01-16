

//Daily Challenge: Stars
//Write a JavaScript program that recreates the pattern below.

let print = "*";
for (let i = 0; i < 5; i++) {
    console.log(print);
    print += "*";
}

//using two nested for loops 
for (let c = 0; c < 5; c++) {
    print = "*";
    for (let b = 0; b < c; b++) {
            print += "*";
    }
    console.log(print);
}



