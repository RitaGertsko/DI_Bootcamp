

//Exercice 4 : Volume Of A Sphere


function volume_sphere(e) {
    e.preventDefault()
    let volume;
    let radius = document.getElementById('radius').value;
    radius = Math.abs(radius);
    volume = (4 / 3) * Math.PI * Math.pow(radius, 3);
    volume = volume.toFixed(4);
    document.getElementById('volume').value = volume;
    return;
}

document.querySelector("input[type='submit']").addEventListener("click", volume_sphere);








