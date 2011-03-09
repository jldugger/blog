Title: Why isn't Arduino in Debian / Ubuntu?
Date: 2009-08-12

After [my review][1] of the Sparkle Labs **Discover Electronics!** kit I
thought I'd look for related software in Ubuntu. I did find [gResistor][2]
(Hat tip: Debianized by [tuxmaniac][3]), and some drafting tools. But I also
found a lot of stuff that wasn't in Debian or Ubuntu.

For example, [Arduino][4] makes an interesting platform for hobbyists,
students and apparently artists. It's lineage is confusing, inheriting from
both [Processing][5] and [Wiring][6]. I'm not yet clear whether Wiring is a
language, hardware or an IDE, but it in turn is based on Processing and adds
some microcontroller-y stuff as I understand it. Processing is a language and
IDE, and has been used for [amazing things][7]. It's all open source, and
reportedly works on Ubuntu. People have built [amazing][8] [things][9] with
the Arduino platform as well.

Strangely, hub of activity hasn't resulted in a .deb package, only a two year
idle [Request For Package ][10] for Processing, and nothing on the subject of
Arduino's IDE. Having packaging available for this stuff can do a lot to
remove trip ups for budding developers and artists. I'd much rather they spend
their time fixing their own bugs rather than trying to remove any bugs in
integrating the platform with Ubuntu. Does anyone know why or where these
efforts have stalled out? Is it legal issues, build problems, or just too
convenient already?

   [1]: http://pwnguin.net/an-electronic-diversion.html

   [2]: http://packages.ubuntu.com/gresistor

   [3]: http://www.tuxmaniac.com/blog/2008/07/26/gresistor-is-now-debianised/

   [4]: http://www.arduino.cc/

   [5]: http://www.processing.org

   [6]: http://www.wiring.org.co

   [7]: http://www.aiga.org/content.cfm/the-amazing-visual-language-of-processing

   [8]: http://www.kellbot.com/2009/05/life-size-katamari-lives/

   [9]: http://gizmodo.com/5028377/amazing-wii+like-3+d-controller-interface-built-with-foil-wiring-resistors-and-arduino

   [10]: http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=433270

