peacemail
============

I deal a lot with a thing I call jerkbrain. 

Jerkbrain is when your brain lies to you and tells you that normal, everyday things are scary and could murder you. This was a good thing back in the day where tiger-sized spiders could drop out of a tree at any moment and eat you, but not so good when the scariest thing we deal with is checking email.

The problem with a brain that refuses to tell the difference between spiders and cranky emails from people I don't like is I don't check email as much as I should, since it might contain digital spiders that will pour out of the computer and engulf me in a screaming wriggling mass. And this is a problem, both for me and the digital spiders, who just need me to

So I wrote a script to make it better. This tells you whether or not you have mail and if that mail is from particular people so you know whether your email contains spiders and can plan accordingly. 

Setup
------

You'll need to set up oauth access to your gmail account.

1. Go to https://console.developers.google.com and create a new project.

2. Go to APIs & Auth -> APIs and add the Gmail API to the project.

3. Go to APIs & Auth -> Credentials and create a new client id. Choose "Installed Application" as the type.

4. It will make you configure an OAuth consent screen, so put whatever makes it happy. 

5. Once done, download the json file, put it in this directory and rename it 'secrets.json'

Next, set up the script itself.

6. Create a new virtual environment and do: pip install -r requirements.txt

7. Rename default_personal.py to personal.py and add your email addresses and any other configuration you like. 

Usage
------

Run ./check.py to check your mail for you and show you a summary of what's there. Optionally, you can see the senders and the gmail snippet of the email, too.

The first time you run it, it will open an oauth screen for you, which you'll need to approve. After that, it'll cache your credentials and everything will be golden.






