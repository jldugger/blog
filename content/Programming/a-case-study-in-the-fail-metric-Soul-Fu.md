Title: A case study in the FAIL metric: Soul-Fu
Date: 2009-05-29

Tom Calloway posts [a metric for evaluating open source projects][1], which I
shall dub "FAIL, Assessing Inadequacy Lazily" (FAIL). To help calibrate the
scales, I'll provide a case study: [Secret of Ultimate Legend Fantasy
Unleashed][2] (Soul-Fu).

### About Soul-Fu

Soul-fu is the brainchild of Aaron Bishop, original author of [Egoboo][3].
They are both dungeon crawler games, with an emphasis on action and influence
from Nethack. It's original platform was apparently Windows, but the author
justifies some code by claiming game consoles were also targeted. Like Egoboo
before it, Soul-Fu is largely abandoned by its creator and the source code
provided to all takers on a custom license.

Technology wise, the game includes openGL rendering and cel shading. Shadows
are cast from characters and enemies, and equipping armor and weapons changes
your appearance in game. Animations involve skeletal motion and are generally
decent.

In Aaron's absence, a modest community has organized around the official
message board, to mod and hack the code. Mod'ing the game involves loading up
a text editor in game, modeled after emacs(!).

So how does this game fare on the FAIL scale? Let's find out.

*Applied points of fail in bold*, _editorial comments in italics_

### Size

_The community SVN helpfully checked in all the game data along with the code
to a single project, but it manages to still fit within 100MB_

  * The source code is more than 100 MB. [ +5 points of FAIL ]

  * If the source code also exceeds 100 MB when it is compressed [ +5 points
of FAIL ]

###  Source Control

_The Soul-Fu community runs their own SVN server, after it was discovered that
SourceForge didn't approve of the license._

  * There is no publicly available source control (e.g. cvs, svn, bzr, git) [
+10 points of FAIL ]

  * There is publicly available source control, but:

  * There is no web viewer for it [ +5 points of FAIL ]

  * There is no documentation on how to use it for new users [ +5 points of
FAIL ]

  * You've written your own source control for this code [ +30 points of FAIL
]

  * You don't actually use the existing source control [ +50 points of FAIL ]

###  Building From Source

_Soul-Fu originally built via VC.NET; someone later wrote a simple Makefile to
get the job done on Linux. These Makefiles have been reverted in SVN, so it's
hard to judge this section. To promote clue, we'll say anything not in SVN
HEAD doesn't count._

  * There is no documentation on how to build from source [ +20 points of FAIL
]

  * If documentation exists on how to build from source, but it doesn't work [
+10 points of FAIL ]

  * Your source is configured with a handwritten shell script [ +10 points of
FAIL ]

  * Your source is configured editing flat text config files [ +20 points of
FAIL]

  * Your source is configured by editing code header files manually [ +30
points of FAIL ]

  * Your source isn't configurable **[ +50 points of FAIL ]**

  * Your source builds using something that isn't GNU Make **[ +10 points of
FAIL ]**

  * Your source only builds with third-party proprietary build tools **[ +50
points of FAIL ]**

  * You've written your own build tool for this code **[ +100 points of FAIL
]** _In game scripting is done with a custom language, PXSS, and it's own
compiler. There's also the conversion of game data to a single file, but I
might forgive that here._

###  Bundling

_Soul-Fu was originally published requiring a custom libjpeg. This has been
fixed in SVN._

  * Your source only comes with other code projects that it depends on [ +20
points of FAIL ]

  * If your source code cannot be built without first building the bundled
code bits [ +10 points of FAIL ]

  * If you have modified those other bundled code bits [ +40 points of FAIL ]

###  Libraries

_Soul-Fu builds against a number of freely available libraries such as SDL,
ogg, and openGL_

  * Your code only builds static libraries [ +20 points of FAIL ]

  * Your code can build shared libraries, but only unversioned ones [ +20
points of FAIL ]

  * Your source does not try to use system libraries if present [ +20 points
of FAIL ]

###  System Install

_The most Soul-Fu has for installing is a .nsi for Windows bundles, and even
that doesn't appear to be in SVN HEAD. I wrote debian packing for it, but
Soul-Fu itself has a snowball's chance in hell of distribution inclusion._

  * Your code tries to install into /opt or /usr/local [ +10 points of FAIL ]

  * Your code has no "make install" **[ +20 points of FAIL ]**

  * Your code doesn't work outside of the source directory [ +30 points of
FAIL ]

###  Code Oddities

