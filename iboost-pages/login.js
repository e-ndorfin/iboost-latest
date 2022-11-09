// disables spaces in the signup
$("input#username").on({
	keydown: function (e) {
		if (e.which === 32) return false;
	},
	change: function () {
		this.value = this.value.replace(/\s/g, "");
	},
});

$("input#email").on({
	keydown: function (e) {
		if (e.which === 32) return false;
	},
	change: function () {
		this.value = this.value.replace(/\s/g, "");
	},
});
