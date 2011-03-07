Title: Eclipse disaster
Date: 2008-05-23

As a student and developer fairly experienced with Linux, I'm often asked what
IDE or debugger to install. I'd love to answer Eclipse, as on paper it's very
nearly competitive with Visual Studio. If you're using Java, by all means,
it's perfect. **If you're using C/C++, don't bother with Eclipse.**

### Why?

The JDT has an interactive tutorial on using eclipse to start a project. CDT
does not. If you don't know how to use Eclipse, this is unfortunate. Not a
deal breaker, as there is documentation and perhaps videos somewhere. But
don't think that the awesomeness of the JDT translates to an awesome CDT.
Moreover, your ability to interact with the object model begins and ends at
starting projects and adding / removing objects. The rest of the Views can
parse and integrate your changes to classes, but you can't use them to stub
the code.

But the big one is [Content Assist.][1] Content Assist is a simple feature
intended to duplicate Visual Studio's [IntelliSense][2]. Sounds great,
terrible implementation. Even the CDT project lead [Doug Schaefer][3] is
[frustrated][4]:

> It's bugs like this that make me wonder why CDT committers are working on
new parsers, when there are still a number of issues like this that need to be
addressed in the existing code base that none of the committers have signed up
to address.

A fellow CDT committer [rebukes him][5]:

> We have requirements for multi-language support from the people that are
paying us to work on CDT, so that's where we're focusing ...Content assist is
important for us, but working on it has to be balanced with our other
priorities.

Its clear that the CDT as an open source project is in a strange position of
having people paid to not make it better. Or rather, balancing priorities
mainly means completely ignoring content assist. At current count, there are
[144 open bugs about CDT Content Assist][6]. Now, some of those bugs in such a
basic search may not actually be correct, and at least one of those bugs is a
feature request. But many of the bugs I've looked at appear valid, yet
stagnate on bugzilla. Plus that feature request is for a cancel-able content
assist, because it takes too damn long, so you can basically call it a
"content assist sucks" bug report. The lack of any significant triage confirms
that the "balanced" approach is complete denial and/or ignorance.

So why would you use Eclipse? If you look at their sponsors, it's pretty easy.
Use Eclipse whenever putting up with the embedded systems toolchain your
vendor offers. [QNX, WindRiver, MontaVista and a ton of others][7] now base
their tools on Eclipse, and you can be damn sure they don't target Java on
their microcontrollers. It's a smart move if you're familiar with embedded
systems development from pre-2001. As terrible as I make Eclipse out to be,
it's quite a move forward in that area, where nobody sought to distinguish
themselves on the IDE front (embedded system designers are masochists almost
by definition, after all). I suspect developers who use eclipse CDT turn off
content assist and get on with their lives in an otherwise fantastic life. I'm
tempted to file a bug that Content Assist should be off by default.

So if I can't recommend Eclipse, what should I?

   [1]: http://publib.boulder.ibm.com/infocenter/rtnlhelp/v6r0m0/index.jsp?topic=/org.eclipse.cdt.doc.user/concepts/cdt_c_content_assist.htm

   [2]: http://en.wikipedia.org/wiki/IntelliSense

   [3]: http://cdtdoug.blogspot.com/

   [4]: https://bugs.eclipse.org/bugs/show_bug.cgi?id=205964#c1

   [5]: https://bugs.eclipse.org/bugs/show_bug.cgi?id=205964#c2

   [6]: https://bugs.eclipse.org/bugs/buglist.cgi?query_format=specific&order=relevance+desc&bug_status=__open__&product=CDT&content=content+assist

   [7]: http://dash.eclipse.org/dash/commits/web-app/summary.cgi?company=y&year=x&top=tools&project=tools.cdt

