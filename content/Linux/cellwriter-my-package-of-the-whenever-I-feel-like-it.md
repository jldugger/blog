Title: Cellwriter - My package of the whenever I feel like it
Date: 2008-07-09

[As promised][1], I've put together a short screencast demoing Michael Levin's
handwriting recognition tool [CellWriter][2]:

([Link for those who don't see a video above][3])

The premise is that you write in cells so the tool can do individual letter
analysis. You _must_ train it on your handwriting for now -- no default
profile is provided. This means substantial work for Latin-based language
speakers, and insurmountable challenge for Asiatic languages.

### More useful than you'd think

You can use it with a regular mouse, but Cellwriter is intended for use with
stylus inputs, like tablets or touchscreens. The software consults with a
number recognition engines to determine the input to a given cell: a stroke
preprocessor (to accommodate different stroke orders and digitizer aliasing),
average distance of the input from sample input, average angles, and frequency
weighted word context.

Tablet input might seem like a slow and silly idea, but it's useful in a
number of places:

  * Devices without a real keyboard. Nokia internet tablets come to mind.

  * Settings where a laptop screen between you and another person forms an
unwanted barrier. Classrooms are a good place where an LCD display can be a
barrier between you and the lecturer and the chalk board, and a distraction to
those around you.

  * Text input to drawing applications. Sometimes you want to add some nicely
rendered text to a drawing, but don't want the hassle of rotating the screen
to get access to the keyboard.

  * Airplanes. Coach is a crowded space, and laptops sometimes fit poorly.
Tablet input can reclaim some of the space the airlines keep taking from you
in the name of efficiency. I've yet to test this theory, however.

### Patches Welcome

CellWriter is a young project, and there are still a number of areas where
Cellwriter needs more help:

  * **Default trained database**. For some languages the sheer number of
characters is overwhelming, and attempting to train for an individual is
farcical. Creating and using default data set would improve immediate
usability for both Latin and non-Latin languages.

  * **Internationalization**. Levin is [reportedly working on gettext
support][4], which is an important first step. From there community
translation services like [Rosetta][5] can aid in bringing the tool to a wider
audience.

  * **Librarification**. Currently CellWriter is a GTK application; there is
an open invitation for [volunteers][6] to split the code into a reusable
library, as well as a Qt UI for KDE. This could be very useful, if say you
wanted GNOME Sudoku to support handwriting input, or a KDE native UI version.

  * **Bug fixing**. A number of bugs still exist in CellWriter; if you have
experience with GTK and struts, [this bug][7] could use your expertise.
Additionally, the video above highlights a number of minor UI flaws, some of
which I'm told are going to be fixed in the next release. Any bugs, patches or
feature requests can be reported at [the Launchpad Project][8] page, or on an
impromptu [forum as bug tracker on Risujin][9].

### Get it today

You can easily install CellWriter in Hardy or Intrepid:

![][10]

Or you can install it in Debian with

> apt-get install cellwriter

Thanks to Michael Levin for his continuting work and to [UROP][11] for making
it all possible!

   [1]: http://pwnguin.net/hello-planet-ubuntu.html

   [2]: http://risujin.org/cellwriter/

   [3]: http://jldugger.blip.tv/file/1054074/

   [4]: http://forum.risujin.org/index.php?topic=4.0

   [5]: https://translations.launchpad.net/

   [6]: http://forum.risujin.org/index.php?topic=3.0

   [7]: https://bugs.launchpad.net/cellwriter/+bug/179107

   [8]: https://bugs.launchpad.net/cellwriter

   [9]: http://forum.risujin.org/

   [10]: http://farm4.static.flickr.com/3241/2650792995_d41fe88e62_o.png

   [11]: http://www.urop.umn.edu/

