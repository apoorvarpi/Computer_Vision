import mechanicalsoup as MS

browser = MS.Browser()
browser.set_proxies({"http": "username:password@proxy:8080",})
browser.set_handle_robots(False)
browser.set_handle_equiv(False)

browser.addheaders = [('User-Agent', 'Mozilla'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'), ('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'),('Accept-Encoding', 'none'),('Accept-Language', 'en-US,en;q=0.8'),('Connection','keep-alive')]

inp = raw_input()
browser.open(inp)
# insert more filetypes after ,
# filetypes denotes the extension of files you want to download from the links
filetypes = [".pdf",".ppt"]
files = []
for l in browser.links():
	for t in filetypes:
		if t in str(l):
			files.append(l) #all the links matching the filetypes stored in files

def downloadlink(l):
	browser.click_link(l)
	print (l.text, " downloaded")

for l in files: #downloading
	downloadlink(l)
