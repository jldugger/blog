Title: SVG vs PNG
Date: 2008-06-20

I've been testing some [software][1] recently that includes liberal use of
large program icons in Ubuntu. [Historically][2], Debian packages have used
[XPM][3] for icons, because they diff easily and are compressed already via
packaging. More recently, [vector graphics][4] have become popular in many
places in the desktop and the web with today's bigger and higher DPI computer
displays, because vector graphics are resolution independent. This makes for
neat stuff, like quick launchers and desktop icons that scale cleanly with
size:

SVGs are nice, but there's still a few reasons you might still use PNG.
They're far more plentiful -- even I'm guilty of converting a Windows .ico
into a PNG for an icon. And they take less disk space, since SVG is a verbose
XML, while PNG is a compressed format. But when size really counts, it also
possible to [compress SVG with gzip][5].

But times are changing. Linux, and Ubuntu in particular, is moving into
several different devices with different resolutions, aspect ratios and
display sizes. Lots of technology is needed to cope with the diversity, as
[Shuttleworth noted][6] (33:30 timestamp). SVG plays a role in coping
resolution and size. This screencap demonstrates how stark the difference is
on my laptop:

![Blown up comparison between PNG and SVG][7]

So what's holding widespread SVG on Ubuntu back? Disk space is a minor concern
on the most constrained devices that Ubuntu could run on, but I think that's a
wash when you start storing 5 sizes of icons versus one scalable graphic.
Render time is an interesting question that depends on a host of factors. If
we assume standard icon bitmap sizes, I would imagine it's a win for PNG. If
we remove that restriction, you have to throw in the cost of scaling the PNG.
[Bryce Harrington,][8] Ubuntu X developer and Inkscape founder, offered the
following insight:

> < bryce> svg supports advanced functionality like filters, gradients, etc.
which can be processor intensive for some chipsets

> < bryce> however a really trivial one - just some simple shapes of
solid colors - could actually render faster <br> < bryce> filesystem I/O tends
to be a major performance killer, so any optimization which allows you to
avoid file I/O at the expense of processor or memory, tends to work out pretty
well

Bryce went on to suggest that tricks to rescale both PNG and SVG by raster
lines were occasionally used in performance sensitive code. Gzip compressed
SVG might help under specific situations, since it reduces I/O and you can
pipeline some of it. But we're talking peanuts for icons, since most will fit
within a single small contiguous extent.

The most interesting argument I saw was from Johan Brannlund:

> < johanbr> Bitmap icons tailored for small sizes look better than SVG.

There's no easy way to dispute that. I don't think you'll find superb pixel
art coming out of SVG renders. I'm not sure it matters, but it helps. One
thing that can be done is see how many packages are actually customizing their
tiny PNG icons. Firefox [seems to][9]. Deluge might, I can't really tell the
difference between their PNG and the SVG. Pidgin is actually backwards here --
as far as I can tell, they generate SVG from PNG, yielding the worst of all
worlds. Carrier (aka "funpidgin" aka "that silly fork of pidgin") does the
same. So clearly all three practices are in use; it would be interesting to
see how common each practice is (and document new ones), but I'm not sure
there's a good way to do it. So if you see me filing bugs and tags in the next
few weeks, this is what's up.

   [1]: https://www.launchpad.net/netbook-remix-launcher (Netbook Remix Launcher)

   [2]: http://alioth.debian.org/docman/view.php/30046/2/menu-one-file.html#s3.7 (Debian Menu icon policy)

   [3]: http://en.wikipedia.org/wiki/X_PixMap (Wikipedia: XPM)

   [4]: http://en.wikipedia.org/wiki/Vector_graphics (Wikipedia: Vector Graphics)

   [5]: http://www.adobe.com/svg/illustrator/compressedsvg.html (Compressed SVG files are typically 50 to 80 percent smaller...)

   [6]: http://podcast.ubuntu-uk.org/2008/05/27/s01e06-flaming-star/ (I would like to see it work really well on a small screen)

   [7]: http://farm4.static.flickr.com/3154/2591515491_afe99f8277.jpg?v=0

   [8]: http://www.bryceharrington.org/drupal/blog/1 (Bryce's blog)

   [9]: iconpacks.mozdev.org (Firefox Icon packs)

