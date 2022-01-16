

//Exercises XP
//Exercise 1
//Write code to remove “Greg” from the people array.
let people = ["Greg", "Mary", "Devon", "James"];

people.shift();
console.log(people)


//Write code to replace “James” to “Jason”.
people.splice(2, 1, "Jason");
console.log(people)


//Write code to add your name to the end of the people array.
people.push("Rita");
console.log(people)


//Write code that console.logs Mary’s index.
console.log(people.indexOf("Mary")) //or
let maryIndex = people.indexOf("Mary");
console.log(maryIndex)


//Write code to make a copy of the people array using the slice method.
// The copy should NOT include “Mary” or your name.
// Hint: remember that now the people array should look like this let people = ["Mary", "Devon", "Jason", "Yourname"];
// Hint: Check out the documentation for the slice method
let newPeople = people.slice(1, 3);
console.log(newPeople)


//Write code that gives the index of “Foo”. Why does it return -1 ?
console.log(people.indexOf("foo")) // it return -1 because "Foo" doesnt exist in the array. and the computer answer to it is -1.


//Create a variable called last which value is the last element of the array.
// Hint: What is the relationship between the index of the last element in the array and the length of the array?
let last = people[3];
console.log(last)



// Part 2
//Using a loop, iterate through the people array and console.log each person. 
for(let person in people){
    console.log(people[person])
}

//Using a loop, iterate through the people array and exit the loop after you console.log “Jason” .
// Hint: take a look at the break statement in the lesson.

for(let index in people) {
    if(people[index]==="Jason"){
        break;
    }
    console.log(people[index]);
}




//Exercise 2
//Create an array called colors where the value is a list of your five favorite colors.
//Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .
let myColors = ["green", "black", "blue", "white", "lilac"];

for (let colorsIndex in myColors){
    i = Number(colorsIndex) + 1;
    console.log(`My #${i} choice is ${myColors[colorsIndex]}`)
}


// Exercise 3
// Prompt the user for a number.
// Hint : Check the data type you receive from the prompt (ie. Use the typeof method)

let user = prompt("give me a number");

if(isNaN(user)){
    console.log("its a String")
}else if(Number(user)){
    console.log("Its a Number")
}
else {
    console.log("Try again...")
}

// While the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?

let input = prompt("insert a number bigger than 10!");

while(isNaN(Number.parseInt(input)) || Number(input) <= 10){
    input = prompt("Try again...")
} if(Number(input) > 10){
    alert("Thanks!")
}




//Exercise 4
//Copy and paste this object to your Javascript file.
let building = {
    numberOfFloors : 4,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
    },
}


//Console.log the number of floors in the building.
console.log(`There are ${building.numberOfFloors} floor in the building`)

//Console.log how many apartments are on the floors 1 and 3.
console.log(`On the first floor the are ${building.numberOfAptByFloor["firstFloor"]} apartments and on the third floor the are ${building.numberOfAptByFloor["thirdFloor"]} apartments`)

//Console.log the name of the second tenant and the number of rooms he has in his apartment.
console.log(`This tenan name is ${building.nameOfTenants[1]} and they have ${building.numberOfRoomsAndRent.dan[0]} rooms in theirs apartment`);

//Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.

let sum = building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1];
console.log(sum)

if(sum > building.numberOfRoomsAndRent.dan[1]){
    building.numberOfRoomsAndRent.dan[1] = 1200;
    console.log(building.numberOfRoomsAndRent.dan[1])
} else {
    console.log(sum)
}




//Exercise 5
//Create an object called family with a few key value pairs.
let family = {
    dad: 57,
    mam: 55,
    sister: 25,
    brother: 27
};

//Using a for loop, console.log the keys of the object.
for (let members in family){
    console.log(members);
}

//Using a for loop, console.log the values of the object.
for (let membersAge in family){
    console.log(family[membersAge]);
} 


//Exercise 6
//Given the object below and using a for loop, console.log “my name is Rudolf the raindeer”
let details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
} 

for (let str in details) {
    console.log(`${str} ${details[str]}`); 
} //or

let strToPrint = "";
for (let sentence in details) {
    strToPrint += `${sentence} ${details[sentence]}`;
};
console.log(strToPrint); //I wasn't sure how I was supposed to present it.



// //Exercise 7
let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

// //A group of friends have decided to start a secret society. 
// //The society’s name will be the first letter of each of their names sorted in alphabetical order.

names.sort();
let secretSocietyName = "";
for (let i=0; i < names.length; i++) {
    let firstLetter = names[i];
    secretSocietyName += firstLetter.slice(0,1);
}

console.log(secretSocietyName);
