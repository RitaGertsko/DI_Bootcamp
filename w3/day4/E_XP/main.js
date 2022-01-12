

//Exercises XP
//Exercise 1: 
let x = 10;
let y = 8;

if (x > y) {
    console.log('x is bigger!')
} 

else {
     console.log('y is bigger!!')
}


//Exercise 2:
//1.
let newDog = 'Chihuahua';

//2.
console.log (newDog.length)

//3.
console.log (newDog.toUpperCase())

console.log (newDog.toLowerCase())

//4.
if (newDog == 'Chihuahua') {
    console.log('I love Chihuahuas, it`s my favorite dog breed')
} 

else {
    console.log('I dont care, I prefer cats')
}


//Exercise 3:
1.
let number = prompt('What number are you thinking of?');

//2.
if (number % 2 == 0) {
    console.log(number + ' is an even number')
} 

else {
    console.log(number + ' is an odd number')
}


//Exercise 4:
let users = ["Lea123 ", "Princess45 ", "cat&doglovers ", "helooo@000 "];

if (users.length === 0) {
    console.log(' no one is online')
} 

else if (users.length === 1) {
    console.log(users[0] + ' is online')
} 

else if (users.length === 2) {
    console.log(users[0] + users[1] + ' are online')
} 

else {
    console.log(users[0] + users[1] + 'and 2 more are online')
} 
