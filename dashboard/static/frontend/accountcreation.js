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

function prev() {
	let registercontainer = document.getElementById("regcontainer");
	current_fs = event.target.parentNode.parentNode.parentNode.parentNode.parentNode;
	previous_fs = event.target.parentNode.parentNode.parentNode.parentNode.parentNode.previousElementSibling;
	console.log(current_fs);
	console.log(previous_fs);

	current_fs.style.display = "none";
	previous_fs.style.display = "block";

	//If the page before is the register page, center the divs.
	if (previous_fs.id == "regpage") {
		registercontainer.className =
			"d-flex container login-form align-items-center justify-content-center";
	}
}

// $(".previous").click(function () {
// 	if (animating) return false;
// 	animating = true;

// 	current_fs = $(this).parent();
// 	previous_fs = $(this).parent().prev();

// 	//de-activate current step on progressbar
// 	$("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");

// 	//show the previous fieldset
// 	previous_fs.show();
// 	//hide the current fieldset with style
// 	current_fs.animate(
// 		{ opacity: 0 },
// 		{
// 			step: function (now, mx) {
// 				//as the opacity of current_fs reduces to 0 - stored in "now"
// 				//1. scale previous_fs from 80% to 100%
// 				scale = 0.8 + (1 - now) * 0.2;
// 				//2. take current_fs to the right(50%) - from 0%
// 				left = (1 - now) * 50 + "%";
// 				//3. increase opacity of previous_fs to 1 as it moves in
// 				opacity = 1 - now;
// 				current_fs.css({ left: left });
// 				previous_fs.css({ transform: "scale(" + scale + ")", opacity: opacity });
// 			},
// 			duration: 800,
// 			complete: function () {
// 				current_fs.hide();
// 				animating = false;
// 			},
// 			//this comes from the custom easing plugin
// 			easing: "easeInOutBack",
// 		}
// 	);
// });
