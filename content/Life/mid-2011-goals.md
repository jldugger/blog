Title: Mid 2011 Update
Date: 2011-07-31

Over halfway through 2011, so it's time to revisit my goals again. I really
should post more often.

### Personal Website ###
   
pwnguin.net consistently gets more than a thousand hits a month. That's enough
that I can start adding A/B experiments on the most popular pages. I've added
some ads to blog posts to see if anything there gets unusually good revenue.
Still haven't published that bit on using grep to solve [NPR's Sunday 
puzzles][3], but someone did admit to doing so on air! Need to add `awstats.js`
to the templates, to better complement Google Analytics.

I also set up an AdWords account just to try it out. I got a $100 coupon but
had to call them to redeem it and it's an awkward conversation since they want 
to set up a campaign themselves when I don't really have anything in mind yet. 
It's quite expensive what they set up, but I think I can come up with a cheaper
campaign once I've got more clue.

In June I set up openLDAP and tied some of the easier systems in. For a while
I was worried, as my free [SSL cert provider][4] was compromised. But they came
back online shortly before my certs expired and I've got it rolling. I also set
up IPv6, but I'm not really using it for anything other than IRC at the moment.
KSU won't be IPv6 ready for quite a while it seems, and IPv4 allocations are
basically running on empty.

### K-SLUG ###

Not much done here. Right now we mostly meet on Wednesdays for informal lunches
and sometimes discuss Linux. Ideally, I'd establish a Friday Night fight (for 
open source gaming), and monthly tech presentations. But before I get that off 
the ground, I need to set up limesurvey and gather opinions. A work in 
progress, but I'm hardly the only slacker here.

### Work ###

Strange goings on lately. We're having difficulty hiring and retaining system
administrators. As I chat with the existing ones, I learn more and more
peculularities that drain their time. Like, scripts to copy out of LDAP instead
of directly relying on it. Anyways, they're having trouble getting a big enough
applicant pool to convince Affirmative Action to allow them to hire two people,
and the recent turnover roughly matches the rate at which they can hire, which 
leaves them constantly understaffed.

I did catch several [Google I/O videos][5] in June, though as you might expect,
most were really about using Google's platform than building your own. Lots of
Android and Chrome WebGL stuff--only [two][6] [videos][7] related to Identity
Management. So I did spend some free time reading some papers on entropy and
passwords, especially during the move last week when I was without net access
at the new place. I'll probably start up a new category and see about getting
on Planet Identity once I've got a few posts up.

Beyond papers and presentations at home, I picked up several books on Java and
a book on Kerberos from the research uni, and helped out a bit with our 
new password change page. Right now it takes users 3 tries to choose a valid 
password, and some people up to ten. This is on par with published research 
on usability, so when our system doesn't improve things, we'll know why.

### Personal finance ###

Beyond those goals, in July I pretty much focused on finance. Nobody in the 
department recieved raises that I know of. So I've located a new place with
a roommate. Took quite a bit of effort to organize all the movers and
cleaners, but I estimate I've saved about 3k annually.

I also get garage parking, a larger kitchen, a closet in the bathroom, and 
access to Tivo / Netflix. The new place is much further away, and in the
destruction path of Tuttle Creek Lake. I located a [site on lake levels][1] 
that might make it worth setting up nagios for so I can write and deploy a 
scraper for it.

In other news, I figured out why my student loan split in GNUCash is always 
wrong. Simple daily interest formula is not possible to represent at the 
moment, although I've filed a [uservoice request][2]. I'm also trying out the
future transactions and cleared / reconciled features. It's actually pretty
nice to schedule a bunch of recurring transactions and have them show up 30
days before they occur. Although creating transactions ahead of time doesn't
work so well for 403(b) contributions. I also converted from XML to the sqlite 
backend, but it turns out the schema's a bit ugly. I was really hoping that
since it has a postgres option I might be able to build some python reporting 
webpages, but it's not as trivial as I'd hoped.

### The future ###

Next quarter, I'll continue integrating apps with LDAP, and maybe selfhost 
openID. It turns out there's nothing in Debian yet for this... Also outta
set up nagios or something to monitor items of interest. And, I should probably
fix my self-hosted Mozilla Sync server.

I've also got some posts in draft for the Identity tag that I can finish up 
and post. There's been some commotion from Mozilla about solving authentication
I could reflect upon. On the wbe analytic side, I'll run through Conversion 
University and try some A/B testing. 

I'll also probably start up a subsite to sell my used games with. I've found
good sites to sell on already, but finders fees and shipping eats into the 
better prices, so having a URL I can point locals at might save me and local 
buyers hassle.

I also need to learn about HSAs and such before open enrollment. Our offering 
looks pretty good, but I know a guy who caught unaware of a new change 
regarding OTC drugs and his FSA.

   [1]: http://www.nwk.usace.army.mil/tc/daily.cfm
   [2]: http://uservoice.com/a/mzAEn
   [3]: http://www.npr.org/series/4473090/sunday-puzzle
   [4]: https://www.startssl.com/?app=11&action=true
   [5]: http://www.google.com/events/io/2011/sessions.html
   [6]: http://www.google.com/events/io/2011/sessions/clientlogin-fail.html
   [7]: http://www.google.com/events/io/2011/sessions/identity-and-data-access-openid-and-oauth.html
