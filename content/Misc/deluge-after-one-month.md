Title: Deluge: After one month
Date: 2008-01-02

A month ago, I wrote about a [plan to automate][1] some of my online
activities, and in particular, to replace Azureus with [Deluge][2]. Well, I've
been using it for the last six months and here's the scoop:

### Pros

**Works** Deluge delivers the goods. Encryption, DHT, uPNP etc. Pretty much
everything you need in the face of mean ISPs, throttling, and leeches.

**Actively developed** Deluge is rapidly improving with quality and features.
The development community is responsive, if a bit hostile at times. The cons
below have a chance at being eliminated in the future, if this continues.

**Non-judgemental** Deluge doesn't try its hardest to stop me from seeding, it
doesn't try to trick users etc. The system to stop seeding is extremely simple
and I hope in the future it's extended to shut the whole thing down when
there's no active torrents left.

### Cons

**No good plan for end user distribution** Traditionally, Debian users wait
for upstream releases to enter unstable, and Ubuntu users sometimes wait for
the next release. The Debian model works great when a DD is involved, and the
Ubuntu system works okay with -backports and PPAs. Deluge has managed to avoid
both of these, but also avoided providing the usual sources.list repo. They've
been grappling with how to better serve their users in light of the cost of
being popular and rapidly changing. Ubuntu represents 50 percent of the
bandwidth and 80 percent of the downloads -- if anyone (Jono maybe) reads
this, perhaps it's nearly time to form an outreach.

**No significant memory savings** Azureus has a reputation for being fat, and
I was hoping that Deluge would be lighter. It was at first, but with new
versions came new features and new weight. My primary reason for switching was
to reduce memory usage. DHT alone seems to cost 5 resident memory MB and 3
writable. I'm not sure how to best analyze memory usage. Comments welcome ;)

For me now, Deluge is the app to beat.

   [1]: http://pwnguin.net/a-plan-for-anime.html

   [2]: deluge-torrent.org/

