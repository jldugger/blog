Title: Streamlined support tricks
Date: 2009-06-12

Ubuntu is a big project. Nobody really understands everything about Ubuntu;
even [authoring a Training video on Ubuntu][1] doesn't guarantee sufficient
expertise. One great thing about the Internet is that it can bring people with
a common interest or problem together. If you have a problem with your car,
there are dozens of outlets you can explore to diagnose and repair it. Today
I'll explore some of the various ways we can diagnose and repair Ubuntu, and
how to moderate the flow from these firehoses.

### Official Channels

Obviously Ubuntu was founded by people with a deep understanding of the
Internet, software, and collaboration. Over the past ten releases there have
been a number of avenues created for people to ask questions and get answers,
with varying degrees of noise and signal.

The most high profile of these is Launchpad's [bug tracker,][2] Malone (named
after Bugsy Malone?). If you have a problem that only changing a program can
fix, this is the place. It's modeled on BugZilla and Debian BTS, but brings a
lot of new stuff to the table. One such improvement over simple email based
tools is the dupe-finder. Given a description, Malone will suggest a set of
bugs similar in description, before asking you for a detailed write up of the
problem. This is a great way for software to help people with similar problems
find each other. But a big project like Ubuntu gets a lot of bugs; setting
yourself as a general bug contact is a very not smart idea. If you want to
help out with bugs, **pick a package or two and set yourself as a bug
contact**.

A more recent Launchpad addition is the [Answers tool][3]. You can ask a
question, and people can ask for more information or suggest an answer.
Answers manages the state of questions so you can safely ignored questions
with accepted solutions. Answers is intended for things that maybe aren't
exactly bugs, but simple questions about how to use a program. Like Malone, it
also features a dupe checker to help consolidate activity. It's not clear from
the website, but you can also set yourself as a answers contact for individual
packages. **https://answers.launchpad.net/ubuntu/+source/_pkg-name_/+answer-
contact** will point you in the right direction, for a given _pkg-name_. I'm
not aware of any RSS feeds for answers, in whole or in part, unfortunately.

We also run two support channels on Freenode, #ubuntu and #ubuntu+1. #ubuntu+1
is for development versions, so it usually focuses around testing packages and
undoing damage from package updates gone wrong. #ubuntu itself is the standard
support channel, but it can be very daunting. There's currently 1300 people
participating in the channel, and it requires a specific etiquette to scale.
Because simultaneous conversations are going on, it's best to address
questions to the channel, but address all replies to a specific recipient. IRC
clients will pick up when their name is used and highlight the reply above the
noise of other support conversations. There's also a set of [IRC bots][4] to
aid in common questions, facts, and [channel logging][5]. One neat extra is
that if you mention a bug number or URL, the bots can provide the channel with
the bug summary. **If you wish to selectively help people via IRC, join
#ubuntu, get familiar with your client and set some hilights on packages
you're an expert on**. If you want to get really sophisticated, there are
scripts out there for screen+irssi and libnotify that will generate a desktop
popup when an IRC hilight comes in.

The mailing lists serve a number of purposes within Ubuntu, but today I'll
focus on [the support][6] lists. Unmoderated lists can get pretty prolific;
[ubuntu-users][7] seems to average about a megabyte of mail a month. This
translated to 4000 individual emails for the month of May. That's 130 messages
a day! Again, a good email client can help trim that down. Gmail will group
messages into coherent threads, but we're still looking at perhaps 20 threads
a day. Cutting down the volume further may require getting familiar with mail
filters that are built into your client. I believe Gmail can store a list to a
folder and then bring in an entire thread to the inbox when a message matches
a keyword; but I haven't tried this. At any rate, I understand **procmail-like
tools are key to narrowing large volume lists to something more viable**.

