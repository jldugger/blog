Title: Backups galore
Date: 2009-05-02

I thought I'd do a quick survey and figure out what backup tools are readily
available in Ubuntu. I found 17 that might be worth mentioning. Many are
front-ends, and front-ends-to-the-front-ends, so to keep them straight I
cooked up a quick diagram with GraphViz:

[![backups galore][1]][2]

So there's a lot, and I may have missed a few nodes or edges. So far, my
favorite is probably mrb:

> Package: mrb Description: Manage incremental data snapshots with make

rsync mrb is a single, self-documenting, executable makefile, which aims to
make trivial the task of maintaining a set of compact, incremental, rsync
mirrors of your important (and sometimes rapidly changing) data. . It relies
only on the time-hardened industry tools GNU make and rsync. Snapshots may be
taken at any opportune interval. Multiple snapshot targets can be configured
in a modular fashion, so fast changing data can be separated from static bulk
data, with snapshots of each scheduled or triggered on demand, as may be
appropriate for each.

At first you think, "Perfect, how hard can a make frontend to rsync be?" 15
kilobytes of Makefile later, you realize this may not be as brilliant as it
sounds on paper. But it is well commented and relatively user friendly, which
may actually impede the code's readability (as if anything involving
whitespace syntax could be readable). Such gems as:


    # If I have to explain this one, then I guess you are just reading this

    # 'for the articles' -- but I hope you'll have enjoyed it anyway...


I haven't tried mrb yet, but I might put it on the TODO list. But first, I'll
need to give [jwz's method][3] a full vetting.

   [1]: http://farm4.static.flickr.com/3325/3492777989_9ec4ca0e1a_b.jpg

   [2]: http://www.flickr.com/photos/jldugger/3492777989/ (backups galore by jld5445, on Flickr)

   [3]: http://jwz.livejournal.com/801607.html

