//Hamburger menu Function
function hamburger(){
	var X = document.getElementById("menu-iconX");
	var menu = document.getElementById("menu-links");
	var logo = document.getElementById("mobileheader");
	var logoafter = document.getElementById("mobileheader");
	function logostyle(){
		logo.style.display="block"
	}
	
	if (menu.style.display === "block" && logo.style.display === "none") {
		menu.classList.add("secondClass");
		setTimeout (logostyle, 490)
		X.style.display = "none";
	} else{
		X.style.display = "block";
		menu.style.display = "block";
		logo.style.display = "none";
		menu.classList.remove("secondClass");
	}
}
