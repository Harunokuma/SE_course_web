import re
import codecs
import os

if __name__ == "__main__":
	string = ""
	for name in os.listdir():
		if(name.find(".html") == -1):
			continue
		print(name)
		with codecs.open(name, "r", "utf-8") as f:
			string = f.read()
			header1 = '<header class="main-header">'
			header2 = '</header>'
			sidebar1 = '<aside class="main-sidebar">'
			sidebar2 = '</aside>'
			footer1 = '<footer class="main-footer">'
			footer2 = '</footer>'
			body = '</body>'
			new_string = string[0:string.find(header1)+len(header1)] +"\n<!--load by js-->\n"+ string[string.find(header2):]
			string = new_string
			new_string = string[0:string.find(sidebar1)+len(sidebar1)] +"\n<!--load by js-->\n"+ string[string.find(sidebar2):]
			string = new_string
			new_string = string[0:string.find(footer1)+len(footer1)] +"\n<!--load by js-->\n"+ string[string.find(footer2):]
			string = new_string
			new_string = string[0:string.find(body)-1]+'  <!-- initial --><script src="../../static/js/initial.js"></script>' + string[string.find(body):]
			string = new_string
			print(string)
		with codecs.open(name, "w", "utf-8") as f:
			f.write(string)

