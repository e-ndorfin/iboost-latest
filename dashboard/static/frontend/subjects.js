const iconDict = {'english': 'bi bi-journals', 'chinese': 'bi bi-translate', 'math': 'bi bi-calculator', 'science': 'bi bi-virus', 'individualsandsocieties': 'bi bi-globe', 'design': 'bi bi-rulers', 'music': 'bi bi-music-note-beamed', 'mypphysicaleducation': 'bi bi-stopwatch', 'art': 'bi bi-brush', 'computerscience': 'bi bi-cpu'};

// Select all <a> elements with class "subject-text"
const subjectLinks = document.querySelectorAll('.subject-text');

// Loop through each element and add the classes
subjectLinks.forEach(link => {
var subject = link.textContent.toLowerCase().trim().replaceAll(" ", ''); 
if (iconDict[subject]) {
    var classesToAdd = iconDict[subject].split(' ');
    link.classList.add(...classesToAdd);
}
});