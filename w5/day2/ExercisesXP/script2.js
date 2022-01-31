
//Exercise 2 : Work With Forms

//1. Retrieve the form and console.log it.

let htmlForm = document.querySelector("form");
// console.log(htmlForm);


//2. Retrieve the inputs by their id and console.log them.

let idsInputsGroup = document.querySelectorAll("#fname , #lname, #submit");
// console.log(idsInputsGroup);


//3. Retrieve the inputs by their name attribute and console.log them.
const firstNameInput = document.forms[0].elements.fname;

const lastNameInput = document.forms[0].elements.lname;

const submitButton = document.forms[0].elements.submit;
// console.log(firstNameInput, lastNameInput, submitButton);


//4. When the user submits the form (ie. submit event listener)

htmlForm.addEventListener("submit",(event) => {
    event.preventDefault();
    let firstNameInputValue = firstNameInput.value;
    let lastNameInputValue = lastNameInput.value;
    
    if(firstNameInputValue && lastNameInputValue){
        for(let i = 0; i < 2; i++){
            let currentInput = event.target.elements[i];

            const htmlUl = document.querySelector("ul");

            let newLi = document.createElement("li");
            let text = document.createTextNode(currentInput.value);
            newLi.appendChild(text);
            htmlUl.appendChild(newLi);
        }
    }
})








