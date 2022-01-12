


let sentence = "The movie is not that bad, I like it";

let wordNot = sentence.match("not");

let wordBad = sentence.match("bad");

if (wordBad < wordNot) {
    console.log (sentence.replace('not that bad', 'good'))
} else {
    console.log (sentence)
}