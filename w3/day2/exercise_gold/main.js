

//Exercises XP Gold
//Exercise 1 : Favorite Color
let me = ["my","favorite","color","is","blue"];
let meJoin = me.join(" ");

console.log(meJoin)


//Exercise 2 : Mixup
//1.
let str1 = "mix";
let str2 = "pod";

//2.
let mix = str1.slice(0,1) + str2.slice(0,1);
console.log(mix)

//3.
let thirdWord = str1.concat(" ", str2);

//4.
console.log(thirdWord)


//Exercise 3 : Calculator
//1.-2.
let num1 = prompt("Give me a number, any kind of number that you like");
    
console.log(typeof(num1))
let numStringToNum1 = num1 - "1";
    console.log(typeof(numStringToNum1))

//let numStringToNum2 = Number(num1);
    //console.log(typeof(numStringToNum2))  I found this method in Stock Overflow.

//3.-4.
let num2 = prompt("Give me another number please");

//5.
alert(`This is the SUM of all the numbers you have given: ${Number(num1)+Number(num2)}`)







