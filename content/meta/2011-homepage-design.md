Title: New Homepage Design
Date: 2011-03-06

New year, new website. The old design worked okay, but [Google's recent
pagerank tweak][3] punished my RSS aggregation trick. So I've accelerated plans
to move the blog to self-hosting, which gives me more stuff to analyze and 
might one day cover the cost of hosting. Tight deadline though, since I want this
ready in time for a conference I'm attending.

### The software ###

The original RSS aggregation method has a number of benefits. It's 
lightweight, and much harder to hack. So I've looked far and wide for
a similar setup for blogging, and the winner was hands down [pelican][1].
Like Planet Venus, Pelican is Python powered, and offers a clean sepearation
of content and visual design to create static sites. 

While Planet Venus used RSS as input, the new site uses static files written 
in markup languages (I use Markdown). Pelican parses all the files and
constructs the various tag pages and feeds. To import all this was a bit 
tricky; Livejournal's export is unique and does only a month at a time.
Luckily, I keep a backup of my entire blog in Liferea, which is sqlite3 backed.
So I wrote a Python script to write each entry out into the Markdown format. 
Stealing code from [html2markdown][4] was very handy, though it choked on a few 
of my more insame markups. Def check out the homepage, because they author's 
got an even more twisted workflow.

Pelican is available via [git][5] or via pip. Deployment is very similar to before,
with a site configuration file and cronjob. I've also decided to place the
site in revision control, to ease authoring, deployment and automation. Perhaps
I'll set up a post commit hook for automated regeneration?

### Output templates ###

Pelican uses The templates are implemented in [Jinja2][2], a very close relative 
of Django's template system. Sandboxing really isn't a feature here, since 
it's used once to generate the HTML. Jinja2 is unfortunately not as 
documented as Django, but that's a very high bar.

I haven't looked into changing the default templates much yet, but I'll do so 
soon to tweak the front page. It also has many parameters for common 
snippets like Google Analytics and Disqus.

Disqus is a very important part of the design. Given a static blog, you might
expect to not have comments, but Disqus provides a javascript interface to 
their system. It's like a sidewiki that sites can opt into. The major advantages
are that I don't have to host comments, Disqus has a centralized profile to 
detect spammers with, and the javascript nature means there's less incentive to 
spam links in comments.

There's also a skribit widget, but I really have no idea what that's about. 
Content suggestions I guess? Perhaps when I'm less busy.

### Web Design ###

The default theme is pretty nice, but it's not a fluid layout.
I've placed it on my todo list to change that and to tweak the colors, but 
for now the default is sufficient. 

I do need to look into a template or something to protect email addresses
from scrapers. There was a nice rot13 trick I used previously that Markdown
alone won't offer.

   [1]: http://docs.notmyidea.org/alexis/pelican/

   [2]: http://jinja.pocoo.org/

   [3]: http://googleblog.blogspot.com/2011/02/finding-more-high-quality-sites-in.html

   [4]: http://www.codefu.org/wiki/Main/Html2markdown

   [5]: https://github.com/ametaireau/pelicanx