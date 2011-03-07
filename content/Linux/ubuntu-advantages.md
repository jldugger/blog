Title: Ubuntu advantages
Date: 2008-07-20

There are some advantages to running Ubuntu I can think of:

  * apt-get

  * six month release cycles

  * at a very low cost

  * deep access to the process that creates Ubuntu

  * a large community with an [established etiquette][1]

But not among those is "never search the internet for drivers again". There is
a perception that this is special to Ubuntu or Linux. Oh, and also that it's
true. Which is why [the Ubuntu UK podcast][2] mentions it.

The problem, as I've lead you to believe, is that it's **not true**. Linux
does support a lot of hardware. Probably more than Windows, certainly more
than Apple. Greg K-H says people want Linux kernel source / binary
compatibility for the driver support. What Linux doesn't do so great job of is
supporting _new_ hardware. Lets say you run out and build a new computer which
includes a Gigafoo motherboard, with a pq43 chipset, which only hit the market
recently and you want to install Ubuntu 8.04. **You can't.** (Specifics
changed because my source is unavailable for details at the moment.)

Unsurprisingly, the hardware is only supported recently, and the 8.04 kernel
is based on an older kernel. 8.10 will probably support this out of the box,
but not 8.04. Technically, 8.04 LTS might be slightly different. But
otherwise, there's a six month gap in Ubuntu's process where you might fall
into unsupported territory (see? process _does_ matter!). You certainly can't
go to the vendor's website and download some drivers to make it work.

You could build a new kernel with the new drivers you need, but good luck
finding where they are and whether they're ready yet. Someone came 
into #ubuntu-kernel today [asking why][3] his upstream kernel didn't build and 
the short answer is "it doesn't." The long answer is "you need to update your
local copy, and if it's still broke get in touch with upstream about it." So
even though your hardware might not be supported, you can still download
something and make it work. If you build your own kernel, know C well enough
to debug FTBFS and don't mind losing support from Ubuntu kernel devs. So in a
malevolent sense, the Ubuntu UK guy was right -- not only do you (in posession
of newer than six month hardware) need to download and build drivers from the
net, **most of you straight up can't.** Somehow I don't think they quite meant
it that way.

This isn't specific to Ubuntu or Linux. Microsoft carries a lot of drivers,
but recognizes that they have to support new hardware released after them.
Hence in Windows XP you have a floppy disk to provide the SATA drivers that XP
didn't have the foresight to include. There appears to be [ a way to do
this][4] but it's not documented, and [historical][5] [sentiment][6] (fun
drinking game: drink every time someone mentions Ubuntu in a Debian political
debate) tells me they're not interested in helping out some poor guinea pig
install Ubuntu.

Going forward, technologies like DKMS and practices like [stable release
updates][7] can breath some life into this problem, but it's every bit social
as it is technical. **I think people have a bit of a right to be irate when
they're promised something that isn't true**, and I hope Ubuntu Marketing and
everyone else understands this and agrees.

   [1]: http://www.ubuntu.com/community/conduct

   [2]: http://podcast.ubuntu-uk.org/2008/07/16/s01e10-easy-come-easy-go/

   [3]: http://irclogs.ubuntu.com/2008/07/19/%23ubuntu-kernel.html

   [4]: http://wiki.debian.org/DebianInstaller/FAQ#head-2522460048fd92cb8a53c3c0f176ca741033be57

   [5]: http://www.netsplit.com/2006/09/02/having-left-debian/

   [6]: http://people.debian.org/~mjr/irc/dpl-debate-2007/dpl-discuss.html

   [7]: https://lists.ubuntu.com/archives/ubuntu-devel/2008-July/025726.html

