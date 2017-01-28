Title: Fun and Profit with Liferea Conversion Filters
Date: 2009-09-13

[Liferea][1] is an RSS feed reader, with some hidden powers. I use it to
automatically download enclosures from the [TED][2] feed, and aggregate unread
comic strips into a single scroll page in a custom view folder. But today, I'd
like to present **conversion filters**.

Conversion filters are scripts that function according to UNIX pipes semantics
to process feeds before display. Liferea performs the task of retrieving the
XML, starts the conversion filter, and passes the XML over stdin. The filter
prints a converted XML file back to Liferea over stdout, and which happily
displays the new RSS feed. For the graphic minded:

![liferea conversion filter diagram][3]

A [small repository of conversion filters][4] has been started, mainly driven
by a different, command line driven RSS reader, snownews. Most published
conversion filters are what you'd call a _source_ in dataflow, rather than a
_filter_. Even more are site specific, making this more of a greasemonkey for
RSS feeds.

I'll share an example I concocted today. I like the [Freakonomics blog][5],
but lately they've added some unrelated content called _Quotes Uncovered_. I
have no idea how identifying the historical source of quotations relates to
microeconomics, but I do have an idea of how to use a conversion filter to
remove it. But first, we need to talk for a moment about **XPath**.

XML is tree structured, like a filesystem. I've seen at least two people take
this analogy to it's conclusion, and implement an [XMLfs][6] via FUSE. XPath
also uses this analogy, for a different purpose, describing paths in
documents. Paths in UNIX filesystems can be singular, like
**/etc/apt/sources.list**, or plural, like **/etc/apt/sources.list.d/***
(technically your shell expands this, but play along). Concepts like **../**
and ***** are supported by XPath. Instead of directories though, we're going
to use XPath to navigate nodes in XML.

Unfortunately, I'm interested in a specific node, based not on it's name but
it's contents. So I need some predicate to narrow this. In UNIX shell, find is
commonly used for this purpose, but XPath integrates this concept and diverges
from UNIX paths. In the case of my Freakonomics cleaner, I want to delete the
item node that has _Quotes Uncovered_ in a child title node:

`//*/item/title[contains(text(),'Quotes Uncovered')]/..`

Liferea doesn't understand XPath though, so we'll need to use the conversion
filter to handle. Conversion filters I've seen thus far end up scripting
parsing the XML, processing the structure and printing it. Only the middle
part is actually going to be unique to conversion filters. Fortunately,
there's a program that adheres to UNIX philosophy and handles this:
[XMLStarlet][7] (in Universe). XMLstarlet reads XML from stdin, and writes XML
from stdout, just as our conversion filters must. On a technical level, it
converts the command line to an XSLT and applies it to the input. In this case
I just need to tell it to delete the section matching that XPath from the
feed. That's accomplished with the ed -d option.

So now I just create a new subscription, and put the command in the box:

![liferea subscription properties dialog][8]

The result is a one-liner that puts the Quotes Uncovered series to pasture.
It's tempting to UNIX pipes to build more complicated filters, but I'm told
Liferea isn't currently coded for chained pipes. So if you get more
complicated than the basic 3 step Fetch-Filter-Display pipeline, you'll need
to write a short shell script for that, or write some really crazy XPath.

### Postscript

The Snownews extension repo is interesting, but doesn't have a way to link
feeds with scripts. Earlier I compared conversion filters to Greasemonkey.
Well Greasemonkey has a partner extension called Greasefire and a website
backend userscripts.org for script discovery. It'd be handy to have conversion
filter discovery for RSS!

   [1]: http://liferea.sourceforge.net/

   [2]: http://www.ted.com/

   [3]: //www.pwnguin.net/media/photologue/photos/conversionfilter.png

   [4]: http://kiza.kcore.de/software/snownews/snowscripts/extensions/

   [5]: http://freakonomics.blogs.nytimes.com/

   [6]: http://github.com/halhen/xmlfs/tree/master

   [7]: http://xmlstar.sourceforge.net/

   [8]: //www.pwnguin.net/media/photologue/photos/Liferea-Subscription.png

