Title: (Old) Homepage Design
Date: 2010-03-12

I've decided my old homepage was bad enough to revisit now that I've got a bit
more content hosted deep within it. I replaced my crappy hand written HTML
with tools written this decade, and threw in some amateur visual design.

### The software

Firstly, in order to keep the webpage fresh with little effort, I've chosen
RSS aggregation as the method of content generation. Since I know Ubuntu and
Debian both use [Planet][1], that's where I first looked. But it seems Planet
2.0 is aging, and the fork [Planet Venus][2] brings some neat new options. It
expands the selection of templates, adds a configurable RSS filter step, and
makes the normalization step configurable.

It's also packaged in Ubuntu as planet-venus, making it fairly simple to set
up. Deployment was a little tricky, as the package leaves most of the site
[configuration][3] to the admin. You'll need a config.ini (I used
/etc/planet/planet.ini), a template dir (/usr/local/share/planet-venus/theme),
a cache dir (/var/cache/planet) and an output dir (somewhere in /var/www
typically). Finally, you'll need to set up a cron job to run the static output
generation script regularly. The script reads all the feeds and parameters in
config.ini, caches the results to save bandwidth on subsequent runs, passes
them to the template engine, and places the final product in the output dir.

When building a lifestream style site, you have to be picky about the kinds of
feeds you put in or it gets Facebook / Twitter style spammy. This is where the
RSS filter step can help; Planet Venus comes with a few filters like
'notweets', and a few stripAds filters to cleanse ads before republishing.
It's the same design pattern I talked about before [here][4] with Liferea. In
the future I could write one to add in comment feeds and then filter out
everything that fails to meet some strong quality criteria.

### Output templates

Planet Venus's real selling point to me is using [Django templates][5]. I've
been meaning to learn Django for a while now, and this is a pretty good way to
work with the templates portion of Django. And again, the filter pattern pops
up. Here, filters take python variables as input; in Planet Venus's setup you
have access to feed and item variables, as well as planetwide settings. One
example filter might be to simply [pluralize][6] a word based on a variable
(yes, you can even handle 'y' pluralization). Another example is the
[urlize][7] filter that adds HTML anchor tags to likely URLs (not so great
when you already have anchor tags in the filter's input).

I also use templates to generate an RSS feed. Nothing difficult about it,
since the input to templates is basically an RSS feed to begin with. To reduce
the probability of bugs, I translated a provided example [htmptmpl][8] RSS
template into Django, and it's much smaller and clearer to me. Unfortunately,
there's a bug in Planet Venus that prevents the use of multiple Django
templates. I've reported it upstream, and I'm sure I can fix it or work around
it.

### Web Design

I also decided to take a look at CSS layout frameworks, to get up to speed on
the subject quickly. 960.gs is popular, but it's 960 pixel width assumption
works poorly with quirky resolutions found on massive monitors and
smartphones. Luckily, I found found [fluid960][9], which is very similar, but
implements fluid layouts. It retains the CSS class names of 960.gs, so
tutorials and documentation on one translate fairly well to the other. Which
is good, because fluid960 pretty much relies on you already knowing regular
960 (I didn't). [This presentation][10] gives a good summary of things you
might want a CSS framework for, and this [ 960 tutorial][11] covers what I
needed to know.

Color scheming is probably the hardest part for me. It's simple to pick a
color pallate that goes together, but there is a higher level opportunity to
communicate something through visual design. I could choose a purple scheme to
reflect my collegiate experience, or an Ubuntu pallete, but it seems
inappropriate for a personal site. I've got a bit of low level coding
experience, so I could go with a green on black terminal theme, but it's been
done to death ever since the Matrix, and it's basically impossible to beat
[jwz's][12] version.

Since I'm not really looking to break into web design, I went with a
relatively muted color scheme that organizes the content without distracting
from it. Truthfully it doesn't matter all that much, as experience shows the
majority of hits will come via RSS.

Well, that's basically all there is to my automated homepage system. On to
more important things, like setting up a calDAV server or a feed processing
tool.

   [1]: http://www.planetplanet.org/

   [2]: http://intertwingly.net/code/venus/

   [3]: http://intertwingly.net/code/venus/docs/config.html

   [4]: //pwnguin.net/fun-and-profit-with-liferea-conversion-filters.html

   [5]: http://www.djangoproject.com/documentation/templates/

   [6]: http://docs.djangoproject.com/en/dev/ref/templates/builtins/#pluralize

   [7]: http://docs.djangoproject.com/en/dev/ref/templates/builtins/#urlize

   [8]: http://htmltmpl.sourceforge.net/

   [9]: http://www.designinfluences.com/fluid960gs/

   [10]: http://vimeo.com/7530607

   [11]: http://net.tutsplus.com/videos/screencasts/a-detailed-look-at-the-960-css-framework/

   [12]: http://www.jwz.org/

