# Python Website Generator by: Alex Eikre
#
# This program is used to generate a website.
# Allows you do choose your text, colorscheme,
# etc. You'll most likely want to customize the 
# html file.
#
# Last modified: Jan. 25, 2016

import os, sys
sys.path.append("..") #Making sure we're editing in main.py's directory
sys.dont_write_bytecode = True #We don't want Python to generate .pyc files!
import css

indexContents=""""""
title='title'
firstTab='firstTab'
secondTab='secondTab'
thirdTab='thirdTab'
fourthTab='fourthTab'
fifthTab='fifthTab'
sixthTab='sixthTab'
tabs=[firstTab, secondTab, thirdTab, fourthTab, fifthTab, sixthTab]
firstTabHeader1='firstTabHeader1'
firstTabHeader2='firstTabHeader2'
firstTabP='firstTabP' #P as in paragraph
colorscheme=0
tabCount=0
tabContents=""


def createIndex(title, firstTab, secondTab, thirdTab, fourthTab, fifthTab, sixthTab, firstTabHeader1, firstTabHeader2, firstTabP):
    os.mkdir("PythonWebGen", 0755 );
    os.chdir("PythonWebGen")
    index = open("index.html", 'a')
    #print "Name of the file: ", index.name
    #print "Closed or not : ", index.closed
    #print "Opening mode : ", index.mode
    #print "Softspace flag : ", index.softspace
    #print "Directory : ", os.getcwd()
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
			<ul id="nav">""" % {'title': title}
    tabCount=int(input("How many tabs would you like? "))
    tabContents=""
    for i in range(0,tabCount):
        tabs[i]=raw_input('Your '+str(tabs[i])+'? ')
        indexContents=indexContents+"""<li><a class="selected" href="#">%(tab)s</a></li>""" % {'tab':tabs[i]}
    indexContents=indexContents+"""</ul>
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
</html>""" % {'firstTab': firstTab, 'secondTab': secondTab, 'thirdTab': thirdTab, 'fourthTab': fourthTab, 'fifthTab': fifthTab, 'sixthTab': sixthTab,'firstTabHeader1': firstTabHeader1, 'firstTabHeader2': firstTabHeader2, 'firstTabP': firstTabP}
    index.write(indexContents)
    print "Index file is completed."
    index.close()

title=raw_input('What will the name of your website be? ')
firstTabHeader1=raw_input('Your first tab header 1?(see image) ')	
firstTabHeader2=raw_input('Your first tab header 2?(see image) ')
firstTabP=raw_input('Your first tab paragraph?(see image) ')	

colorscheme=input("Which Color Scheme would you like?\n 0: Default\n 1: Giant Goldfish\n 2: Thought Provoking\n 3: Papua New Guinea\n")

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
createIndex(title, firstTab, secondTab, thirdTab, fourthTab, fifthTab, sixthTab, firstTabHeader1, firstTabHeader2, firstTabP)
css.createcss(header, background, box)
