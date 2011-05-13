Title: Reducing Interruptions
Date: 2011-05-13

Been pondering lately how I'd design a desktop environment to improve 
productivity. Many of the ideas are non-trivial changes, but there's a few 
papercut sized tweaks I thought I'd document and share. These all revolve 
around the notion of [flow][1], a state of concentration. The aim is to reduce
notification popups and, as a side effect, waste less time futzing with the 
window manager by batch processing them.

1. *Set Liferea update frequency to once a day.* Many feeds specify a refresh 
of two hours. For news junkies, this might be fine. But none of the feeds I 
subscribe to are time sensitive. So I set the "Default Feed Refresh Interval" 
to 1 day. You can override the default for 'important' feeds, if need be.

2. *Set Evolution to check less frequently*. This one can be controversial. By
default Evolution checks and notifies every 10 minutes. Since the goal is 
multiple hours of uninterrupted concentration, that's far too many chances of
interruption. The challenge is responding to urgent mail without letting the 
less urgent stuff interrupt. My approach is to turn off general notifications 
and set alerts for important senders, like the boss and the support ticket 
system. 

3. *Set Gwibber to check less frequently.* If someone needs your immediate 
attention for 140 characters or less, they probably know how to reach you by 
SMS. You can tweak the notifications to only include mentions and replies, 
which dramatically cuts down on the traffic. Unfortunately, Gwibber limits the 
upper bound between refeshes to an arbitrary 240 minutes, so if you wanted a 
once a day reminder to check everything, you're out of luck there.

4. *Filter noisy RSS feeds.* Not all feeds are pure information. For example, 
the LinkedIn feed throws in tweets from your connections. I'm a fan of feed 
processing tools, whether it be Yahoo! Pipes or client side XSLT. If you're 
extra lucky, the feed has a digest; Lifehacker was unique in offering a 
highlights tag feed, which reduces a weeks worth of posts to a single digest
post on Friday. Gawker seems to have killed these tag feeds and posts, after
the rousing success of driving users away with their recent redesign. Of
course, you can always unsubscribe if you find the signal just isn't worth the 
noise...

5. *Turn off banshee track notifications.* Music is a great way to mask ambient
noise in your home or office. Default Banshee however, pops up a notification
on every track change. As I'm reading a paper or writing code, this pop up 
distracts the eye away from the monitor I _was_ looking at. There doesn't seem 
to be a configuration change one can make, but a clever user on AskUbuntu has
[found a makeshift solution][2]. 

   [1]: http://en.wikipedia.org/wiki/Flow_%28psychology%29
   [2]: http://askubuntu.com/questions/33946/disable-notifications-on-track-change
