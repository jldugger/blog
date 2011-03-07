Title: Limesurvey notes
Date: 2010-12-19

The local LUG group is small and shrinking, due to weak recruiting efforts and
a failure to strike a balance between student oriented and staff oriented
events. In fact, the website appears to be down today. I take some of the
blame here, but we can also blame Canonical for making Ubuntu too easy and too
popular -- the last installfest, the mainstay of LUG events, was basically
unattended save for some Wii gaming courtesy of the ACM student chapter.

In fact, pretty much the only thing that gets students' attention these days
is video games. So it's time to adapt. If students don't want or need
installfests, we should find out what they do want and work with that. With
that in mind, I decided I should prepare a survey for a games related event.
Coworkers have used SurveyMonkey in the past, but have been upset about the
bait and hook approach. In googling for SurveyMonkey alternatives, I came
across [Limesurvey][1] (formerly PHPSurvey). It appears to be a nice OSS app
that approaches the same features as SurveyMonkey.

Unfortunately, it's not yet packaged in Ubuntu, only [Debian experimental][2].
So the rest of this post shall be dedicated a technique I've adopted for
coping with this. Particularly, the svn:externals property, which allows for
nested checkouts.

### svn:externals

A few months ago, I finally took the plunge and set up [svnhome][3].
Technically, git is all the rage these days, but SVN should import into git
without loss of information at a later date, and it's professionally relevant
right now for me to dig into advanced SVN features. This does involve a lot of
svn:ignore properties, and at first I was really trigger happy with the
ignore. Originally, I ignored my src/ directory, but since they're mostly SVN
checkouts, I might as well use svn:externals, to document what I've got and
where it came from.

What makes this a bit complicated is that I want to combine the LimeSurvey SVN
checkout with the debian packaging that's also in an SVN collab-maint branch.
That, and they're both external to my homedir structure. Originally I had
chained the externals, marking LimeSurvey external in the homedir repo, and
the debian/ directory external to the limesurvey checkout. The problem is I
don't have commit rights to the LimeSurvey repo, so I can't commit an
svn:external in one computer and use svn update to duplicate the setup
elsewhere. Some might propose that I should just svn export LimeSurvey, and
merge it into my homedir repo (or not at all). I don't like it because it
makes it harder to send patches upstream and pull patches from them.

The solution I've settled on is to define the debian checkout from the src/
dir:

> limesurvey
https://limesurvey.svn.sourceforge.net/svnroot/limesurvey/source/limesurvey

>limesurveydebian svn://svn.debian.org/svn/collab-maint/deb-
maint/limesurvey/trunk/debian

From the limesurvey checkout point of view, this does leave debian/ as
unversioned, so I'll have to think harder about it or live with the
questionmark. Perhaps bzr has a clean way to integrate all this.

But for now, I move on to building and installing. One minor challenge is that
apt doesn't have a package to grab build depends from, so I have to do that
manually. And LimeSurvey pulls in a LOT of libraries, some of which are
packaged already, some of which are not. At least a few are bundled in other
apps like PHPMyAdmin, so that'll be something to look at for collaborative
improvement. And I should probably design and run that survey to start
rekindling the LUG!

   [1]: http://www.limesurvey.org/

   [2]: http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=472802

   [3]: http://joey.kitenet.net/svnhome/

