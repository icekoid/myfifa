import webbrowser
import requests
import os

url = 'http://localhost:63342/fifa22/myFIFA.html?_ijt=kvje064dg9kd7stddj870sim8q&_ij_reload=RELOAD_ON_SAVE'
r = requests.get(url, allow_redirects=True)

open('myFIFA.html', 'wb').write(r.content)

new = 2 # open in a new tab, if possible

cwd = os.getcwd()
filepath = cwd + "/myFIFA.html"
webbrowser.open(filepath,new=new)

