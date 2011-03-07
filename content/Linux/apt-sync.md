Title: apt-sync
Date: 2008-06-21

As a followup to [apt-rsync][1] and [analysis][2], I should point out that the
people on IRC who suggested it was already done [were clearly right][3].
What's not clear, however, is how this might enter Ubuntu or Debian accepted
practice. There's been a lot of debate since apt-sync's work over other ways
of compressing packages. LZMA, [already seen once][4] on this blog, is a
frequent contender. [Hardy][5] allows LZMA packaging, and I've seen several
mailing list threads about it. Unfortunately LZMA and rsync are mortal
enemies, shall we say. I'm not sure, but I think that LZMA has won because
zsync makes the CD image size problem worse, not better.

An alternative compromise might be to investigate [LZMA & squashfs.][6]
Currently this represents one of the interesting problems with the Linux
kernel. Almost everyone uses squashfs, and while Greg KH can go around
declaring that everyone should want their code in the tree and how there's
throngs of developers eager to make it happen, the LKML was fairly clear about
rejecting inclusion in 2005. There's been some **very** recent[ efforts to
bring squashfs into mainline][7], so there is hope. The trouble for squashfs-
lzma is that the squashfs maintainer refuses the patches because he's afraid
to risk being turned down by LKML again. So squashfs-lzma is distributed as a
patch to a patch, and most distros are wary, if they're even thinking about it
at all.

But assuming we could use LZMA on squashfs, that would leave Ubuntu more
free to ship packages built with an zsyncable package archive, but would still
leave a conflict between network bandwidth and disk space.

   [1]: http://jldugger.livejournal.com/6115.html

   [2]: http://jldugger.livejournal.com/6667.html

   [3]: https://edge.launchpad.net/apt-sync

   [4]: http://jldugger.livejournal.com/3722.html

   [5]: https://blueprints.edge.launchpad.net/ubuntu/+spec/dpkg-lzma

   [6]: http://www.squashfs-lzma.org/

   [7]: http://www.nabble.com/-patch-0-6--First-take-at-squashfs-mainlining-support-patches-to17825431.html

