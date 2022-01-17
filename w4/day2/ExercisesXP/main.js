


//Exercise 1 : part 1:  Information

console.log("-----Exercise 1 part 1-----")

function infoAboutMe() {
    console.log("My name is Rita and Im 27 years old. my favorite color is greeen.");
}

infoAboutMe();


//Part II : function with three parameters

console.log("-----Exercise 1 part 2-----");

function infoAboutPerson(personName, personAge, personFavoriteColor) {
    console.log(`My name is ${personName} Im ${personAge} years old and my favorite color is ${personFavoriteColor}.`);
}

//Call the function twice with the following arguments: infoAboutPerson("David", 45, "blue"),  infoAboutPerson("Josh", 12, "yellow")

infoAboutPerson("David", 45, "blue");

infoAboutPerson("Josh", 12, "yellow");


//Exercise 2 : Tips

console.log("-----Exercise 2-----");

function calculateTip() {
    let bill = prompt("What is the bill amount?");
    bill = Number(bill);
    let tip = "";
    let tipNumber = 0;
    if(bill < 50){
        tip = "20%";
        tipNumber = 0.2;
        console.log(tip);
    }else if(bill >= 50 && bill <= 200){
        tip = "15%";
        tipNumber = 0.15;
        console.log(tip);
    }else {
        tip = "10%";
        tipNumber = 0.1;
        console.log(tip);
    }
    let finallBill = bill + tipNumber;
    console.log(tip, finallBill);
}

calculateTip();


// Exercise 3 : Find The Numbers Divisible By 23

console.log("-----Exercise 3-----");

function isDivisible() {
    let total = 0;
    let indexStr = "";

    for (let i = 0; i < 500; i+=1) {
        if(i % 23 === 0){
            indexStr += i + " ";
            total += i;
        }else{
                continue;
        }
    }
    console.log(`Outcome: ${indexStr}`);
    console.log(`Total: ${total}`);
}

isDivisible();


//Exercise 4 : Shopping List

console.log("-----Exercise 4-----");


let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 
console.log(stock);

let shoppingList = ["banana", "orange", "apple"];

function myBill() {
    let bill = 0;
    for(let product of shoppingList){
        if(stock[product] > 0){
            bill += prices[product];
            stock[product] -= 1;
        }
    }
    return bill;
}

console.log(myBill());
console.log(stock);


//Exercise 5 : What’s In My Wallet ?

console.log("-----Exercise 5-----");

function changeEnough(itemPrice, amountOfChange) {
    let sumChange = amountOfChange[0] * 0.25 + amountOfChange[1] * 0.1 + amountOfChange[2] * 0.05 + amountOfChange[3] * 0.01;
    if(sumChange >= itemPrice){
        return true;
    }
    return false;
    
}

console.log(changeEnough(6, [25, 3, 5, 0]));


//Exercise 6 : Vacations Costs

console.log("-----Exercise 6-----");

function hotelCost() {
    let numberOfNights = prompt("How many nights would you like to stay?");
    while (!isValidNumber(numberOfNights) || numberOfNights === "") {
        numberOfNights = prompt("give me a proper number sir!");
    }
    return numberOfNights * 140;
}


let destination = {
    "london": 183,
    "paris": 220,
    "italy": 170,
}


function planeRideCost() {
    let userDestination  = prompt("where are you going to?");
    while(Number.isInteger(Number(userDestination)) || userDestination === ""){
        userDestination = prompt("give me a proper destination sir!");
    }
    if (destination[userDestination] !== undefined) {
        return destination[userDestination];
    } 
    return 300;
}



function rentalCarCost() {
    let numOfDays  = prompt("For how long would you like to rent a car? (answer should be a number)");

    while(!isValidNumber(numOfDays) || numOfDays === ""){
        numOfDays = prompt("give me a proper number sir!");
    }
    let rentalCost = 0;
    if(numOfDays > 10){
        rentalCost = numOfDays * 40 * 0.9;
    } else {
        rentalCost = numOfDays * 40;
    }
    
    return rentalCost;
}

function totalVacationCost(){
    return `The car cost: $${rentalCarCost()}, the hotel cost: $${hotelCost()}, the plane tickets cost: $${planeRideCost()}.`
}

console.log(totalVacationCost());


//helper function
function isValidNumber(number){
    return Number.isInteger(Number.parseInt(number));
}

