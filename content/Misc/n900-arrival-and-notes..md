Title: n900 arrival and notes.
Date: 2009-12-10

The phone arrived, and I'm recording a few notes on initial experiences,
covering mail, the display, the browser, available apps, battery life.

**Mail**. "Mail for Exchange" worked fine, surprisingly. There are two popular
versions of exchange, 2003 and 2007. Last I checked 2007 wasn't supported by
Ubuntu (this may have changed but I'm afraid to test it for fear of destroying
my inbox or the server itself). There's a 'peak hours' mode that would be
better called 'work hours' to control when it should poll for mail. There's a
lot of complaints of gMail support on the forums. Need to test that more; in
addition to IMAP there's a mobile version of the webapp and the full version
works to some degree.

**Brightness**. Many displays are weak outdoors, due to the physics of LCDs.
Essentially, the two options available are to outshine the sun or reflect and
filter the incoming sunlight (transflective). Older Nintendo handhelds shipped
without any light source, leading some clever people to design LED light that
drew power from the gamelink port, or even open the device to mod it with an
aftermarket frontlight screen. Wikipedia reports the N900 is a transflective,
and it performs admirably in daylight.

**Browser**. I think I've tried this UI before on some other system images.
It's not bad, but the back button is form over function; when I want to go
back one click it has to first cook up a scrollable picture history. With
[Fennec landing on the N900 first][1], I'd be remiss not to give it a go, if
only for the Weave support.

**Installable apps**. Some quirky stuff going on, like a facebook app
_installer_ app and a facebook app. And to the best of my observation, the
installer app is larger than the app itself. I suppose at least it's not a
free trial. It looks like most of the fun stuff is sitting in satellite repos
like extras or garage?

On further inspection, there's a sort of [rolling release system in place for
extras][2], loosely modeled on Debian with perhaps clearer names: extras,
extras-testing and extras-devel. It looks like most packages reside in
-testing, and enabling -testing was similar to Ubuntu's software sources. On
the other hand, -devel has giant warning flags in the wiki.

**Battery life**. My friend Tom insists smartphones are power leeches, so I've
been trying to keep it on leash. On the other hand, it seemed to survive a
workday yesterday as I fiddled. It charges via microB, which sounds handy
until you realize the only microB cable you've got is the one that it came
with. We've got countless USB A->B from monitors but no microB. I should break
out the Kill-a-watt and powertop, and see what's going on.

**Self reported data.** I've captured some output from various Linux internal
documentation interfaces; I'll post them as comments later.

### App Ideas

Just a few random ideas I've had:

  * **Club Carder**. Capture and display barcodes for customer loyalty and
library cards. Preliminary testing with displaying photographed barcodes
suggests that the screen is not transflective, and may defeat laser scanners
measuring reflectance. Most of the reviews of the Android app that does this
don't attempt retail scan testing, so I may need to borrow a friend's device
for comparison. If it does work, integrating with GPS may help recall the
correct card for the correct situation.

  * **FlashTorch**. Apparently some LED flashes can be driven for longer. Just
finished a longish debate on the merits on #maemo, wherein it was determined
that the light can be driven in flash mode safely for .5s, and longer at 50mA
(less bright but supposedly not bad).

  * **GCStar scanner**. Barcode scanner integrated with GCStar or some other
personal inventory app. There's already a barcode scanner work in progress,
probably just need to concoct a plugin to direct the data.

  * **Cellwriter**. Should be possible to port it, the main problem is whether
it's actually faster, and whether one can override the onscreen keyboard with
it. It occurs to me that you could preload it with Graffiti or Graffiti 2, but
I doubt they're fast enough. In my experience, cursive is the way to go for
speed. There's certainly spare CPU to process it, but processing cursive
requires another error prone step we don't have yet.

   [1]: http://news.cnet.com/8301-30685_3-10411569-264.html?part=rss&subj=news&tag=2547-1_3-0-20

   [2]: http://wiki.maemo.org/Extras

