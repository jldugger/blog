Title: Why the video tag won't save us
Date: 2009-01-28

I see Mozilla is forking over [some cash to improve Ogg Theora][1]. It's a
nice symbolic gesture, certainly. But Mozilla is fighting an uphill battle, in
the snow, upside down and underwater. I've been sitting on this post for quite
a while, so this announcement is a good excuse to dust it off and finish it.
If you have a glimmer of hope that the <video&gt tag will somehow undo the
Flash dependencies that Google Video and Youtube hath wrought, I have news for
you. Flash video is the path of least resistance to what video hosting sites
want: **revenue.**

In 2007 a large consortium of engineers representing companies discussed the
adding [a <video&gt tag][2] to HTML. A number of [papers][3] were published
for the event, describing company's positions. Nokia wrote about how they need
hardware decoder support for whatever codecs are chosen. Mozilla wrote about
the need for an open and free "baseline" codec. Adobe's is surprisingly
insightful. Youtube seems to have the distinction of being the only company to
send a marketing rep to an engineering forum. An excerpt from their [position
paper][4] :

> It is estimated that the total revenue for online video will expand to $6.3
billion by 2012. Right now, online video content is responsible for an
estimated $538 million in the US alone. That may seem like a small slice of
the $20+ billion spent on online advertising in 2007, but consider this: while
online ad revenues are growing 26% per year, online video ad revenues are
growing 55.5% per year. The potential for Video monetization is clearly there
– just a matter of when.

I'm not misrepresenting Youtube here; their entire paper reads like this.
Reading between the lines of Youtube's otherwise incomprehensible position
lies the statement that delivering advertising is all they care about. Not
consumer preference, not [saving energy][5] or hardware support or bandwidth
consumption. Ogg and Javascript bring nothing to the Youtube table.

Youtube isn't alone; several video sites are banking not on banner ads or
customized channel pages, but on targetted per viewer ads, similar Google's
AdSense. A traditional broadcast video has markers for broadcasters to insert
ads, mixing them together in real time. These two ideas are fundamentally
incompatible. You can't mix in ads server side and still hand out targeted ads
to millions of people. Instead you can use Flash to overlay interactive ads on
top of videos and do the processing on client side, where there's a lot of
unused CPU. Some places have already started this, and it's quite annoying.
This practice is why Flash can't use Xv -- Xv is in CMYK, and the non-video
parts of Flash are in RGB. Hence the high loads when watching flash video; it
decodes the video into CMYK, converts to RGB, then draws crap on top of it,
and sends it to be drawn.

Video hosting sites are increasingly closing their services off behind walled
gardens in preparation for "monetization". There are well known scripts that
can retrieve the underlying video from a Youtube URL (and others), sans Flash
advertising. Nobody should be surprised to find out that it's against the TOS
to do so. When Google Tech talks migrated from Google Video to Youtube, they
lost their .mp4 video enclosures, never to return. Simple programmatic access
to hosted video is approaching impossible, restrained only by the need for
Flash player to access the same video somehow. This would normally be a step
backwards in **making the world's information searchable and universally
accessible and usable.**

### The good news

For sites that do offer direct access to video files, within the <video&gt tag
lies some great functionality. You can use the attribute markup to set time
markers ("a cue"), leading surfers directly to an excerpt of a larger video. I
was going to share an example here, but I commented it out after seeing that
pretty much nothing supports time markers yet.

Anyways, a lot is to be gained by this. You can quote exactly what a person
said, or select a segment or scene from a larger video corpus to share with
your audience. And you don't have to recut a video to do it, just let the
browser handle that. Building these controls into the browser lets you
entirely skip the cut and re-encoding and just grab what you need.

Some sites offer this function independently via URL parameters, but making it
standard brings a benefit beyond your direct audience. You can apply a lot of
the same techniques Google uses for regular links. If everyone uses the same
published syntax to cite clips within a larger video, engines can index sites
as they're discovered and instantly apply knowledge of the citation to the
region of time quoted, rather than waiting for a programmer to translate
another video hosting site's parameters. Search engines can apply annotations
to a larger video and perhaps even generate table of contents automatically.
Youtube is experimenting with annotations in Flash, and it's apparent they're
in dire need of something more pageranky to curb the abuse.

This all relies on a fast seek to make cues feasible. As far as I can tell,
none of the major vendors have even addressed this, even though the spec calls
for it. For example, can anyone explain what unit the start and end attributes
are measured in? Seconds would make sense, but it could be bytes if you want
to seek quickly.

So I applaud Mozilla's efforts and wish them success, but we're kinda ignoring
the elephant in the room here.

   [1]: http://www.0xdeadbeef.com/weblog/?p=977

   [2]: http://www.whatwg.org/specs/web-apps/current-work/#video

   [3]: http://www.w3.org/2007/08/video/positions/

   [4]: http://www.w3.org/2007/08/video/positions/Youtube.html

   [5]: http://mjg59.livejournal.com/80563.html

