function addreflection(id, id2) {
    let mainbody = document.getElementById(id);
    let addreflection = document.getElementById(id2);
    mainbody.style.display = "none";
    addreflection.style.display = "block";
}

function removereflection(id, id2) {
    let mainbody = document.getElementById(id);
    let addreflection = document.getElementById(id2);
    mainbody.style.display = "block";
    addreflection.style.display = "none";
}

