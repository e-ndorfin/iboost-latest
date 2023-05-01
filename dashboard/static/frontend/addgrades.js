function addgrades(id, id2) {
	let mainbody = document.getElementById(id);
	let addgrades = document.getElementById(id2);
	mainbody.style.display = "none";
	addgrades.style.display = "block";
}

function removegrades(id, id2) {
	let mainbody = document.getElementById(id);
	let addgrades = document.getElementById(id2);
	mainbody.style.display = "block";
	addgrades.style.display = "none";
}

function test() {
	console.log("test");
}
