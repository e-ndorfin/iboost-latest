//jQuery time
var current_fs, next_fs, previous_fs; //fieldsets
var left, opacity, scale; //fieldset properties which we will animate
var animating; //flag to prevent quick multi-click glitches

function next() {
    let registercontainer = document.getElementById("regcontainer");
    current_fs = event.target.parentNode.parentNode;
    next_fs = event.target.parentNode.parentNode.nextElementSibling;

    current_fs.style.display = "none";
    next_fs.style.display = "block";

    if (current_fs.id == "regpage") {
        registercontainer.className = "d-flex container login-form";
    }
}

function prev(id) {
    let currentElement = document.getElementById(id);
    let previousElement = currentElement.previousElementSibling;

    currentElement.style.display = "none";
    previousElement.style.display = "block";
}