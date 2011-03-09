Title: A plan For anime
Date: 2007-11-30

I guess you could say watching fansubbed anime's a pastime of mine. The two 
most common distribution methods these days is IRC and bittorrent. I've built 
up a small ritual around it:

1. Check a site like [TokyoTosho][1] for new shows. 
2. Download the torrent, and pass to azureus.
3. Allow azurues time to download, and maybe seed. 
4. Watch.

Its a process I've honed over the years. Recently, I've been trying to make 
the ordeal smoother. Starting backwards, I guess. 

gMPlayer doesn't integrate with desktops very well, or show subtitles by 
default, so a few months ago I wrote a nautilus script to pass suitable 
options to mplayer. It's a very small script based on another one I found 
on [g-scripts][2]. Totem's getting better, but performance still tanks hard on
mkv for unknown reasons. 

The next step is making bittorrent itself a bit more automatable. [Azureus][3],
like all java programs is a big footprint kind of program. It takes somewhere 
between 30 and 50 Megs of RAM. And it tends to crash. Hard. So hard it crashes 
on restart, until you remove, of all things, the log files. So I'm currently 
looking for a replacement for Azureus. For all it's weight, Azureus does a 
good job of staying up to date and has lots of great tech. DHT, upload/download
limiting, etc. There's even a plugin to handle RSS feeds, which is good for 
automation (more on this in a second). 

Right now I'm looking at [Deluge][4] as a replacement for Az. It's got a bit 
more control over when and why torrents are closed, and appears to take around 
10 megs at idle. I should probably do smarter measurements of RAM use while 
actually running a torrent, but it's a good sign at least. But what counts is 
download time. Many people in the local LUG moan that their torrents never go 
fast, I've never had that problem with Az and I don't intend to go back to 
such times. 

The third step is has a couple options at the moment. Both Azureus and Deluge 
support RSS subscriptions. I'd prefer not to have a bulky torrent running in 
the background all day not doing anything though. I do however, use a tool 
called [Liferea][5] in the background on my desktop. I've been moving a lot of 
stuff over to Liferea, and this is also a candidate. Liferea has an option to 
download enclosures and launch an application on them. In this case, I'd run 
Deluge or Azureus. Not sure how to close them when they're idle again, as 
bittorrent authors prefer that people always be running their program and 
seeding. A big problem currently is that liferea doesn't handle MIME types, 
even though the enclosure protocol specifies their existance. It's mostly a 
matter of laziness on mine and the author's part. I've fixed the parsers to 
handle MIME types, but that's just the first part of several changes.

The final step is to actually create an RSS for just the things I'm interested 
in. US TV has [tvrss][6], which does a good job of making RSS feeds from sites 
like mininova. Anime doesn't have that, but it does have several dedicated 
sites like mininova. This is where [Yahoo! Pipes][7] comes in.  It's like a 
flowchart for UNIX pipes. Most unix pipes aren't very complicated though. They 
mainly just filter or transform things and pass them on to the next guy in 
line. Ideally, Yahoo!'s system allows for splitting pipes in far more 
intelligent ways than tee ever did. In practice it's a bit frustrating to 
write a complicated Pipe, as their loop operator doesn't take operators 
itself. You have to sort of build them out of string manip and regexp's. Fun 
times.

Here's an explanation to [the pipe][8] design. In order to get the very latest 
torrents, RSS feeds from several sites (instead of just one) are pulled in and 
merged. Then it filters based on user provided parameters. What's left should 
be your series, in chronological order. Then we normalize the feed, as each 
site offers different data. Some tools, like Liferea, only work on enclosures, 
not links. So the pipe sets those values up, and bam, [broadcatching][9] 
complete.

If you've made it this far, I'm open to questions about patching liferea, 
suggestions on other feeds to aggregate, bug reports, and alternative 
bittorrent clients.

   [1]: http://tokyotosho.com/?cat=1

   [2]: http://g-scripts.sourceforge.net/

   [3]: http://azureus.sourceforge.net/

   [4]: http://packages.ubuntu.com/deluge-torrent

   [5]: http://liferea.sourceforge.net/

   [6]: http://tvrss.net

   [7]: http://pipes.yahoo.com/pipes/

   [8]: http://pipes.yahoo.com/jldugger/anime

   [9]: http://en.wikipedia.org/wiki/Broadcatching