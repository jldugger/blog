Title: Java Symposium 2011 Recap
Date: 2011-03-20

Went out to Vegas to attend [The Java Symposium 2011][1]. Not really fond of
the location, but you have to pick your battles. It's a three day conference, 
but travel really knocks out at least a day. 

The most interesting talks, I thought, were less about specific technology
releases like JEE 6 or Java 7 or Glassfish or Apache Camel, but performance 
tuning techniques and war stories. In retrospect the one live demo I saw was 
maybe a bit of smoke and mirrors, where they swapped out an optimistic 
concurrency pattern using Exceptions that looks really ugly for a synchronized 
version and magically halved throughput. They claimed it was antagonistic 
performance from a 3rd party dependency, like Facebook or Twitter. The idea 
being that if you remove roadblocks in your code, you might discover the 
increased load on twitter scales even more poorly. Because apparently queues
are quadratic in Web 2.0 land.

But beyond that there were interesting talks on classloaders, static analysis 
for performance anti-patterns, how the JVM abstraction makes compliance 
difficult to optimize, and the virtues of Dtrace. Many insisted the first 
place to look for dramatic fixes was not code, but configuration and hardware.
We wound up scheduling time with one of the vendor's freemium tools next week 
to debug some terrible performance problems in testing environments not 
present in production or development. I suspect the issue is going to be
insufficent hardware allocation or misconfiguration of the Oracle server; I 
haven't seen any version control for config of that, and it seems like a 
prime candidate for config and data drift. Unfortunately I don't have enough
access to the test env to debug the problem. Perhaps I'll ask for that to be 
remedied.

The keynotes were mostly bland vendorspeak, although Oracle did claim they had
no evil plan, because if they did, the past year would have been less dramatic.
Because obviously they're only good at planning for evil, and fail at 
benevolent planning. Otherwise, lots of emphasis on The Cloud, and Java 7, and
quite a bit of Open Source as a feature. 

   [1]: http://javasymposium.techtarget.com/
