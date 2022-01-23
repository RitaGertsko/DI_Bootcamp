

//Exercise 3 : Users And Style
//

const htmlDiv = document.querySelector('div');

htmlDiv.style.padding = '5px';
htmlDiv.style.background  = 'lightblue';


const liListes = document.getElementsByTagName('li');
let firstLi = liListes[0];
let scondLi = liListes[1];

firstLi.style.display = 'none';
scondLi.style.border = '2px solid black';

let bodyStyle = document.querySelector('body');
bodyStyle.style.fontSize = '30px';


