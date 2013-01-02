Title: PuppetConf 2012
Date: 2012-09-30

Recovered from the post-con crash a while ago, so it's time to write up some thoughts.
Last week I attended PuppetConf with my coworkers at the OSL. The OSL attended
PuppetConf primarily as a pre-deployment information gathering exercise. We want
to avoid common pitfalls, and be able to plan for things coming down the pipeline.
Puppet 3.0 was targetted to be released on Friday and [clearly that slipped][5].

The venue itself was nice, but space partitioned poorly. The two main tracks had
surplus space, but the three side tracks nearly always had people turned away for
space concerns. Supposedly, the recordings will be available shortly, so it may
not be the Worst Thing In The World, but only time will tell.

Content wise, one recurring theme is to start small and simple, and not worry about
scale or sharing until they become an issue. Designing a deployment for thousands of
nodes when you have perhaps a dozen gives new life to the term "architecture astronaut,"
and there's a certain amount of benefit to procrastinating on system design while
the tools and ecosystem mature. Basically, [build one to throw away][6].

Another problem we've been worrying about at the OSL is updating 3rd party config
modules in their various forms. The hope is that by explicitly annotating in your
system where things came from, you can automate pulling in updates from original 
sources. Pretty much the universal recommendation here is a condemnation: avoid git 
submodules. Submodules *sounds* like the right strategy, but it's for a different use
case. In our experience, it dramatically complicates the workflow. At least one person 
mentioned [librarian-puppet][1], which as far as I can tell is isn't much different 
than [mr][2] with some syntactic sugar for PuppetForge. This is great, because mr was 
basically the strategy I was recommending prior to PuppetConf.

The [Better Living Through Statistics][3] talk was less advanced than I'd hoped. Anyone
who's spent maybe 5 minutes tuning nagios check_disks realizes how inadequate it is, and
that the basic nagios framework is to blame. What you really want is an alert when the
`time to disk outage` approaches `time to free up more disk`, and no static threshold
can capture that. While Jamie did provide a vision for the future, I was really hoping
for some new statistical insight on the problem. It appears it's up to me to create and
provide said insight. Perhaps in another post.

[R Tyler Croy][7] gave a useful talk on [behavior/test driven infrastructure][4]. I'd
looked into Cucumber before, but RSpec was only a word to me before this talk. It's
certainly something I'll need to take some time to integrate into the workflow and
introduce to students. One concern I had (that someone else aired) was that in the demo,
the puppet code and the code to test it was basically identical, such that software
could easily translate from code to test and back. Croy insisted this was not the case
in more complicated Puppet modules, but I'm reserving judgement until I see said modules.

Overall, I'd definately recommend the conference to people preparing to deploy puppet.
There's plenty more sessions I didn't cover in here that are worth your time. You'd
probably get the most out of it by starting a trial implementation first, instead of
procrastinating until Wednesday night to read the basics like I did. Beyond simply
watching lectures, it's useful to get away from the office and sit down to learn about
this stuff. Plus, it's useful to build your professional network of people you can
direct questions to later.

   [1]: http://librarian-puppet.com/
   [2]: http://joeyh.name/code/mr/
   [3]: http://puppetconf.com/speakers/?speaker=Jamie%20Wilkinson
   [4]: http://puppetconf.com/speakers/?speaker=R.%20Tyler%20Croy
   [5]: http://projects.puppetlabs.com/versions/271
   [6]: http://en.wikipedia.org/wiki/The_Mythical_Man-Month
   [7]: http://unethicalblogger.com/
