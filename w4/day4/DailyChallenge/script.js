

//Daily Challenge: 99 Bottles Of Beer


let userAnswer = prompt("Give me a number between 1 and 99");
userAnswer = Number.parseInt(userAnswer);
const numOfBottles = 99;

function song() {
    let lyrics = "";
    let bottelesGoingUp = (numOfBottles - userAnswer);
    let subtractingBottles = (userAnswer - 1);
    let syntax = "";

    while (userAnswer > 0) {
        if(bottelesGoingUp <= 1){
            syntax = "it";
        }else{
            syntax = "them";
        }    

        lyrics += `${userAnswer} bottles of beer on the wall,\n${userAnswer} bottles of beer.\nTake ${bottelesGoingUp} down and pass ${syntax} around,${subtractingBottles} bottles of beer on the wall.`;
        userAnswer--;
        bottelesGoingUp++;
        subtractingBottles--;
        lyrics += "\n\n";
    }

    lyrics += (
    `No more bottles of beer on the wall, \nno more bottles of beer.\nGo to the store and buy some more,\n99 bottles of beer on the wall.`);
    
    return lyrics;
}

console.log(song());


