Title: GNOME a11y Contest
Date: 2008-08-05

Keeping with the theme of [money in Linux][1], today I present you [GNOME
Outreach Program: Accessibility][2]. The Program has raised $50,000 in pursuit
of three goals:

  1. Increase awareness of accessibility and its relation to computer
applications

  2. Encourage and inspire people to work on accessibility

  3. Help the free software community improve its accessibility

These come from [the rules][3] the front page encourages everyone to read.
Divided into Long-Term and Short-Term Tasks, the rules read more like a
sweepstakes than an employment agreement or contract. Still, the fundamentals
are oddly close to a work for hire: you perform a set of tasks, and are
rewarded with money. $6000 for Long-Term tasks, $200 for Short-Term tasks.

### Short-Term Tasks

On the subject of short-term tasks, [the tasks list page][4] says:

> Are you a developer who wants to become more familiar with accessibility?
Are you an artist that can draw? Maybe you might also be interested in
becoming a module maintainer some day. A great way to get started is by fixing
bugs, and we're offering you a way to get paid to do it. :-)

Short term tasks are two week affairs that pay out $200 each (in bundles of
five) a construction similar to Google's ["Highly Open Participation
Contest"][5]. Unfortunately, I doubt any of the people completing them expect
to claim any prize money. It's a simple matter of math: if any task takes more
than 30 hours, flipping burgers pays better (where I live).

Bundling by fives is crazy. It discourages participants simply by the unknown
quantity of effort and massive investment before payout. But it gets worse. A
sufficiently clever person can nullify all monetary incentive for some tasks
and **a sufficiently conscientious person will avoid completing tasks they
don't intend to claim a prize on.** An example: there's only five "Create 10
Accessible Icons" tasks posted. Completing one task effectively reserves the
rest for you. Certainly, if you try one, finish it, and decide the other four
tasks are too much work to bother with, you've removed the intended monetary
incentive, albeit accidentally.

This assumes the flow of tasks is stagnant, though I've seen only
[evidence][6] supporting that assumption. If you can't find five tasks you
think you can claim before anyone else does, you can either wait until new
tasks come along or start now and hope they do. Worse still, many of the small
task bugs marked as completed were done without knowledge of the Outreach
Program it seems. A total of six small tasks are marked completed:

  * [Option to switch OFF sound completly while keeping video
communications][7]

  * [User choice of video codec compression algorithms][8]

  * [Notification Area needs keynav][9]

  * [Automatically scroll text caret to make it visible][10]

  * [Dasher interface lacks HIG compliancy][11]

  * [Add accessibility support to GtkVolumeButton][12]

The first two bugs were closed by an Ekiga developer as WONTFIX. Folks, it
doesn't get any more **classic Bugzilla** than that. The middle two were fixed
by a developer being paid for their work by Sun. Only the last two were
claimed tasks under the Outreach Program. So of the 30 total Short-Term task
claims, 2 have been fixed thus far via Outreach.

### Long-Term Tasks

Long term tasks are closer to Google Summer of Code in nature: 6 month
projects netting $6000. Thus far, there have been two proposals accepted;
["MouseTrap: Head Tracking via Lowcost Webcam"][13] and [Magnification.][14]

MouseTrap was actually working two months ago. You can see video of it in
action:


>(<a href="http:/youtube.com/profile_videos?user=flaper87">Link if you don't
see the Flash Player above)

And the magnification task is being worked on by the developer of Compiz's
Enhanced Zoom. They're both talented people and I'm sure the money motivates
them to continue the work they started outside of GNOME.

### Will they meet their goals?

With half a year yet to go, it seems unfair to make any doom and gloom
predictions. So instead, let's examine where they stand now in relation to
their goals.

Have they helped improve free software accessibility? **Yes. Not as much as
they hoped**, but there's time left to save it. They've fixed a few bugs,
enticed a few projects towards GNOME that could have large impact.

Have they encourage and inspire people to work on accessibility? They've
certainly encouraged the two Long-Term authors, though maybe not _inspired_
them. Another three people seemed inspired enough to pick up some short term
tasks, but none seem on pace to net five Completed Tasks.

Have they increased awareness of accessibility? I'd say not enough. **This is
an "outreach program", but it almost seems GNOME needs "inreach" to convince
their own project members accessibility matters.** Normally when I think of
outreach I think of an expert organization going to the public to share that
expertise, not an organization in search of experts. Closing bugs as WONTFIX
that Foundation and Sponsors are trying to pay someone to fix does not look
like an organization full of accessibility experts. If GNOME leadership
doesn't convince the rank and file that it needs accessibility, outside
contribution faces a hurdle that could leave them bitter on the subject. This
sort of failure jeopardizes any success found in the previous two questions.

Still, $6,000 is a cheap price for getting some of the Compiz people thinking
about how GNOME might ever integrate their work. And a cheap price to get the
ball rolling on head tracking within GNOME. If we're lucky, in some distant
future we might see eye tracking as well!

   [1]: //www.pwnguin.net/introducing-money-into-open-source.html

   [2]: http://www.gnome.org/projects/outreach/a11y/

   [3]: http://www.gnome.org/projects/outreach/a11y/rules/

   [4]: http://www.gnome.org/projects/outreach/a11y/tasks/

   [5]: http://code.google.com/opensource/ghop/2007-8/

   [6]: http://bugzilla.gnome.org/show_activity.cgi?id=519313

   [7]: http://bugzilla.gnome.org/show_bug.cgi?id=519469

   [8]: http://bugzilla.gnome.org/show_bug.cgi?id=519484

   [9]: http://bugzilla.gnome.org/show_bug.cgi?id=103223

   [10]: http://bugzilla.gnome.org/show_bug.cgi?id=464468

   [11]: http://bugzilla.gnome.org/show_bug.cgi?id=506900

   [12]: http://bugzilla.gnome.org/show_bug.cgi?id=519092

   [13]: http://mousetrap.flaper87.org/trac/

   [14]: http://www.gnome.org/projects/outreach/a11y/tasks/magnification/

