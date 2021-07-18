import requests
import os
header = {'Authorization': os.environ.get('auth')}
def script():
  first = input("what is your first name?:")
  last = input("what is your last name?:")

  def email_check():
    _ = input("What is your E-Mail?:")
    if _ == input('Please verify your E-Mail:'):
      return _
    else:
      email_check()
  email = email_check()

  status = requests.post(url='https://api.sheety.co/cb355fa7dfbe807c46143010b5acc159/flightContacts/sheet1',
  json = {
    'sheet1': {
      'firstname':first,
      'lastname': last,
      'email': email}},
  headers = header)
  if status.status_code == 200:
    print('Success!')
    if input('Would you like to go again? Y/n').upper() == 'Y':
      os.system('clear')
      script()
  else:
    print('Sorry this was not succesful')
script()
