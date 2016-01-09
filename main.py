import os, sys
sys.path.append("..") #Making sure we're editing in main.py's directory
sys.dont_write_bytecode = True #We don't want Python to generate .pyc files!
import css

indexContents=""""""
title='title'
firstTab='firstTab'
firstTabHeader1='firstTabHeader1'
firstTabHeader2='firstTabHeader2'
firstTabP='firstTabP' #P as in paragraph
secondTab='secondTab'
thirdTab='thirdTab'
fourthTab='fourthTab'
fifthTab='fifthTab'
sixthTab='sixthTab'
colorscheme=0


def createIndex(title, firstTab, secondTab, thirdTab, fourthTab, fifthTab, sixthTab, firstTabHeader1, firstTabHeader2, firstTabP):
    os.mkdir("PythonWebGen", 0755 );
    os.chdir("PythonWebGen")
    index = open("index.html", 'a')
    print "Name of the file: ", index.name
    print "Closed or not : ", index.closed
    print "Opening mode : ", index.mode
    print "Softspace flag : ", index.softspace
    print "Directory : ", os.getcwd()
    indexContents="""<html>
<head>
<title>%(title)s</title>
<link rel="stylesheet" type="text/css" href="styles/global.css" />
<meta name="viewport" content="width=device-width, initial-scale: 1.0, user-scalabe=0" />
<script src="scripts/jquery-1.11.1.min.js"></script>
<script src="scripts/general.js"></script>
</head>

<body>

	<div id="header">
		<div class="logo"><a href="#"><span>%(title)s</span></a></div>
	</div>

	<a class="mobile" href="#">MENU</a>

	<div id="container">
		<div class="sidebar">
			<ul id="nav">
				<li><a class="selected" href="#">%(firstTab)s</a></li>
				<li><a href="#">%(secondTab)s</a></li>
				<li><a href="#">%(thirdTab)s</a></li>
				<li><a href="#">%(fourthTab)s</a></li>
				<li><a href="#">%(fifthTab)s</a></li>
				<li><a href="#">%(sixthTab)s</a></li>
			</ul>
		</div>
		<div class="content">
			<h1>%(firstTab)s</h1>
			<p>%(firstTabHeader1)s</p>

			<div id="box">
				<div class="box-top">%(firstTabHeader2)s</div>
				<div class="box-panel">
					%(firstTabP)s
				</div>
			</div>

			<div id="box">
				<div class="box-top">%(firstTabHeader2)s</div>
				<div class="box-panel">
					%(firstTabP)s
				</div>
			</div>

			<div id="box">
				<div class="box-top">%(firstTabHeader2)s</div>
				<div class="box-panel">
					%(firstTabP)s
				</div>
			</div>

		</div>
	</div>

</body>
</html>""" % {'title': title, 'firstTab': firstTab, 'secondTab': secondTab, 'thirdTab': thirdTab, 'fourthTab': fourthTab, 'fifthTab': fifthTab, 'sixthTab': sixthTab,'firstTabHeader1': firstTabHeader1, 'firstTabHeader2': firstTabHeader2, 'firstTabP': firstTabP}
    index.write(indexContents)
    print "Index file is completed."
    index.close()

title=raw_input('What will the name of your website be? ')
firstTab=raw_input('Your first tab? ')
secondTab=raw_input('Your second tab? ')
thirdTab=raw_input('Your third tab? ')	
fourthTab=raw_input('Your fourth tab? ')	
fifthTab=raw_input('Your fifth tab? ')	
sixthTab=raw_input('Your sixth tab? ')
firstTabHeader1=raw_input('Your first tab header 1?(see image) ')	
firstTabHeader2=raw_input('Your first tab header 2?(see image) ')
firstTabP=raw_input('Your first tab paragraph?(see image) ')	

colorscheme=input("Which Color Scheme would you like?\n 0: Default\n 1: Giant Goldfish\n 2: Thought Provoking\n 3: Papua New Guinea\n") #TODO: Add custom color schemes

header='#2c3e50'
background='#95a5a6'
box='#2980b9'

if colorscheme==1:
	header='#FA6900'
	background='#E0E4CC'
	box='#F38630'
if colorscheme==2:
	header='#675267'
	background='#53777A'
	box='#C02942'
if colorscheme==3:
	header='#5E412F'
	background='#F07818'
	box='#5E412F'
print colorscheme
createIndex(title, firstTab, secondTab, thirdTab, fourthTab, fifthTab, sixthTab, firstTabHeader1, firstTabHeader2, firstTabP)
css.createcss(header, background, box)
