

//Exercises XP
//Exercise 2 : Users

let ulClassList = document.getElementsByClassName("list");


for (let index = 0; index < ulClassList.length; index++) {
    let currentUl = ulClassList[index];
    let firstUl = ulClassList[0];
    
    currentUl.classList.add("student_list");
    firstUl.classList.add("university", "attendance");

    let bullets = currentUl.getElementsByTagName("li");
    bullets[0].innerText = "Rita";

    for (const bullet of bullets) {
        if (bullet.innerText === "Pete") {
            bullet.innerText = "Richard";
        }
        if(bullet.innerText === "Sarah"){
            bullet.remove();
        }
    }

    let newNode = document.createElement("li");
    newNode.innerText = "Hey Student";
    currentUl.appendChild(newNode);
}



