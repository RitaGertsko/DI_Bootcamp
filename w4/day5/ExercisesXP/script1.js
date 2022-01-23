

//Exercises XP
//Exercise 1 : Change The Navbar

let newDiv = document.getElementById("navBar");
newDiv.setAttribute("id", "socialNetworkNavigation");  

let newly = document.createElement("li");
let newTextNod = document.createTextNode("Logout");

newly.appendChild(newTextNod);

newDiv.children[0].appendChild(newly);


