Title: Introducing Money Into Open Source
Date: 2008-08-04

Jeff Atwood's [Coding Horror][1] is a blog ostensibly about "Programming and
Human Factors". So then Jeff's [proposition][2] about donating money in OSS is
a little troublesome. Jeff is confused and needs help spending money, like [ a
popular novel and film][3]. I've stopped reading Coding Horror on a daily
basis long ago, but the goals behind this particular theme are well placed,
and it seems like a worthwhile initiative. He [writes about donating $5,000 to
an open source .NET project][4]:

> I had hoped that $5,000 grant money would be converted into something that
furthered an open source project -- perhaps something involving the community
and garnering more code contributions. But apparently that's more difficult
than anyone realized.

>[...] I'm absolutely dumbfounded to learn that contributing money isn't
an effective way to advance an open source project. Surely money can't be
totally useless to open source projects... can it?

What follows below is the kind of research Jeff Atwood should have done in
preparation of giving that money. What I think would have been most useful to
Jeff is researching what has already been done, though I suppose he's not got
**time** for such trivial things.

### Ubuntu ###

To that end, several people were hired and a company formed. Lots of **time** 
was spent picking who would be hired, what would be done, and explaining what 
was broken in Debian and how Ubuntu would work differently. 

### Inkscape ###
Bryce Herrington, intimate with the development of Inkscape, writes in ["Pay 
in Time, not Money"][5]:

>I can't count the number of times people have offered $100 bounties for 
> implementing some feature or other in Inkscape. From what I've seen - and 
>I've seen MANY features come into Inkscape from folks who aren't developers
>- $100 is the wrong way to do it.

>Not that people are anti-money or anything like that. Certainly we've gotten 
>rabid success out of our Google Summer of Code projects, but these pay out 
>$4500. So maybe $100 just isn't the right price point to stir interest (even 
>a simple feature is going to require 10-20 hrs work, at which point you might 
>make more flipping burgers!)

Bryce wrote this after Jeff's decision, so it might seem unfair to cite him, but 
I think it's fair to say Bryce's thoughts reflect many of the developers Jeff 
could have asked. Bryce offers advice reinforcing Jeff's perception that time is 
more important than money. Bryce goes on to laud the advantages of documenting 
failure in a wiki, for others to read and overcome. Perhaps Launchpad should 
have [offered wikis instead of bounties][6].

Bryce also cites Google's Summer of Code as a success. He rightly chastises these 
chump change bounties, but I wonder how Bryce feels about the apparent failure of 
Jeff's larger donation that matches Google's SoC in scale.

### Google Summer of Code ###
Google Summer of Code is probably the most well known project spending money on 
open source. They've certainly paid for at some kickass projects on behalf of 
Ubuntu in the past. But unlike most bounties their model is a bit different -- 
they're targeting a specific group of people and asking for specific goals. The 
specific group is important -- college students interested in working at Google. 
$5000 motivates these students, since students don't have long term employment needs 
or expectations, a job to quit or family to feed. Additionally, because Google puts 
it out there as an "internship in open source", there's an implicit assumption that 
a job with Google can be had via this project, and that's something most of us can't 
rely on. 

Asking for specific goals is another part of the equation. Google rightly recognizes 
that many projects don't have a lot of management. By asking groups deal with deadlines 
and requiring all parties to come to them with ideas and choices, they embed 
management principles often ignored into open source projects. They also sidestep 
organizational problems by sending checks directly to the people doing work and doing 
some of the footwork beyond cutting a check themselves. 

Google asks organizations and people to plead their case. It's anti-democratic and _it 
works_. That's important to note, because Debian's own attempts at funding have been met 
with fierce democratic resistance.

### dunc-tank ###
Debian is a rough and tumble society. If you disagree, look at Sam Hocevar's 
[homepage][7] some time. **They elected a weapons grade troll as DPL**. (A title Sam 
might proudly wear, I think). Still, he's been an effective leader, and his [platform][8] 
was entirely reasonable after a highly contentious year. He writes on the subject of money:

> Debian has money. Last time someone wanted to use that money for something, we disagreed, 
> and he found money somewhere else. So we still have that money, and I would like to use 
> it at least to fix our broken hardware. I cannot believe this is in a DPL platform, but 
> escher has been down for ages, developers do not have access to an alpha machine, and we 
> have not even tried to fix that problem with money.

> Speaking of money, one thing that requires lots of it is meetings. IRC meetings are not 
> enough for some tasks, and isolating people in a remote place to work together on nothing 
> else than their Debian project has proven to work very well. Though I am getting scared by 
> the escalating luxury of the DebConf accommodations, I believe we can and should afford even 
> more meetings to take place. There are local structures in many countries (Extremadura in 
>Spain, Cetril in France) that can take care of the logistics. 

Sam's DPL-ship followed a long and painful debate about raising funds to compensate key people 
for their work. I don't want to open wounds here, but its a risk that must be taken to review 
what went wrong. [dunc-tank][9] was (is?) a project to compensate the volunteer release managers 
of Debian for their work. The proposal was received so poorly that a small minority of people 
didn't just reduce involvement in the face of compensation from others, but aimed to see the goals 
of dunc-tank fail, by [filing as many RC bugs as possible][10]. In one sense, the introduction 
of paid workers failed -- Etch released late. 

But in another sense it succeeded wildly. Suddenly a group of people had been motivated to 
test Debian and report RC bugs in far greater numbers than before, in _spite_ of not being paid 
for their efforts. Clearly something else was at work here, beyond compensating key players. I 
suspect that Sam Hocevar's role in that contra group greatly contributed support to his bid for 
DPL; it certainly demonstrated his ability to drive community contribution to release engineering. 
Sven Muller gave an opinion in his [summary of events][11]

