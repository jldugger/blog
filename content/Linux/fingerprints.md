Date: 2007-11-15 
Title: Linux Fingerprint Developments

It's been a busy week for Fingerprint Authentication in Linux. [Timo announced
][1] that pam_thinkfinger is being retired, and a new project will supposedly
arise from it. So it's effectively being abandoned. Normally I'd say it's a
bad thing, but it's a solid driver at the moment, and most of the problems
arise from the PAM module. Requiring uinput has been a source of pain as it's
partly considered insecure. The good news is that Thinkfinger is a whirlwind
of activity at the moment preparing for a final release, reviewing and
integrating patches that have been floating around. Hopefully upstream won't
die as much as branch. 

Additionally, theres a new Ubuntero pushing on [including BioAPI in Ubuntu][2]. 
He seems a bit of a novice though, so don't hold your breath. I don't quite 
see the purpose in pushing BioAPI exactly, but if it works, great for everyone. 

Finally, [fprint][3] announced an initial release this week. They aim to create 
a generic library with which they can support all kinds of fingerprint hardware. 
Unsurprisingly, security is ["of interest, [but] not a primary objective".][4] 
That's right. A security tool who's primary objective is not security. Mostly 
this is an artifact of the contradiction of using fingerprints as security 
devices -- they're not as secure as a good password, but they are slightly 
better than auto login as root.

   [1]: http://sourceforge.net/mailarchive/forum.php?thread_name=1195126619.17548.65.camel%40zimtstern.suse.de&forum_name=thinkfinger-devel

   [2]: https://bugs.launchpad.net/bugs/54816

   [3]: http://www.reactivated.net/fprint/wiki/Main_Page

   [4]: http://www.reactivated.net/fprint/wiki/Security_notes