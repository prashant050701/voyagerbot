import flask_app
from credentials import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import tweepy
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.utils import ChromeType
def god() :
  auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
  auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
  api = tweepy.API(auth)
  options = webdriver.ChromeOptions()
  options.add_argument('--no-sandbox')
  driver = webdriver.Chrome( executable_path='./chromedriver',options=options)
  url="https://voyager.jpl.nasa.gov/mission/status/#where_are_they_now"
  driver.get(url)
  st=driver.find_element_by_xpath("//*[@id='voy1_lt']").text.split(':')
  h=st[0]
  m=st[1]
  s=st[2]
  voy1_dist="NASA Voyager 1 is " + h +" hours "+m+" minutes "+s+" seconds light time away from Earth."
  st=driver.find_element_by_xpath("//*[@id='voy2_lt']").text.split(':')
  h=st[0]
  m=st[1]
  s=st[2]
  voy2_dist="NASA Voyager 2 is " + h +" hours "+m+" minutes "+s+" seconds light time away from Earth."
  with open('temp.txt', 'w') as f:
    f.write(voy1_dist+'\n\n'+voy2_dist)
  with open('temp.txt', 'r') as f:
    #print(f.read())
    api.update_status(f.read())
 
flask_app.keep_alive()

if __name__ == "__main__":
  god()
