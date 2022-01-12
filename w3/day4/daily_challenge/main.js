


let sentence = "The movie is not that bad, I like it";

let wordNot = sentence.indexOf("not");

let wordBad = sentence.indexOf("bad");

if (wordBad > wordNot) {
    let toRemove = sentence.substring(wordNot, wordBad + 3);
    console.log (sentence.replace(toRemove, 'good'))
} else {
    console.log (sentence)
}