> The whole thing might have been a lot different if some random, mostly unknown DD (or even better: 
> non-DD) had started dunc-tank, collecting money and finally paying some DDs to work on some specific tasks.

Much of the controversy appears to have been around whether the DPL could approve the use of 
general Debian funds to pay some developers but not others. That's a tough question, especially 
when a few developers appeared to despise money itself. Prescient Ben Mako Hill wrote something
[on mixing volunteers and money][12] that Dunc Tank might have neglected. It covers a few other 
examples of how money complicated things, including the historic X Consortium's [collapse][13]
and the revival in the form of the Xfree86 and later the X.org Foundation.

### Nouveau ###

[Nouveau][14] has a spectacular example of crowd-sourcing funding. Rather than raising $10,000 
from a monied few, David Nielsen offered the [following pledge[15]:

>"I will pledge at least $10 USD towards the development of the open source nouveau driver for the nvidia card series but only if 1,000 other people will do the same."

David was astonished at the [rate][16] of success of the pledge drive, and the nouveau developers 
were as well. So did the developers choose to spend it on beer, cigarettes and hardware? Surprisingly, 
no. Despite overwhelming support, none of the money raised has been collected or spent, for many 
reasons, some unique to this drive. I asked Stephane Marchesin, prolific nouveau developer, what happened, 
and he replied:

> My bank said the issue with small donations, especially international donations, is that the transfer 
> itself costs you money (up to $10, which is the amount for each donation). They also said under banking 
> regulations, 1400 $10 transactions could look suspicious and freeze my personal account. I don't know to 
> what extent this would have been taxed. This was not my major concern, as setting up a non-profit 
> organization would have solved that issue anyway. 

American readers may not realize it, but European [taxes][17] are quite high. The frozen account part 
is troublesome but the separate non-profit legal entity insulates Stephane's bank account from both 
these problems (but not the transaction fee problem). We have many such entities, though as Mark Shuttleworth 
alluded to above, sometimes they don't inspire confidence. Unfortunately, it appears [not a single one of the 
public entities] supporting open source was ready to risk legal battles by accepting responsibility for 
nouveau's pledge money. Stephane tells me that the Software Freedom Conservancy has since improved:

> We recently got an acknowledgment from the Software Freedom Conservancy that nouveau would have been a 
> suitable project for them to harbor (they are not afraid of being sued, for example they host the finances 
> for samba and wine). It's just unfortunate that at the time we looked for a helping organization they were 
> still in the process of setting up theirs.

Additionally, there's concerns over who gets what. When I asked on #nouveau about the pledge drive, 
it was suggested that simply putting money on the table is a recipe for [epic drama][19], and their 
current system works well enough: groups of people pitch in to buy hardware and ship it to a specific 
developer. 

### Conclusions ###
$5k or $10k is enough money to get attention, enough that people worry about doing it right. But not 
enough that people are actually motivated to do it right. Projects won't waste time thinking about 
spending money they don't anticipate receiving, so they generally don't have anything in place to take 
your money. They might not even realize they need it; the ScrewTurn wiki author Dario self nominated his 
project for the donation, apparently not fully aware how much paperwork and red tape might be involved. 
Some projects do indeed appear to use their money-agnostic traits as an insurgent model like Jon Galloway 
suggests; not only do they not know what to do with it, having it makes them more legitimate targets.

If not every project can use money, it's important then to review what does work. Google's approach neatly 
circumvents many of the problems above. They seek projects with the infrastructure to accept money. They 
amortize the costs of organizing by handling a huge number of projects, and they invite projects to 
participate in the stewardship of the resources Google's money has bought for them. Transaction costs are 
minor because the numbers involved are large. 

One thing that's clear from the evidence is that travel expenses are a uncontroversial way of spending money 
on a project. It's heavily recommended by the comments to Jeff's own blog, Sam Hocevar, and Ben Mako Hill. 
The comments suggest paying for PDC and using the other half for flight, food and hotel. ($2,500 for a 
conference sounds expensive to me--does PDC stand for "Pretty Damn Costly?")

The obvious answer to Jeff's problem is to reduce the [candidate list][20] to those projects capable of 
spending his money. That seems like the number one lesson Jeff can impart to the growing .NET Open Source 
community, and maybe open source at large.


   [1]: http://www.codinghorror.com

   [2]: http://www.codinghorror.com/blog/archives/000893.html

   [3]: http://en.wikipedia.org/wiki/Brewster's_Millions

   [4]: http://www.codinghorror.com/blog/archives/001158.html

   [5]: http://bryceharrington.org/drupal/node/52

   [6]: http://www.stefanoforenza.com/launchpad-needs-a-wiki/

   [7]: http://sam.zoy.org/

   [8]: http://www.debian.org/vote/2007/platforms/sho

   [9]: http://www.dunc-tank.org/
   
   [10]: http://dunc-bank.zoy.org/
   
   [11]: http://blog.incase.de/index.php/2006/10/27/debian-and-dunc-tank/

   [12]: http://mako.cc/writing/funding_volunteers/funding_volunteers.html
   
   [13]: http://www.usenix.org/publications/library/proceedings/usenix2000/invitedtalks/gettys_html/img0.htm

   [14]: http://nouveau.freedesktop.org/
   
   [15]: http://www.pledgebank.com/nouveaudriver
   
   [16]: http://www.pledgebank.com/nouveaudriver/info
   
   [17]: http://en.wikipedia.org/wiki/Taxation_in_France
   
   [18]: http://davidnielsen.wordpress.com/2007/02/26/a-cry-for-help/
   
   [19]: http://youtube.com/watch?v=awskKWzjlhk
   
   [20]: http://spreadsheets.google.com/pub?key=pKxDW35algYebfs8nssTjIQ
