function addinfo(id, id2) {
	let mainbody = document.getElementById(id);
	let addinfo = document.getElementById(id2);
	mainbody.style.display = "none";
	addgrades.style.display = "block";
}

function removeinfo(id, id2) {
	let mainbody = document.getElementById(id);
	let addinfo = document.getElementById(id2);
	mainbody.style.display = "block";
	addgrades.style.display = "none";
}
