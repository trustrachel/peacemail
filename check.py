#!/usr/bin/env python
# -*- coding: utf-8 -*-


import httplib2
import simplejson as json
from pprint import pprint

from apiclient.discovery import build
from apiclient.http import BatchHttpRequest

from oauth2client.file import Storage
from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import argparser, run_flow

from models import Message, Summary
import constants


summary = Summary()


def authorize_me():

	# Open up the JSON file from google and pull stuff out of it
	info = json.load(open(constants.SECRETS_FILE, 'rb'))
	
	client_id = info['installed']['client_id']
	client_secret = info['installed']['client_secret']
	
	flow = OAuth2WebServerFlow(client_id, client_secret, constants.AUTHORIZATION_SCOPE)

	storage = Storage(constants.CREDENTIALS_STORE)

	credentials = storage.get()

	# This makes oauth2 flow work better on the command line, since it doesn't try to redirect
	# to the web server we're not running.
	flags = argparser.parse_args(args=['--noauth_local_webserver'])
	
	if credentials is None or credentials.invalid:
		credentials = run_flow(flow, storage, flags=flags)

	http = httplib2.Http()
	http = credentials.authorize(http)

	service = build('gmail', 'v1', http=http)

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
	messages = response['messages']
	
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


if __name__ == '__main__':
  summarize_mail()