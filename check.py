#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import httplib2
from pprint import pprint


from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
from googleapiclient.http import BatchHttpRequest

from models import Message, Summary
import constants

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


summary = Summary()


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'peacemail.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(constants.CLIENT_SECRET_FILE, constants.AUTHORIZATION_SCOPE)
        flow.user_agent = constants.APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def authorize_me():

    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    return service, http
    
def parse_mail(request_id, message, exception):

    if exception is not None:
        raise RuntimeError(exception)
        
    msg = Message().parse(message)    
    
    summary.add(msg)
            
  
def summarize_mail():

    service, http = authorize_me()
    batch = BatchHttpRequest()

    response = service.users().messages().list(userId=constants.USER_ID, q=constants.DEFAULT_QUERY).execute()
    messages = response.get('messages', [])


    if messages:
        # TODO think this only gets the first few, might need to page through results

        for message in messages:
            request = service.users().messages().get(userId=constants.USER_ID, id=message['id'], format=constants.RESPONSE_FORMAT, metadataHeaders=[constants.FROM_HEADER, constants.TO_HEADER])

            batch.add(request, callback=parse_mail)

        batch.execute(http=http)


        print "There are %s unread messages in your inbox." % len(summary.messages)

        print "%s of them are marked as important and %s are addressed to you." % (summary.important, summary.addressed_to_me)

        print "%s of them are scary." % summary.flagged

        response = raw_input("\nYou can do the thing! Do you want to see a preview of your messages? ")

        if response.lower().startswith('y'):
            print "\n"
            for i, msg in enumerate(summary.messages):
                print "Message #%s" % i
                print "=" * 30
                print "From: %s\nTo: %s\nSubject: %s" % (msg.sender, msg.to, msg.snippet)
                print "=" * 30
                print "\n"
    else:
        print "No messages! You are free. :)"


if __name__ == '__main__':
  summarize_mail()
