const pages = document.querySelectorAll('.form-page');
var page_pointer = 0; 
pages[page_pointer].style.display = "block"; 

function next(){ 
	pages[page_pointer].style.display = "none"; 
	page_pointer += 1; 
	pages[page_pointer].style.display = "block"; 
}

function prev(){ 
	pages[page_pointer].style.display = "none"; 
	page_pointer -= 1; 
	pages[page_pointer].style.display = "block"; 
}