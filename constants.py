try:
  import personal
except ImportError:
  print "Hi, you forgot to rename default_personal.py to personal.py. Please do that and try this again!"
  raise SystemExit


MY_EMAIL_ADDRESSES = personal.EMAIL
SCARY_SENDERS = personal.SCARY_SENDERS
DEFAULT_QUERY = personal.DEFAULT_QUERY

IMPORTANT_LABEL = u'IMPORTANT'

FROM_HEADER = 'From'
TO_HEADER = 'To'

USER_ID = 'me'

RESPONSE_FORMAT = 'metadata'
AUTHORIZATION_SCOPE = 'https://www.googleapis.com/auth/gmail.readonly'

CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'PeaceMail'