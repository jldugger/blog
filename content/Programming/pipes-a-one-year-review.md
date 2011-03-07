Title: Pipes -- A one year review
Date: 2008-02-08

[Yahoo! Pipes][1] is celebrating their [one year anniversary][2]; plenty has
been written on what Pipes is and what it does, so I'll spare you mere
description with an incredible amount of fanfare by tech media. [O'Reilly
wrote:][3]

> Yahoo!'s new Pipes service is a milestone in the history of the internet

But not everyone agreed at the time. IT Week columnist Tim Anderson asked if
Pipes was all it cracked up to be, mere days after the announcement. The
author attacks not the concept or implementation, [but the open internet
culture it needs to succeed:][4]

> Participating in mashups works well for e-commerce sites like eBay or
Amazon, because it drives sales, but that model fails for other kinds of
services.

Clearly at release, opinions clashed. So after a year in beta, has Pipes
succeeded? The answer has slowly become clear to me. They've certainly
jumpstarted a new class of web application, which I have been using ("beta
testing") for much of the past year. But what I've found is equal parts
frustrating and amazing.

### Milestone of internet programming?

Firstly, in some senses, O'Reilly understates the accomplishment of Yahoo!
Pipes. UNIX pipes are fantastic, but textual representations lead to common
linear topologies. Even the canonical program tee merely dumps output to a
file, rather than duplicating the stream into a second pipe. UNIX pipes
essentially allow you to glue two text apps together, with some fun filters
like grep in between. Search all your source code for instances of blah and
display in a text editor, or create a diff of a programming project and mail
it to a grader. Anything more complex than this and you'll suddenly need to be
writing code in C to arrange the programs and pipes, which quickly loses
advantage and appeal. But there's a broad satisfaction among UNIX users with
pipes; you can quickly write a program to perform a specific task without even
thinking about programming -- it feels more like simply using the system than
actually programming.

Yahoo's graphical representation allows you to easily construct entire
assemblies, split pipelines apart, independently modify them and recombine
them into something far better. This concept is no milestone -- done
correctly, it's a monument. A monument to what, exactly? Things that a few
years ago I dismissed as junk: XML, Webservices, etc. Yahoo pipes correctly
uses XML as a programmer tool, able to analyze it's own data input formats
**while writing your program**. If your feed has extra attributes, these
become targets for rules later on in the pipe. This has been the most
impressive use of XML I've seen to date. Pipes effectively lowers the Web
Services bar from people familiar with Greasemonkey or XML Transformations
down closer to sysadmin skills.

### No panacea

So Pipes is great in that it maintains the simplicity of the UNIX pipes model,
while extending it in ways the old model could never have adapted to.
Unfortunately, a year later, a lot of bugs that would have been forgivable at
release continue to exist. For example, regular expressions were added as a
way to mangle strings. For advanced uses, this is priceless. Sadly, they're
not implemented correctly. I repeatedly run into a wall regarding their regexp
Module. It's painful enough learning Perl-like regular expression syntax, but
Yahoo!'s bugs make it downright impossible for experts to do things let alone
novices. HTML isn't meant to be parsed in this manner, and many sites may
resort to fighting Pipes (which has an opt out system for content owners) and
knock-offs (which may not) by twiddling the code in ways that affect regular
expressions but not more advanced grammars used in actual rendering.

This means Pipes' best tool in the toolbox to counter IT Week's closed
internet claims is bent, if not broken. And he's right on the merits. Almost
nobody has a business incentive to publish RSS or other web services in an
advertising driven system. Google dropped their search API in favor of
Javascript widgets and Gears. Google Video might allow people to publish video
for download, but Youtube doesn't. Pipes introduced a Fetch Page module, in an
attempt to let users break up any given page into sub elements. Webscraping
with Pipes is difficult to do at best, and the broken regexp module makes it
almost meaningless in making feeds from sites without one already. For
example, I've been working at an RSS feed for the Greatest Site in the
Universe, but the author's handwritten HTML requires delicate touches that
Pipes' regexp system cannot handle.

But this is not the only problem that comes up. I've constructed a fairly
simple pipe that searches several RSS feeds for items, and formats them in a
way that I can automate [broadcatching][5] with. One pipe, run with several
different parameters. For reasons unknown to me, these pipes work fine in
debugging mode, but in particular I get the same feed from two distinctly
different parameters. I can only imagine that something is terribly broken in
their caching scheme.

A third annoyance is that you can only use other modules as inputs. The beauty
of UNIX pipes was that so many programs were "fittable" from either end.
Yahoo! pipes cannot accept an anonymous standard input. Without this, every
workaround you create must be duplicated in every pipe you need it for, and
it's sometimes a typo bound endeavor.

Finally, the Pipes team is not at all on top of their beta tester user base.
This is somewhat understandable when the comments are like "Pipes should have
an easy HTML to RSS module!", but when you provide a test Pipe that clearly
demonstrates simple bugs like regular expression case sensitivity, it sends a
confusing signal to me. Are they not interested in fixing Pipes? Is there
somehow a bigger problem I'm not seeing? Are the kinds of things I have in
mind for Pipes simply not on the slated future of Pipes? A fellow Pipes user
[responds to my question:][6]

> I'm still not clear on how to alert the pipes development team about these
issues.

If I was a Microsoft looking to evaluate the value Pipes adds to Yahoo!, these
sorts of failings are not a good sign.

### So now what?

I'm forced to conclude that **Pipes is mostly a pipedream**. In order to fix
the many problems I'm encountering, I'll likely resort to abandoning Pipes in
favor of running scripts locally. Plagger requires perl and is apparently a
PITA to package. OCamlRSS has gone over a year since it's last update. This
situation is slightly disappointing because with Pipes, the explanatory
diagrams were the code. But for now I have more faith in my ability to
translate hand drawn diagrams into code and perl regular expressions than
Yahoo!s ability to deliver a working regExp system.

   [1]: http://pipes.yahoo.com/

   [2]: http://blog.pipes.yahoo.com/2008/02/07/our-one-year-anniversary/

   [3]: http://radar.oreilly.com/archives/2007/02/pipes_and_filte.html/

   [4]: http://www.itweek.co.uk/itweek/comment/2185589/yahoo-pipes-cracked

   [5]: http://en.wikipedia.org/wiki/Broadcatching

   [6]: http://discuss.pipes.yahoo.com/Message_Boards_for_Pipes/threadview?m=tm&bn=pip-DeveloperHelp&tid=2912&mid=2914&tof=-1&rt=2&frt=2&off=1

