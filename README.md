peacemail
============

I deal a lot with a thing I call jerkbrain. 

Jerkbrain is when your brain lies to you and tells you that normal, everyday things are scary and could murder you. This was a good thing back in the day when giant spiders constantly swarmed out of trees and sucked out our sweet juicy innards, but not so good when the scariest thing we deal with is, say, checking email.

The problem with a brain that refuses to tell the difference between cranky emails from people I don't like and a spider swarm that wants to engulf me in a screaming wriggling mass is I don't check email as much as I should. And this is a problem, both for me and the spiders, who just want to confirm details on lunch or whatever.

So I wrote a script. This lets you know when there's mail, optionally shows you the sender and the first line, and flags when there's mail from particular people; this lets you know when your email contains spiders so you can plan accordingly. 

Setup
------

You'll need to set up oauth access to your gmail account.

1. Go to https://console.developers.google.com and create a new project.

2. Go to APIs & Auth -> APIs and add the Gmail API to the project.

3. Go to APIs & Auth -> Credentials and click the *Add credentials* button and select *OAuth 2.0 client ID*.

4. Select the application type *Other*, name it whatever (PeaceMail is a good option) and click the *Create* button.

5. Once done, there will be a download button next to the client id. Click it.

6. Put that file in this directory and rename it `client_secret.json`.

Next, set up the script itself.

7. Create a new virtual environment and do: pip install -r requirements.txt

8. Rename default_personal.py to personal.py and add your email addresses and any other configuration you like.

Usage
------

Run ./check.py to check your mail for you and show you a summary of what's there. Optionally, you can see the senders and the gmail snippet of the email, too.

The first time you run it, it will open an oauth screen for you, which you'll need to approve. After that, it'll cache your credentials and everything will be golden.






