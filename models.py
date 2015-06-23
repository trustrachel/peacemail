import constants

class Message(object):
  id = None
  to = None
  sender = None
  snippet = None
  labels = []
  debug = None
  
  def __init__(self, id=None):
    self.id = id
    
  def parse(self, json):
    
    self.id = json['id']
    
    # Not sure if these headers are in all mail? 
    for header in json['payload']['headers']:
      if header['name'] == 'From':
        self.sender = header['value']
      elif header['name'] == 'To':
        self.to = header['value']
		
    self.snippet = json['snippet']
    self.labels = json['labelIds']
    self.debug = json
    
    return self
    
    
class Summary(object):
  important = 0
  addressed_to_me = 0
  flagged = 0
  messages = []
  
  def add(self, message):
    if constants.IMPORTANT_LABEL in message.labels:
      self.important += 1
      
    for email in constants.MY_EMAIL_ADDRESSES:
      if email in message.to.lower():
        self.addressed_to_me += 1
      
    if self.is_flagged(message):
      self.flagged += 1
      
    self.messages.append(message)
  
  def is_flagged(self, message):
  
    for scary in constants.SCARY_SENDERS:
      if scary in message.sender.lower():
        return True
      
    return False
    
    