Title: yay Garmin
Date: 2008-07-10 

I just saw a link on IRC that I should [share.][1] Garmin has decided to
publish [source code][2] to their Linux based devices.

You can see Garmin's new offices from my house, they're quite tall. It's good
to know that friends of mine working for Garmin are slowly changing how things
work. A surprising number of K-SLUG members have been hired over the past few
years and I hope they're just getting started. For example, they should
probably be working with legal to figure out how to [forward patches
upstream][3].

It's never easy to transition a company from closed processes to encouraging
or even allowing outside contributions. Nobody wants to open the firewall and
expose corporate intranet assets to the evil Internet, the development process
is confusing when some projects are open and others aren't, etc. There's also
liability floating in the ether, mostly in the form of "I damaged my product!"
but maybe also in the "your X server patch (the one you reverted but is still
published via VCS) broke my monitor."

So it's no wonder many embedded vendors stop at publishing tarballs and avoid
public review at all costs. I won't let them off that easy however. They were
kind enough to publish in the Debian style .orig/.diff pairing, so I've been
browsing some of the changes. Here's an inexplicable example:

`diff -Nur xrandr-1.2.0.orig/xrandr.c xrandr-1.2.0/xrandr.c`:

    --- xrandr-1.2.0.origxrandr.c 2008-06-23 11:48:28.000000000 -0500
    +++ xrandr-1.2.0xrandr.c 2008-06-23 11:48:56.000000000 -0500
    @@ -163,7 +163,7 @@ <br>
      #if HAS_RANDR_1_2 <br> typedef enum _policy {
    - clone, extend <br>+ policy_clone, extend
      } policy_t; <br>
      typedef enum _relation { <br>@@ -1398,7 +1398,7 @@
      #if HAS_RANDR_1_2 <br> output_t *output = NULL;
      char *crtc; <br>- policy_t policy = clone;
    + policy_t policy = policy_clone; <br> Bool setit_1_2 = False;
      Bool query_1_2 = False; <br> Bool query_1 = False;
    @@ -1634,7 +1634,7 @@ <br> continue;
     } <br> if (!strcmp ("--clone", argv[i])) {
    - policy = clone; <br>+ policy = policy_clone;
     setit_1_2 = True; <br> continue;
     }

Of course, these devices are a bit outside my pricerange, but the appearance
of source does appear promising for the upcoming nuvifone. It'll be
interesting to see how it compares to the openMoko design.

   [1]: http://www.computerworld.com.au/index.php/id;1756347190;fp;16;fpid;1

   [2]: http://developer.garmin.com/linux/

   [3]: http://developer.garmin.com/forum/viewtopic.php?t=453

