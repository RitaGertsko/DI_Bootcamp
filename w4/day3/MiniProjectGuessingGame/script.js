
const numOfIterations = 3;

//Mini Project : Play A Guessing Game
//part 1


function playTheGame() {
    let playerAnswer = confirm("Hi!, Would you like to play?");
    if (!playerAnswer) {
        alert("No problem, Goodbye!");
        return;
    }

    askForValidNumber(); 

    let computerNumber = Math.floor(Math.random() * 11);
    return computerNumber;
}


//part 2:

function test(userNumber, computerRandomNumber) {
    for(let i = 1; i <= numOfIterations; i++){
        if(userNumber === computerRandomNumber){
            alert("WINNER");
            return;
        } else if (userNumber > computerRandomNumber){
            alert("Your number is bigger then the computer's, guess again");
        } else {
            alert("Your number is smaller then the computer's, guess again");
        }
        //doesnt need to ask in last iteration
        if (i < numOfIterations){
            userNumber = askForValidNumber();
        }
    }
    alert("out of chances");
}


//helper function
function isValidNumber(number){
    let validNumber = false;
    number = parseInt(number);

    if (Number.isInteger(number) && number >= 0 && number <= 10){
        validNumber = true;
    }
  
    return validNumber;
}

function askForValidNumber(){
    let playerNum = prompt("Please Give me a Number between 0 and 10 only!");

    while(!isValidNumber(playerNum)){
        playerNum = prompt("invalid number, please enter a number  between 0 and 10 only!");
    }
    return Number.parseInt(playerNum);
}
