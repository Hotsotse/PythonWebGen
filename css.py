import os
import sys

def createcss(colorscheme):
    sidebar='#171717'
    header='#2c3e50'
    background='#95a5a6'
    box='#2980b9'
    print "0"
    
    os.mkdir("styles", 0755 );
    os.chdir("styles")
    css = open("global.css", 'a')
    cssContents="""@import url("http://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,300,700,400,600");

* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
}

body {
	font-family: 'Open Sans';
}

a {
	text-decoration: none;
}

div#header {
	width: 100%%;
	height: 50px;
	background-color: %(header)s ;
	margin: 0 auto;
}

.logo {
	float: left;
	margin-top: 10px;
	margin-left: 10px;
}

.logo a {
	font-size: 1.3em;
	color: #fff;
}

.logo a span {
	font-weight: 300;
}

div#container {
	width: 100%%;
	margin: 0 auto;
}

.sidebar {
	width: 250px;
	/*height: 100%%;*/
	background-color: %(sidebar)s ;
	float: left;
}

ul#nav {

}

ul#nav li {
	list-style: none;
}

ul#nav li a {
	color: #ccc;
	display: block;
	padding: 10px;
	font-size: 0.8em;
	border-bottom: 1px solid #0A0A0A;
	-webkit-transition: 0.2s;
	-moz-transition: 0.2s;
	-o-transition: 0.2s;
	transition: 0.2s;
}

ul#nav li a:hover {
	background-color: #030303;
	color: #fff;
}

ul#nav li a.selected {
	background-color: #030303;
	color: #fff;
}


.content {
	width: auto;
	margin-left: 250px;
	height: 100%%;
	background-color: %(background)s ;
	padding: 15px;
}

.content p {
	color: #424242;
	font-size: 0.73em;
}

div#box {
	margin-top: 15px;
}

div#box .box-top {
	color: #fff;
	text-shadow: 0px 1px #000;
	background-color: %(box)s ;
	padding: 5px;
	padding-left: 15px;
	font-weight: 300;
}

div#box .box-panel {
	padding: 15px;
	background-color: #fff;
	color: #333;
}

a.mobile {
	display: block;
	color: #fff;
	background-color: #000;
	text-align: center;
	padding: 7px;
}

a.mobile:active {
	background-color: #4a4a4a;
}

@media only screen and (max-width: 320px) {
	.sidebar {
		width: 100%%;
		display: none;
	}

	.content {
		margin-left: 0px;
	}
}

@media only screen and (min-width: 320px) {

	a.mobile {
		display: none;
	}

	.sidebar {
		height: 100%%;
		display: block;
	}
}"""  % {'background': background, 'box': box, 'header': header, 'sidebar': sidebar}
    css.write(cssContents)
    print "CSS file is completed."
    css.close()

