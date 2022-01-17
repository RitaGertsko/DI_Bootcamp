let userInput = prompt("please insert several words (separated by commas)");
let wordArray = userInput.split(",");

let maxLength = 0;

for(let word of wordArray){
    if (maxLength < word.length){
        maxLength = word.length;
    }
}

console.log("*".repeat(maxLength + 4));
for(let word of wordArray){
    console.log(`* ${word}  *`)
}

console.log("*".repeat(maxLength + 4));