Finally, there is [the forum][8]. Web forums have a reputation for being very
novice friendly, and very time wasting. Forums are also historically polling
oriented; if you want to know what's going on currently, you visit the website
and refresh the pages. I think UbuntuForums supports subscriptions, but only
at the granularity of boards and threads. That's potentially a lot of traffic,
so if you want something less demanding, you'll need to **subscribe to an
UbuntuForum board and filter it yourself in your mail client**, similar to the
mailing lists. There's no tracking of question status ("problem solved!");
that feature was deemed too hard on the database and disabled.

It seems like web based system have a higher potential to scale; I assume
that's mostly due to being backed by a database. But it's also important to be
able to customize the system for the support workflow and collaboration, and
that's an important distinction between Launchpad and a generic forum. Forums
are like the swiss army knife of social websites, you can use them to do lots
of things... poorly. I feel custom tailored software will always have an edge
over a general forum: wikis for howtos, bugtrackers for bugs, revision control
for scripts and programs.

### Unofficial resources

So far, we've only covered the things that people use who want to be involved
and associated with Ubuntu. The internet is a much wider place than ubuntu.com
and subdomains. I'll mention a few places I've found that some people may use
instead. Reasons for avoiding official avenues range from ignorance of what's
available, to having a established reputations and relations at another place,
to better turnaround times and wider points of view.

The first and obvious external support tool is Google websearch. It's a great
tool for surveying the hundreds of bugzillas, web forums and blogs on the net.
For many people, websearch is the first go-to tool when they encounter a
problem; any distribution that stops Google and search engines in general from
indexing their bug tracker is doing their users a disservice. Launchpad uses
an interesting URL scheme to make their database indexable; I hope to see how
they implemented it sometime in July.

The first actual website I'll mention is [AskMetafilter][9]. Metafilter is
free to read, but requires a 5 dollar one time fee to post. As a result, they
have managed to build a community of [pleasantly eloquant posters][10]. **And
they're full on board with web 2.0 features like tagging and [RSS
feeds][11].** The volume is already quite low as a result of the 5 dollar
hurdle, especially since you can only ask one question a week and have to wait
a week before asking a question.

But generally, you probably don't want to pay to help other people out. An
interesting new group of sites has been built with some very worthwhile design
insights to motivate quality responses and questions. There are countless
question and answer sites out there; Google Answers (now retired), Yahoo
Answers, etc. There's also specialized sites like Experts Exchange that do
some unsavory tricks and generally profit from crowdsourced labor that happens
spontaneously on the web. StackOverflow is a site designed to shift the rules
for programming questions on the web towards open access. But more interesting
for Ubuntu is it's companion site, [ServerFault][12], which is geared towards
servers and system administration, a topic that will be more relevant to
Ubuntu than programming questions typically get. They support RSS feeds, so
you can **subscribe to all questions tagged [Ubuntu][13]**. I hope people
working on LP answers observe what is and isn't working for ServerFault.

And obviously, if a specific program is having trouble, there's usually an IRC
channel, mailing list, bug tracker or forum organized by upstream. If you're
going upstream for help, just be careful. It can be frustrating for user after
user to come in and complain about a bug in Ubuntu that is fixed in upstream's
latest release. If you're looking to help people, getting involved upstream is
always a good pick. If you're still reading, hopefully this lengthy post has
given you some ideas on how to target specific support request topics, and
save yourself some time wading through noisy communication channels. Helping
out doesn't have to be an avalanche of data!

   [1]: http://jldugger.livejournal.com/19709.html

   [2]: http://launchpad.net/ubuntu

   [3]: http://answers.launchpad.net/ubuntu

   [4]: https://wiki.ubuntu.com/UbuntuBots

   [5]: http://irclogs.ubuntu.com

   [6]: https://lists.ubuntu.com/#Community+Support

   [7]: https://lists.ubuntu.com/archives/ubuntu-users/

   [8]: http://ubuntuforums.org/

   [9]: http://ask.metafilter.com

   [10]: http://www.thatsaspicymeatball.com/comments/

   [11]: http://ask.metafilter.com/tags/ubuntu/rss

   [12]: http://serverfault.com/

   [13]: http://serverfault.com/feeds/tag/ubuntu

