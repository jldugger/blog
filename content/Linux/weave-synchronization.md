Title: Weave synchronization
Date: 2009-12-06

During the transition from Firefox 2.0 to 3.0, [Google Browser Sync][1] was
lost to the churn of time and API. This plugin encrypted and synchronized your
browser history, tabs and cache among browsers. Since it's disappearance, many
people seem to recommend [Xmarks][2]. While Xmarks is a fairly robust bookmark
sync tool, it neglects other aspects of a profile like cookies or history,
making it harder to recommend. Conceivably, Ubuntu One could handle Firefox
profiles the way it handles Tomboy and Evolution contacts, but for now, the
only plausible comprehensive option is Mozilla's own offering, [Weave][3].

Weave is a browser sync engine. The FAQ gives a brief summary of features:
[Weave Sync currently supports synchronization of bookmarks, browsing history,
open tabs, saved passwords, form entries, and selected preferences. Security
settings will be added in a future release.][4] Yes, even _tabs_. If you leave
a tab open on your work box you can copy it to another box (the remote tab
remains open). Password recall is advertised as useful for mobile phones; pull
complex passwords into your phone's [Fennec][5] and skip the tedious
caps/numlock/funky character disaster. All of these are configurable, so you
can prevent disclosure if you fear distributing passwords to multiple boxes,
or fear distributing to Mozilla's hosting service.

I tried giving Weave a spin around a year ago, but it wasn't quite open to
public use. There were hints to use WebDAV enabled servers on your own, but
the only server code published was more a code testing server (since retired I
think), and the plugin outright refused to work without a valid Mozilla labs
account, at a time where such accounts were invite only. In fact, I think I
couldn't even download it without someone with an existing account giving me
the URL; not exactly a participatory open source experience to say the least.

But that was then and this is now; they've made regular progress on Weave and
are ramping up for a 1.0 release. Since I've ordered a n900 smartphone, I
decided to spend the Thanksgiving holiday setting up a personal Weave server
to populate its browser with data quickly. I did more research, consulted the
web and documentation, even queried a few IRC channels for user's opinions. It
seems they've opened registration to the general public, and there's a new
[lightweight server][6] published that relies on PHP and SQLite. I've set it
up on my personal server to see whether things have improved; when my phone
comes in I'll also test integration with Fennec.

It's fairly young, but inherits many design decisions from prior Weave
servers, so it should catch up quick and the smaller scope is an advantage.
One minor problem is that its only published via tarball and uses (part of) a
blog for a website, which does not instill confidence. But with only like five
files and no build, it should be trivial to package or even fork and maintain
if necessary. And I have it on good authority better publishing is [under
consideration][7].

Of course, it would be a bit silly to package a server [without the
client][8]. If Mozilla announces it formally soon enough, 1.0 plugin and a
minimal server could plausibly be in Ubuntu 10.04. So far, the server seems to
be working in proper order, but it'll take more and wider testing to have
utmost confidence in it.

### Server Install Notes

  * Apache runs as www-data on Ubuntu, so make sure that user has write
permissions on the database and read/execute on the PHP code.

  * Dependencies are fairly obvious: php5-sqlite, php5 and php5-cli (to create
your user). It feels a bit goofy to use PHP for CLI scripting, but I guess in
some situations it reduces dependencies.

  * If you self-sign a certificate, you need to store an exception on every
browser used. Or replace it with trusted SSL cert.

  * After a week of initial use, my database currently sits around 5MB; I'm
not sure how fast that will grow over time. Probably not much worse than a
local FF profile grows.

### A note to Mozilla

There's something like three versions of Weave documentation floating around
on your wiki, and Google search likes the oldest one best. Probably because
even your FAQ links to the oldest server documentation. I expect you don't
want this, and should probably take action to change it. Perhaps if
documentation had a "current version" alias, people could link to that instead
of a specific version destined to go out of date, and warning boxes could
appear when viewing old versions. If you need software online help to
reference versioned documentation, perhaps you could, you know, use the built-
in wiki version control?

   [1]: http://www.google.com/tools/firefox/browsersync/

   [2]: http://www.xmarks.com/

   [3]: https://mozillalabs.com/weave/

   [4]: https://wiki.mozilla.org/Labs/Weave/FAQ#Firefox_Mobile

   [5]: http://www.mozilla.org/projects/fennec/1.0a1/releasenotes/

   [6]: http://tobyelliott.wordpress.com/2009/09/11/weave-minimal-server/

   [7]: http://tobyelliott.wordpress.com/2009/09/11/weave-minimal-server/#comment-136

   [8]: http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=556135