_Honestly, the code itself has a host of oddities that might merit it's own
categories, but we're trying to use simple and objective metrics as a stand-in
for intelligent analysis._

  * Your code uses Windows line breaks ("DOS format" files) [ +5 points of
FAIL ]

  * Your code depends on specific compiler feature functionality [ +20 points
of FAIL ]

  * Your code depends on specific compiler bugs [ +50 points of FAIL ]

  * Your code depends on Microsoft Visual Anything **[ +100 points of FAIL ]**

###  Communication

_Soul-Fu's hub of activity is a phpBB forum. Theoretically, the original
author has a mailing list, but I don't think it's available for community
use._

  * Your project does not announce releases on a mailing list **[ +5 points of
FAIL ]**

  * Your project does not have a mailing list **[ +10 points of FAIL ]**

  * Your project does not have a bug tracker **[ +20 points of FAIL ]**

  * Your project does not have a website [ +50 points of FAIL]

  * Your project is sourceforge vaporware [ +100 points of FAIL ]

###  Releases

_Per the original author's guidelines, official community releases must be
approved by a vote. No such vote has happened yet. We'll give it a no release
mark and move on._

  * Your project does not do sanely versioned releases (Major, Minor) [ +10
points of FAIL ]

  * Your project does not do versioned releases [ +20 points of FAIL ]

  * Your project does not do releases **[ +50 points of FAIL ]**

  * Your project only does releases as attachments in web forum posts [ +100
points of FAIL ]

  * Your releases are only in .zip format [ +5 points of FAIL ]

  * Your releases are only in OSX .zip format [ +10 points of FAIL ]

  * Your releases are only in .rar format [ +20 points of FAIL ]

  * Your releases are only in .arj format [ +50 points of FAIL ]

  * Your releases are only in an encapsulation format that you invented. [
+100 points of FAIL ]

  * Your release does not unpack into a versioned top-level directory (e.g.
glibc-2.4.2/ ) [ +10 points of FAIL ]

  * Your release does not unpack into a top-level directory (e.g. glibc/ ) [
+25 points of FAIL ]

  * Your release unpacks into an absurd number of directories (e.g.
home/johndoe/glibc-svn/tarball/glibc/src/) [ +50 points of FAIL ]

###  History

_Soul-Fu was originally a solo project, intended for commercialization. As
such you will encounter stupid code and **intentional** obfuscation of data
objects. The metric may need revision to accommodate the level of peer review
code got while proprietary. An additional "original authors abandoned the
project when open sourcing it" criteria may be in order, for now we'll call it
a fork since the original is still available._

  * Your code is a fork of another project [ +10 points of FAIL ]

  * Your primary developers were not involved with the parent project **[ +50
points of FAIL ]**

  * Until open sourcing it, your code was proprietary for:

  * 1-2 years **[ +10 points of FAIL ]**

  * 3-5 years [ +20 points of FAIL ]

  * 6-10 years [ +30 points of FAIL ]

  * 10+ years [ +50 points of FAIL ]

###  Licensing

_The code is licensed under what can only be called a custom "Be Nice"
license. I actually asked the OSI to rule on it after the author claimed it
was okay and the OSI would approve it. The license itself is hidden within an
HTML manual, and generally states that it must remain nagware and
noncommercial. It also stipulates that official releases must see community
approval. On the bizarre licensing the author has not budged._

  * Your code does not have per-file licensing **[ +10 points of FAIL ]**

  * Your code contains inherent license incompatibilities [ +20 points of FAIL
]

  * Your code does not have any notice of licensing intent [ +30 points of
FAIL ]

  * Your code doesn't include a copy of the license text [ +50 points of FAIL
]

  * Your code doesn't have a license [ +100 points of FAIL ]

###  Documentation

_Soul-Fu code does not self document, and what passes for documentation are
some notes the author made while writing Soul-Fu._

  * Your code doesn't have a changelog **[+10 points of FAIL]**

  * Your code doesn't have any documentation [ +20 points of FAIL ]

  * Your website doesn't have any documentation [ +30 points of FAIL ]

##  FAIL METER

0 points of FAIL: Perfect! All signs point to success!

>5-25 points of FAIL: You're probably doing okay, but you could be better.
<br>30-60 points of FAIL: Babies cry when your code is downloaded

>65-90 points of FAIL: Kittens die when your code is downloaded <br>95-130
points of FAIL: HONK HONK. THE FAILBOAT HAS ARRIVED!

>135+ points of FAIL: So much fail, your code should have its own reality TV
show. 

**495 points of FAIL: Soul-Fu**.

This is why I have Soul-Fu patches and Ubuntu packaging, but am sitting on
them. It would be a drop in the bucket of failure.

   [1]: http://spot.livejournal.com/308370.html?view=1403794#t1403794

   [2]: http://www.soulfu.com/forums/index.php

   [3]: http://en.wikipedia.org/wiki/Egoboo_(computer_game)

