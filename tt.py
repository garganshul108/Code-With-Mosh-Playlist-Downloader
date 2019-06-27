import mechanize
from bs4 import BeautifulSoup
import urllib2 
import cookielib

cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open("https://sso.teachable.com/secure/146684/users/sign_in?clean_login=true&reset_purchase_session=1")

br.select_form(nr=0)
br.form['user[name]'] = 'sci.agarg@gmail.com'
br.form['user[password]'] = 'ag.garg96'
br.submit()

print(br.response().read())