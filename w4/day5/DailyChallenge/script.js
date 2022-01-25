

//Daily Challenge: Planets
//Create an array which value is the planets of the solar system.

let planets = [
    "mercury",
    "venus",
    "earth",
    "mars",
    "jupiter",
    "saturn",
];

//For each planet in the array, create a "div" using createElement. This div should have a class named "planet".

planets.forEach(function(){
    let planestDiv = document.createElement("div");
    planestDiv.classList.add("planet");

    //Finally append each "div" to the "section" in the HTML (presented below).
    let section = document.getElementsByTagName("section")[0];
    section.appendChild(planestDiv);
});


//Each planet should have a different background color. (Hint: add a new class to each planet).

let colors = [
    "red",
    "orange",
    "blue",
    "pink",
    "brown",
    "purple",
];

listOfPlanetClasses = document.getElementsByClassName("planet");

for (let i = 0; i < listOfPlanetClasses.length; i++) {
    listOfPlanetClasses[i].style.backgroundColor = colors[i];
}




