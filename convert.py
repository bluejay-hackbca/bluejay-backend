import re
from mechanize import Browser
br = Browser()
br.set_handle_robots( False )
br.addheaders = [('User-agent', 'Firefox')]


search_term = 'george washington'

br.open("http://www.google.com/")
br.select_form('f')
br.form['q'] = search_term
br.submit()
#br.follow_link( list(br.links())[0] )
#print list(br.links())[10]
#br.follow_link( link )
