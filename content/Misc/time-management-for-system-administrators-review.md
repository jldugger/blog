Title: Time Management for System Administrators review
Date: 2010-04-30

After [Coders At Work][1], I needed to decide what next to read in my
professional sphere. I've been slowly collecting rainy day ideas and ToDos in
a text file, and moved them into Evolution when that got long enough that I
needed summary views to hide notes for each item. Even then, it became
overwhelming again. A personal website to improve, video games to play, books
to read, software to install, things to blog about, programs to write,
investments to research. Meanwhile work load at the college is only growing,
so reading a book on time management seems apropos.

There's lots of books on time management, but the system administrator role
brings together a unique combination of managerial meetings, discretionary
time and on-demand customer service. We're also members of a rare group of
people for whom on-call pagers are a nearly universal term of employment. And
for reasons I'll never understand, IT professionals are rarely managed by more
experienced IT professionals, resulting in scenarios like [this][2]. When I
look around the office, there's few people I can look to for advice on the
subject of time management. Some people stick in the office till 7PM, and
others let unproductive committee meetings dominate their work day. But I
recall a mantra: "to change the world, first change with yourself." So I
decided to pick up [Time Management for System Administrators][3] and
give it a shot.

### About the Author

The author, Tom Limoncelli, is an accomplished system administrator, having
worked for Lucent, Lumeta and now Google. He's published through the [LISA
conference][5] numerous times and serves on this year's program committee.
He's also a co-blogger on [Everything Sysadmin][6], created in part to promote
books they've coauthored, such as "Practice of Network and System
Administration," a fairly comprehensive book on the subject. Clearly, the guy
is qualified as both a sysadmin and a busy one at that.

### Time Management for System Administrators

Limoncelli knows your time is valuable, so TMfSA is a thin book, a svelte 194
pages. But do not be fooled. This is not a book you can read once and put on a
shelf to collect dust. You can get something out of it, of course, but it's no
different than a diet book, **you have to be prepared to take action to truly
have gained** from this book. Multiple times he admonishes the reader to start
practicing his approach right now, because _getting started_ is the hardest,
most valuable advice. The only way to encourage readers to start now any
harder would be to include stationary to practice with, which Franklin Covey
already does quite annoyingly well at.

The basic central system is what Limoncelli calls "The Cycle System." In a
nutshell, his advice is to record everything, and organize by day. Record
every task to be done, prioritize and estimate the time it takes. If your day
is overbooked, he offers coping mechanisms to make up the difference:
Delegate, shorten the task, break the task up into smaller subtasks, delay
meetings. Let people know when high priority tasks aren't getting done on time
and come up with contingency plans.

Like any modern time productivity book, TMfSA addresses the email time sink.
It advocates an inbox zero approach, heavy on automating the filing, filtering
and processing. It's not as dogmatic as _Getting Things Done_ or _Inbox Zero_
but does name drop the former in the Epilogue. TMfSA's main advice appears to
be to touch all mail once and skip archiving.

The "Cycle System" is generic enough that I wouldn't recommend this book if
that's all it contained. But the details count for a lot. He points out that
programmers and sysadmins work best in a state of '[flow][7]', and that a good
workplace is organized to maximize flow and minimize interruptions. He
suggests that teams can organize a support rotation for a few hours a day so
the rest of the team can utilize large blocks of uninterrupted thought. New
email checks can be done every 3 hours rather than every 3 minutes, and you
can have a scheduled 'on call' person to shield the rest of the team from
interruptions. Since it's easier to concentrate when it's quiet, don't
squander that opportunity on replying to email.

Finally, it gets into the stuff that's dramatically different for IT than
other kinds of employees. There's some advice on running effective meetings,
the eternal bane of techies. There's some advice on specialization. An example
gets the point across: a lawn service can justify expensive mowing equipment
that improves productivity because they'll use it a lot more over a season.
**If 1 hour of your time is worth more than 20 minutes of theirs, hiring a
service becomes a no-brainer**. TMfSA covers a few such no-brainers in the
sysadmin workplace. It also covers when to document, when to automate and when
to outsource, and presents a clever use of make to automate system deployment.

### Takeaways

The book was interesting and certainly gave me ideas on how to approach time
management, however there's a lot of places I choose to deviate. The author
spends a lot of time addressing a paper oriented system, but smartphones have
gotten to the point where most sysadmins have a phone that performs as well as
or better than the old Palm PDAs. The author makes a point about a
_centralized calendar_ but all that's really called for is a _unified
calendar_. For example, a unified view of your work calendar on Exchange and a
personal calendar on CalDAV or Google. My phone supports local calendars
and oddly, Exchange but not CalDAV. I really hope the next firmware release of
Maemo adds CalDAV because it would solve this problem neatly. Failing that, I
really think it's something for Meego to look at.

I also dislike the idea of deleting email. There's a lot of valuable historic
information that saves my bacon on occasion, and anticipating this on the spot
is a hard task. Keeping your inbox empty adds a "keep or delete" decision that
I just skip. Limoncelli advocates the opposite approach primarily for a
technical reason, that clients and servers cope poorly with them; my
experience with Gmail suggests the problem is solvable rather than inherent. I
did agree with his point about the price of email interruptions and I've tuned
mail popups to specific high importance mail only, and set up better
filters—now patchmail goes into a folder I review once a week while preparing
change tickets.

As I said before, reading this book is less fruitful if you don't practice the
advice within. I find The Cycle System performs fine at work. It does less
well at home where there's rarely ultra high priority tasks and little
motivating distinction between "soon" and "eventually". I think a [slack time
based prioritization][9] would help with tasks that have deadlines, as would a
CalDAV app for my phone. For personal projects and hobbys, I've decided to
take a page from my university days and built a weekly schedule to fit
everything into. I've even blocked of some time every week to contribute more
to Ubuntu, now that my webserver is at a point where it's running the latest
stable and has a test disk image. No more patching Ubuntu packages locally!

The technical content has become less relevance over time. It may have been
best to not discuss PDAs and smartphones, as many things have changed since
2006. Palm is no more, and PalmOS is all but vanished. Wikis are popular
enough that pages are probably better spent on effective wiki permissions than
syntax--too many enterprise wiki systems deny by default and interfere with
the purpose of wikis. The make trick is clever, but cfengine would have been
more appropriate, if it cfengine was less confusing for readers. Since
publication, [Configuration Management Tools][10] have flourished into popular
and less confusing systems. I suppose make does feature a high
reward:investment ratio you can use as a reference point on your way to puppet
or chef or cfengine etc.

Overall, the book is a useful way to begin building your own time management
approach. Although the book's sysadmin voice feels forced at times with the
inclusion of UserFriendly clips, if you're a UNIX system administrator this
book is a way great jump start your own routine. Time Management for System
Administrators review

   [1]: //www.pwnguin.net/coders-at-work-book-review.html

   [2]: http://ask.metafilter.com/151380/Youre-harshing-my-flow-manager

   [3]: http://amzn.to/2eiqo3H

   [5]: http://en.wikipedia.org/wiki/Large_Installation_System_Administration_Conference

   [6]: http://everythingsysadmin.com

   [7]: http://en.wikipedia.org/wiki/Flow_%28psychology%29

   [9]: http://en.wikipedia.org/wiki/Least_slack_time_scheduling

   [10]: http://en.wikipedia.org/wiki/Comparison_of_open_source_configuration_management_software

