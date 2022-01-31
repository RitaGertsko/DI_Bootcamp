


//Exercise 3 : Transform The Sentence

//1. Create a global variable named allBoldItems.
let allBoldItems = [];
let p = document.querySelector("p");

//2. Create a function called getBold_items() that takes no parameter. 
//This function should collect all the bold items inside the paragraph 
//and assign them to the allBoldItems variable.

function getBold_items(){
    allBoldItems = document.querySelectorAll("strong");
}
getBold_items()

//3. Create a function called highlight() 
//that changes the color of all the bold text to blue.

function highlight(){
    allBoldItems.forEach(element => element.style.color = "blue")
}


//4. Create a function called return_normal() 
//that changes the color of all the bold text back to black.

function return_normal(){
    allBoldItems.forEach(element => element.style.color = "black")
}


//5. Call the function highlight() onmouseover 
//(ie. when the mouse pointer is moved onto the paragraph), 
//and the function return_normal() onmouseout (ie. when the mouse pointer is moved out of the paragraph).

p.addEventListener("mouseover", highlight);
p.addEventListener("mouseout", return_normal);




