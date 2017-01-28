Title: N900 Eulogy
Date: 2012-11-23

[3 years ago][1], Nokia released an intriguing option into the smartphone
market. The N900 was a true Linux phone, and a simple, freely available app
was all you needed to get root access to your hardware. The N900 was not a
massive hit with carriers, and not a massive hit in the market by extention.
That subsidy is pretty important for the US market. Of course, they faced a
variety of other problems competing in this market. Time to market, developer
support, economies of scale, feature parity, etc.

My exit two months ago is due to the notoriously flaky USB / charger port finally
failing. But today I want to focus on the software flaws rather than financial
or hardware. I ended up relying on this phone for a number of purposes. It
was an alarm clock, camera, PDA, mp3 playerphone, flashlight, remote terminal,
wireless keyboard and mouse, calculator, watch, and USB drive. A veritable
electronic multitool. But this digital convergence comes at a price: it's
also a large Single Point of Failure. It's a bit awkward falling back to using
a spare Nintendo DS as your wake up alarm.


Thorns
======

Beyond the aggregate, there are some specific pain points that were never
adaquately solved:

**Calendar Sync**. In a bizarre twist, the only protocol supported by the
both N900 and Zimbra was Exchange. I had set up davical on the theory that
desktop and phone would support CalDAV, but apparently, despite being based
on evolution, the N900 calendar has disabled CalDAV support. But hey,
there's a Exchange for Maemo app. So you know, as long as it works for the
narrow circumstances in which their developers operate, no problem? Sigh.

**Google IMAP**. For whatever reason, connecting to gmail via IMAP takes
ages. I think it's missing IDLE support? Or perhaps it's just not very
good at requesting data in chunks--gmail encourages leaving everything
in your inbox.

**Browser**. Three browsers, none terribly good. Fennec is slow to load
and render, and the built in browser is outdated enough that gMail is
basically broken on it.

**Installable apps**. This is a mixed blessing. Maemo never saw the
massive developer influx that Android has. It also doesn't have nearly
as much crapware or other privacy invasive free apps that Android seems
to implicitly encouraged.

My own ideas for apps turned out to be infeasible; those barode laser
scanners are tuned for specific frequencies, so you can't just display
or generate a picture. The flashlight eventually got implemented, but
is slightly annoying due turning on the camera app when opening the
lense cover. The relatively rapid Meego announcement dramatically
terminated any interest in the platform, so few were surprised when the
the "burning platform" memo was leaked.


Roses
=====

One thing the Maemo platform did right, however, was their plugin system.
Rather than a Flickr app and a Picasa app and so on, almost all basic apps
relied on a Sharing API, so that one could install and register plugins
providing it. You'd take a picture and select from your providers where it
should be delivered. I had a plugin for the gallery2 webapp, for example.
Similarly, their Conversations app integrated SMS and the whole libpurple suite
into one consistent UI. Adding new protocols was simple, and you could merge
contacts into a consistent view.

The Linux OS does offer app devs a few useful improvements over the Android
interfaces; to [the best of my knowledge][2], there is no Android version
of [BlueMaemo][3], a Bluetooth keyboard emulator that requires no custom
software on the other side. And it came with a suite of open source tools
relatively easy to build and ready to go.

Being available off contract was a huge boon; I was able to get many of
the benefits of a smartphone without being held to a pricey data plan. For
plenty of people, wifi is available in the home and the office, so it's not
a huge a sacrifice as it might seem. Combined with Skype and other VOIP
apps, it's not super hard to get by with a 100 dollar a year voice only plan.


Moving on
=========

Clearly Maemo/Meego are dead and buried. Jolla has a huge market share
disadvantage; every minute they don't have a device in user's hands is a
moment someone is buying, and thus funding, a competitor. Case in point: I
bought a Galaxy Nexus as a replacement. It will be quite a few years
before Jolla will get a shot at converting me. And it will be a tough sell.
Google's Nexus line offers no contract, no carrier crapware phones, and the
pace of updates has been incredible.

   [1]: //www.pwnguin.net/n900-arrival-and-notes.html

   [2]: http://android.stackexchange.com/q/4538/1698
   
   [3]: http://www.valeriovalerio.org/?page_id=174
