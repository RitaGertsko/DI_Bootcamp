

//Exercises XP
//Exercise 1 : Change The Article

//Using a DOM property, retrieve the h1 and console.log it.

const retrivingH1 = document.querySelector("h1");
// console.log(retrivingH1);

//Using DOM methods, remove the last paragraph in the <article> tag.

let lastParInTheArticle = document.querySelector("article p:last-child");
lastParInTheArticle.parentNode.removeChild(lastParInTheArticle);

//Add a event listener which will change the background color of the h2 to red, when it’s clicked on.

const h2Var = document.querySelector("h2");

h2Var.addEventListener("click", () => h2Var.style.background = "red")


//Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).

const h3Var = document.querySelector("h3");

h3Var.addEventListener("click", () => h3Var.style.display = "none")

//Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.

const articalHtml = document.querySelector("article");

let htmlButton = document.createElement("button");
htmlButton.innerText = "Make all article text bold!";

htmlButton.setAttribute("onclick","makesParagraphsBolder()");

articalHtml.appendChild(htmlButton);

function makesParagraphsBolder(){
    let allParGroup = document.querySelectorAll("p");

    for(let i = 0; i < allParGroup.length; i++){
    allParGroup[i].classList.add("bolder");
    }
    return 
}


