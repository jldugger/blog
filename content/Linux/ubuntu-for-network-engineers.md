Title: Ubuntu for Network Engineers
Date: 2009-01-26

Keith Tokash posted a review of Ubuntu 8.04 [from the perspective of a network
engineer][1] who switched from Windows XP to Ubuntu. It's been picked up [at
Slashdot][2] as well. Rather than post a comment there, I thought I'd share a
more in depth response.

A quick synopsis before hitting individual points: much of the review centers
around Linux as embodied within Ubuntu, rather than the things Ubuntu brings
over the other Linux distributions. Balancing the praise are a few thorns,
places where Ubuntu isn't sufficient for his needs. On to a few specific
points, then.

He mentions that Evolution and Exchange don't get along well. This is hardly
news, and a significant barrier where I work as well. And frankly, it get gets
even worse than he reports. Evolution uses the Outlook Web Access (OWA) to
connect to Exchange. This works okay in Exchange 2003, but not Exchange 2007.
For people working in a large organization, you're unlikely to see a move to a
mail server with wider compatibility, but there's hope: [OpenChange][3] is
working on a library to implement MAPI, so clients can access Exchange on the
same terms as Outlook. I can't find it now, but there was some discussion
about getting Debian packaging going and getting this done in the Jaunty
timeline. It's by no means final, and won't help people preferring LTS, but by
the next LTS, I would think Evolution will connect to Exchange 2007. Hopefully
Exchange doesn't change much in the meantime!

He also mentions Visio, a diagram program. Visio is certainly a well polished
tool, and I've yet to find anything comparable. I hate dia, OpenOffice renders
like crap, and Inkscape's diagram tool isn't usable. GraphViz and dotty are on
my list to try out, but the lack of a GUI is going to put off a lot of people,
and frankly the screenshots give me no faith in their power to make things
pleasing. Most diagramming tools in Ubuntu revolve around UML in one way or
another.

He also cites the lack of a password manager compatible with PasswordSafe.
I've been looking into this myself, and as it happens, he's wrong. [Password
Gorilla][4] is a compatible program, in package password-gorilla
([available][5] since hardy). Unfortunately, if you search for "passwordsafe"
in the repos, Gorilla doesn't come up, which explains why he might not have
found it. Personally, I like KeePass 2.0 over PasswordSafe. Keepass works
great in Jaunty, not so great in Hardy or Intrepid. No package yet, but I may
publish one in a repo.

Finally, there's also a few complaints that are far more mundane. For example,
turning off 2-page view in Evince (GNOME's PDF reader). Instead of looking in
the View menu, he _installed Adobe's Linux PDF client_! Worth a chuckle, I
guess. (If you're reading Keith, it's a checkbox under View->Dual).

All in all it seems Ubuntu is doing a good job of putting together a coherent
desktop. Many of the rough edges are being worked on, but Visio remains a sore
spot for the foreseeable future.

   [1]: http://www.ccieflyer.com/2009-Feb-KTokash-Ubuntu.php

   [2]: http://linux.slashdot.org/article.pl?sid=09/01/25/037223

   [3]: http://www.openchange.org/

   [4]: http://fpx.de/fp/Software/Gorilla/

   [5]: http://packages.ubuntu.com/search?keywords=password-gorilla

