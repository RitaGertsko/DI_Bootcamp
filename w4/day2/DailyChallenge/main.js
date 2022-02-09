let userInput = prompt("please insert several words (separated by commas):")
  .split(",")
  .map((word) => word.trim());

let maxLength = 0;
userInput.forEach((word) => {
  maxLength = Math.max(maxLength, word.length);
});

let newArray = new Array(maxLength + 4).fill("*").join("");

let stars = "*".repeat(maxLength + 4);

userInput = userInput.map(
  (word) => word + new Array(maxLength - word.length).fill(" ").join("")
);

console.log(stars);
userInput.forEach((word) => {
  console.log(`*  ${word} *`);
});
console.log(stars);
