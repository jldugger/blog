Title: On synchronization and "the cloud"
Date: 2010-06-09

I've been meaning to do a followup post on N900/Maemo5, but every time I
summon the effort to start drafting the post, a new firmware comes out to
address problems motivating the post. Case in point: the most recent firmware
(PR1.2) finally added the USSD code support one needs to query Tmobile about
money left on prepaid accounts (a fantastic money saver for me).

But one thing that has become readily apparent is why people are so excited
about "the cloud". Roughly speaking, the non-technical and [semi-technical
people][1] who use that term mean something other than _elastic computing_. As
best I can tell, what they're after is an _online datastore / network API
that's on 24/7_. Which can be neat, but isn't the revolutionary thing you
might imagine based on the rhetoric.

Anyways, about that neatness: after a few months of smartphone ownership it
became apparent that I need some way to deal with the fact that all of my
devices create and store new data sources, but none of them are on and
accessible 24/7. Solutions like [unison][2] remain academic because they are
neither automated nor available 24/7. Essentially, it seems **people are
rediscovering the value of mainframe computing**, but with redundancy and
graceful degradation to offline mode. Maemo5 meets this concept to varying
degrees of success.

### Music

Synchronizing music libraries is relatively simple, and even Banshee supports
it. Simple file sync tools like unison are also admissible to me because
generally speaking, I don't add much music very fast and changes needed
immediately. But there's a side problem here: hidden data. Music ratings are a
great tool I use to create shuffle playlists of minimally acceptable music.
Because the MP3 format does not include this admittedly subjective rating
field, it's not sufficient to sync files to get this data. It's become clear
that **the tight integration iTunes offers by sharing metadata between desktop
and device is pretty damn useful**. Granted, they're impossible to get out,
and people sometimes accidentally wipe their ratings stored on iPods, so
perhaps the grass is just greener on the other side of the electric fence.
Perhaps I should see if something like Last.fm / Libre.fm can play a role in
collecting and syncing this data.

Maemo5's media player doesn't provide a rating concept, so there's nowhere for
this data to be put on the device for smart playlists. I hear that Meego took
a great step in the right direction by selecting Banshee as the media player,
so I hope the group takes time to address Banshee<->Banshee setting sync, to
meet or beat iTunes.

### Photography

Maemo does an outstanding job here with a great idea. The unit of software
deployment on smartphones is generally the app. Maemo's Sharing plugin system
does a superlative job of modularizing the upload process such that you don't
need a seperate uploader app for each hosting provider. There is a gallery2
plugin, which works well for me, and there's no shortage of other plugins if
you prefer not to self host. This deserves an A++ and I hope Meego keeps this
tradition.

### Bookmarks / History

Upon seeing that Mozilla was building their mobile Fennec browser for N900, I
decided to check out [Mozilla Weave][3]. It's a great replacement for an old
tool that was popular and canceled before the term "cloud" was cool: Google
Browser Sync. They've since rebranded it Mozilla Sync which maybe indicates
more clearly what the product does. Many people use Xmarks, but Sync also
handles history, preferences, even tabs. Mozilla offers a central service, but
I prefer to use the minimal standalone system that I can host myself. This is
probably the ideal -- people who want privacy have a number of steps they can
take, while there's still an easy to use compliment. Interestingly, Meego has
chosen Chrome as it's default browser, and the state of the art in cross
browser sync is bookmarks only (I can't imagine sharing preferences between
browsers being useful).

### Calendar & Organizer

I've lately been experimenting with calendars and todo lists at work. For
example, I have "package weave-minimal for Ubuntu" as a todo item. At work we
have Exchange and Outlook. At home I have Evolution, which integrates with the
desktop in some neat ways I'd like to keep. Surprisingly, Maemo supports
Exchange very well. Calendars / alarms, todos, notes, etc. all come across
fine, and PR1.2 even generates responses to meeting invites. Ideally, I'd keep
work and personal data separate and let the phone unify them for presentation,
but I've yet to find a way to do that -- CalDAV support is not in Maemo. The
good news is that I've seen a few emails from Nokia developers that suggest
CalDAV might work in Meego. Guess it's time to set up a personal CalDAV server
and point Evolution at it.

As far as contacts go, I generally just centralize it on the SIM card and
leave it there, but I think Ovi has a system in place, and [syncML][4] has
rough support.

### Conclusions

I don't know why this form of cloud computing is popular now, when many of the
same problems and solutions have been around since laptops and wifi. Perhaps
the pocketability and utility of cellphones cancels out the "nerd factor"
associated with carrying around laptops, so that people now run into these
problems daily rather than just during offsite business meetings. Either way,
there's plenty of technology to support private cloud systems; I use gallery2,
weave and (soon) CalDAV privately to synchronize my computers.

Frankly, the greatest remaining challenge I have left is storage. In contrast
with [jzawodny][5], S3 doesn't even come close to making economic sense at
personal scales of a couple TB, and Dropbox is even more pricey with less data
at end. For now I'll just take the availability risk of residential networking
and save the money.

   [1]: https://sites.google.com/site/traininginthecloud/

   [2]: http://www.cis.upenn.edu/~bcpierce/unison/

   [3]: //www.pwnguin.net/weave-synchronization.html

   [4]: http://wiki.maemo.org/Sync

   [5]: http://jeremy.zawodny.com/blog/archives/007624.html

