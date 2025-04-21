//Hamburger menu Function
function hamburger(){
	var menu = document.getElementById("menu-links");
	var logo = document.getElementById("mobileheader");
	var logoafter = document.getElementById("mobileheader");
	function logostyle(){
		logo.style.display="block"
	}
	
	if (menu.style.display === "block" && logo.style.display === "none") {
		menu.classList.add("secondClass");
		setTimeout (logostyle, 499)
	} else{
		menu.style.display = "block";
		logo.style.display = "none";
		menu.classList.remove("secondClass");
	}
}
