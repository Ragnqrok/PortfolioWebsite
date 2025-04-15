//Hamburger menu Function
function hamburger(){
	var menu = document.getElementById("menu-links");
	var logo = document.getElementById("mobileheader");
	var logoafter = document.getElementById("mobileheader");
	if (menu.style.display === "block" && logo.style.display === "none") {
		menu.style.display = "none";
		logo.style.display = "block";
	} else{
		menu.style.display = "block";
		logo.style.display = "none";
	}
}