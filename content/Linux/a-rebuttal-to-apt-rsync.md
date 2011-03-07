Title: A rebuttal to apt-rsync
Date: 2008-05-09

Seen on #ubuntu-devel today:

> [hi5] Re:rysnc method driver for apt. The context of this can be anything
from people over sat connections, 3rd world countries (like iraq where there
is no fiber, or copper backbones/lines since the ground is so hard it's almost
impossible to run it so everything is expensive sat. based), or saving
bandwidth / speeding up updates 1000x for all users / saving money to run
repos. Are there no thoughts?


A mess of counter opinion was offered, and some feelings were hurt. I see
this pretty often -- someone has an idea to help some people (usually
themselves included) and when people shoot the idea down and offer
alternatives they get outright angry. Sometimes people invest too much emotion
in the solution instead of the problem, I guess. Similar things happened with
Automatix, even though Automatix really did stupid things that really did
cause some upgrades to break and Ubuntu worked very hard to come up with (I
think) suitable alternatives. 

> [ andrew___] hi5: I think you need to be reading a book on
statistics rather than programming, actually. If you can show that debiff will
reduce bandwidth by X% and increase CPU usage by Y%, we can have a proper
debate about whether it's worth it. Until then, we're all just hand-
waving.<blockquote>

With that in mind, I'd like to suggest a quick demonstration of why rsync
fails at it's proposed goal of saving bandwidth. <a
href="http:/en.wikipedia.org/wiki/Rdiff">Rdiff is basically a binary patching
system based on rsync. It should be a good way to measure how much data needs
to be transferred. In order to give rsync a fair shot, I'm going to pick two
versions of a package and rdiff them. I'll pick them to be close in version,
one version bump, if you will. Browsing my apt cache the first satisfactory
package to hit my eye was xulrunner (the package causing many people angst
with firefox randomly terrible disk performance):

> jldugger@jldugger:~rdiff $ ls -lh

> -rw-r--r-- 1 jldugger jldugger 7.4M 2008-05-08 22:44 xulrunner-1.9_1.9~b5
+nobinonly-0ubuntu3_i386.deb<br>-rw-r--r-- 1 jldugger jldugger 7.4M 2008-05-08
22:44 xulrunner-1.9_1.9~b5+nobinonly-0ubuntu4~8.04.0mt1_i386.deb



> So it's a fairly big package, plenty of room for rdiffrsync to identify any
easy bandwidth savings. Any network overhead should be recoverable on a
package this size. First make a signature:

> jldugger@jldugger:~rdiff $ rdiff signature xulrunner-1.9_1.9~b5
+nobinonly-0ubuntu3_i386.deb xul.sig

> jldugger@jldugger:~rdiff $ ls -lh xul.sig

> -rw-r--r-- 1 jldugger jldugger 44K 2008-05-08 22:46 xul.sig<blockquote>

Then make the actual diff:

> jldugger@jldugger:~/rdiff $ rdiff delta xul.sig xulrunner-1.9_1.9~b5
+nobinonly-0ubuntu4~8.04.0mt1_i386.deb xul.diff

> jldugger@jldugger:~rdiff $ ls -lh xul.diff

>-rw-r--r-- 1 jldugger jldugger 7.4M 2008-05-08 22:47 xul.diff<blockquote>

And there you have it: **rsync saves no bandwidth at all for .debs.**
Moreover, these are the two CLOSEST versions. It's not hard to imagine why
this is: [the .deb file format][1] is an ar archive of two compressed
tarballs. The tarballs are going to mostly look like random data, and change
size. Just in case minor changes didn't totally screw over rsync by making
seemingly random changes all over the tarball, gluing the two tarballs
together is going to shift most of the archive around and raise hell as well.

At this point it's appropriate to introduce a [lecture][2] [(mp3
version)][3] by the author. It's really quite enlightening, but I'll highlight
the important bits for the lazy:

> the remote update problem is basically: you have two computers
connected by a very high latency, very low bandwidth link... a typical
Internet link, at least if you're in Australia. So, a piece of wet string, a
really pathetic link... and you've got two files. [...] You've got two lumps
of data; one sitting on one of the computers and the other sitting on the
other computer, and you want to update one of the lumps of data to be the same
as the other one.<blockquote>

> Basically the rsync program works fine on compressed files, the actual
binary works fine, but the rsync algorithm is not very efficient on compressed
files. [...] gzip uses dynamic Huffman encoding, which means if you change one
byte in the file, everything after that point in the file changes in the
compressed data. Problem; that means of course that rsync will be terrible,
unless, of course, the change is toward the end of the file. [58m, 31s]


Most importantly, near the end: <br>

> yes, handling renames is something I do want to do, partly because of the
stuff Steven has been doing with his apt-proxy stuff, where he's actually done
an rsync-based apt-proxy system. And look for it; I think it's called apt-
proxy, isn't it Steven?


>[Apt-proxy][4] essentially concludes the same thing, and restates a common 
hypothesis that rsync is CPU intensive. So unless you can convince gzip to 
adopt an rsync amenable compression, the apt-rsync is on life support. There 
are other ways one might go about this, but rsync isn't it today. I leave 
you with a bit of hope:

> There are always more efficient algorithms than rsync. If you
have structured data, and you know precisely the sorts of updates, the
constraints on the types of updates that can happen to the data, then you can
always craft a better algorithm than rsync.

   [1]: http://en.wikipedia.org/wiki/Deb_(file_format)

   [2]: http://olstrans.sourceforge.net/release/OLS2000-rsync/OLS2000-rsync.html

   [3]: http://ftp.gnumonks.org/pub/congress-talks/ols2000/high/cd2/2000-07-21_15-02-49_C_64.mp3

   [4]: http:/apt-proxy.sourceforge.net/

