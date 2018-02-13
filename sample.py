import talon
from talon import quotations
import time

talon.init()
start =29
end=30
html ="<div>"
while start < end:
	fileName = '/Users/Kannan/Documents/Freshdesk/Projects/Email_service/Parsing test case/samplefiles/html/'+str(start)+'.eml'
	with open(fileName, 'r') as myfile:
		html = myfile.read()
	start1 = time.time()
	html = (html[:10000] + '..') if len(html) > 10000 else html
	reply = quotations.extract_from(html, 'text/html')
	#reply = quotations.extract_from_html(html)
	start=start+1
	print reply
print len(html)
print len(reply)
