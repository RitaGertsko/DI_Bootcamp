// Exercise 1:

let favFood = 'sushi';
let favMeal = 'breakfast';
let sentence = ' I eat ' + favFood + ' at every ' + favMeal;

console.log (sentence)

// Exercise 2:
//part 1:
//1.

let watchedSeries = [" black mirror ", " money heist ", " the big bang theory "];
let watchedSeriesLength = (watchedSeries.length);

console.log (watchedSeriesLength)

//2.

let myWatchedSeries = 'those are some of the series I watched: ' + watchedSeries[0] + ',' + watchedSeries[1] + ' and ' + watchedSeries[2] + '.';

console.log (myWatchedSeries)

console.log ('I wached ' + watchedSeriesLength + ' series, for example ' + myWatchedSeries)


//part 2
//1.
watchedSeries[2] = "friends ";

console.log (watchedSeries)

//2.
watchedSeries.push("House M.D.")

console.log(watchedSeries)

//3.
watchedSeries.unshift("Criminal Minds ")

console.log(watchedSeries)

//4.
watchedSeries.splice(1,1)

console.log(watchedSeries)

//5.
let thirdLetter = watchedSeries[1][3];

console.log(thirdLetter)

//6.
console.log(watchedSeries)


// Exercise 3:
let celsiusTemperature = 30;
let fahrenheitTemperature = celsiusTemperature / 5 * 8 + 32; 

console.log(fahrenheitTemperature)


// Exercise 4:
let c;
let a = 34;
let b = 21;

console.log(a+b) 
//1. first expression
// Prediction: it will equal 55. that will be the output.
// Actual: indeed

a = 2;

console.log(a+b) 
//2. second expression
// Prediction: the output will be 23.
// Actual: indeed

// 3. What is the value of c? - there is no value we didn't gave it any value.


// 4. Analyse the code below, what will be the outcome? 

console.log(3 + 4 + '5');   
//Prediction: the outcame will be error.
// Actual: 75. 7 is a number and 5 is a string. oopsy :) got it!.


// Exercise 5:

typeof(15)
// Prediction: number
// Actual: indeed

typeof(5.5)
// Prediction: number
// Actual: indeed

typeof(NaN)
// Prediction: number
// Actual: indeed

typeof("hello")
// Prediction: string
// Actual: indeed

typeof(true)
// Prediction: boolean
// Actual: indeed

typeof(1 != 2)
// Prediction: Boolean
// Actual: indeed

"hamburger" + "s"
// Prediction: hamburgers
// Actual:

"hamburgers" - "s"
// Prediction: NaN
// Actual: indeed

"1" + "3"
// Prediction: 13 as a srting.
// Actual: indeed

"1" - "3"
// Prediction: NaN
// Actual: -2 . but why? (-__-)

"johnny" + 5
// Prediction: johnny5
// Actual: indeed

"johnny" - 5
// Prediction: NaN
// Actual: indeed

99 * "hello"
// Prediction: NaN
// Actual: indeed

1 != 1
// Prediction: false
// Actual: indeed

1 == "1"
// Prediction: false
// Actual: true. (=__=) 

1 === "1"
// Prediction: false
// Actual: indeed



//Exercise 6:


5 + "34"
// Prediction: 534
// Actual: indeed

5 - "4"
// Prediction: 1
// Actual: indeed

10 % 5
// Prediction: 0. I cheated I read about it on Google 
// Actual: indeed

5 % 10
// Prediction: 5
// Actual: indeed

"Java" + "Script"
// Prediction: javascript
// Actual: indeed

" " + " "
// Prediction: empty space
// Actual: indeed

" " + 0
// Prediction: 0
// Actual: indeed

true + true
// Prediction: true 
// Actual: 2.  oh I forgot about that. ok, got it!

true + false
// Prediction: 1
// Actual: indeed

false + true
// Prediction: 1
// Actual: indeed

false - true
// Prediction: -1
// Actual: indeed

!true
// Prediction: false
// Actual: indeed

3 - 4
// Prediction: -1
// Actual: indeed

"Bob" - "bill"
// Prediction: NaN
// Actual: indeed








