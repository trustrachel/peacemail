
# A list of all your email addresses. These can be partial matches
# i.e. 'foobar@gmail.com' or 'foobar'
# TODO: regex support for those google-style foo+whatever@gmail.com style
# 
# Examples: 'email@domain.com', 'my_email' 

EMAIL = []

# Flagged senders of email. This looks at the from header, which is usually of the form
# Person Name <email@address.com>. You can put email addresses or names in here and 
# if it's in the sender field, it'll match.
# TODO: regex support
# 
# Examples: 'person@scary.com', 'scary.com'
SCARY_SENDERS = []

# What query we should use to find email. By default, we ask for unread mail newer than
# 7 days and in your primary box. For more queries, see Google's help:
# https://support.google.com/mail/answer/7190?hl=en
# 
DEFAULT_QUERY = "category:primary is:unread newer_than:7d"