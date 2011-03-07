Title: Developer time is rivalrous
Date: 2009-06-07

[Martin Owens][1] writes on the subject of open source economics:

> What I would suggest is that we are looking at the problem the wrong way.
While software is not rivalrous or excludable, software development as a
service is excludable (although not quite rivalrous) and this is important.

Fundamentally, I'm not sold on "source code isn't excludable". Or computer
data of any sort for that matter. If I make a photo, I can exclude it by not
publishing it until I receive payment for it. Similarly, if I hire Martin to
patch the source code for a project, I can exclude others from that work
simply by not publishing the patch. It's tempting to apply the following logic
to excludable goods:

  1. HackerWare publishes an open source product, FizBuzz.

  2. SuitSales Inc [discovers FizBuzz has a flaw][2].

  3. SuitSales Inc, depending on FizBuzz, hires a Joe The Programmer to fix
the bug for them in house.

  4. **(the "software isn't excludable" step/fallacy) **Joe the Programmer
gives the patch away for free to people, maybe even HackerWare.

Except Joe the Programmer doesn't have to give the patch away for free. He
could go around consulting with SuitSales's competitors and repeat the
transaction, at significantly lower costs (people complain about this practice
in the IT community). He might even negotiate an agreement with people not
share his patch. But even if he doesn't, ** SuitSales Inc. has the same
incentives**: share in exchange for cash. In any case, some action has to be
taken for a third party to enjoy the benefits of the patch.

In fact, the GPL isn't enough to make normal code a public good. You're under
no obligation to publish patches for private use, and no third party is
required to be involved. Instead, the GPL is sort of a compromise, to undo the
damage copyright has wrought on the process. Copyright provides massive
incentives to produce "intellectual property." Ever notice how "hit-driven"
markets seem to deal exclusively with intellectual property? Movies, music,
software, books; theres more stuff out there that I want to enjoy than I could
spend a lifetime consuming.

So if this is more of a club good, why do people offer code seemingly for
free? Joe might give the patch away in exchange for some peer review of his
code before he offers it to his clients for production use. SuitSales might
want ease of maintenance, [because carrying a delta incurs a cost][3]. The GPL
provides grease on the wheels for this.

And why would HackerWare [release the code][4] in the first place? Because all
this consulting work is, and always has been, the gravy train, and HackerWare
has a major competitive advantage. They can advertise support contracts at the
same place you get the software from, and they know the heart of the code.

So I find Martin Owen's proposal interesting, but probably misguided. He
denigrates support contracts as somehow indirect and undesirable, when it's
really a good way to insure a group of users and fund development in the
process. The trouble with buying and selling developer time directly is one of
estimation. Generally speaking, you hire developers for their output. It's
generally believed that programmer productivity is unequal and hard to measure
beforehand, so you really have no idea how many "blocks" you'd need to spend
to prioritize a feature or bug. And how would you enforce hours worked?

Most importantly, what does escrow do with failed projects?

   [1]: http://doctormo.wordpress.com/2009/06/06/foss-can-work-in-the-free-market/

   [2]: http://imranontech.com/2007/01/24/using-fizzbuzz-to-find-developers-who-grok-coding/

   [3]: https://wiki.ubuntu.com/MarkShuttleworth#Is%20Ubuntu%20a%20Debian%20fork?%20Or%20spoon?%20What%20sort%20of%20silverware%20are%20you,%20man?

   [4]: http://en.wikipedia.org/wiki/Zope

