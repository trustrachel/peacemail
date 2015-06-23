peacemail
============

I deal a lot with a thing I call jerkbrain. 

Jerkbrain is when your brain lies to you and tells you that normal, everyday things are scary and could murder you. This was a good thing back in the day when tiger-sized spiders constantly dropped out of trees to suck out our sweet juicy innards, but not so good when the scariest thing we deal with is, say, checking email.

The problem with a brain that refuses to tell the difference between cranky emails from people I don't like and spiders pouring out of the computer to engulf me in a screaming wriggling mass is I don't check email as much as I should. And this is a problem, both for me and the spiders, who just want to confirm details whatever.

So I wrote a script. This summarizes your inbox and flags when there's mail from particular people, so you know when your email contains spiders and can plan accordingly. 

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






