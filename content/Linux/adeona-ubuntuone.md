Title: Adeona + UbuntuOne?
Date: 2009-08-23

[Adeona][1] is an OSS anti-theft program. The theory of operation is described
as a _privacy-preserving device-tracking system_ in the [research
publication][2]:

> A device tracking system consists of: client hardware or software logic
installed on the device; (sometimes) cryptographic key material stored on the
device; (sometimes) cryptographic key material maintained separately by the
device owner; and a remote storage facility. The client sends location updates
over the Internet to the remote storage. Once a device goes missing, the owner
or authorized agent searches the remote storage for location updates
pertaining to the device’s current whereabouts.

The paper goes on to describe specific goals for Adeona:

  * network update anonymity

  * privacy from the thief

  * efficiency on par with existing tools

I'll argue that most of this is post-hoc requirements from an early decision
to rely on OpenDHT (which turns out to be a not so great idea). That said,
it's not bad stuff to have; Joey Hess's [recent discovery][3] made headlines,
and rightly so, when Palm Pre violated pretty much every principle the Adeona
wrote about.

However, it's rarely a wise idea for products to rely on academic research
projects. As a research project, it might have been acceptable for Adeona to
depend on OpenDHT. But this decision should have been revisited when Adeona
launched as a community product. And they've paid a price -- OpenDHT announced
it would be closing down on July 1st 2009. I'm not clear on whether the
OpenDHT infrastructure is too slow and unreliable, or if the software itself
is unreliable, but Adeona's own website currently starts with a disclaimer of
non-functionality.

So what I'm wondering out loud is, why not integrate Adeona and UbuntuOne? The
purpose of using OpenDHT appears to be to find cheap storage for tracking
data. Obviously some privacy would be sacrificed. Canonical would basically be
able to track some things, like IPs connected to UbuntuOne. While there are
already other reliable places for Canonical to snoop IP addresses (access logs
from Ubuntu archives), UbuntuOne takes the extra step of authenticating users.
I believe though, that the only thing they'd be able to associate is your
username with a set of IPs. I guess it comes down to how many ultra-paranoid
users object to the privacy concerns of UbuntuOne itself.

Ideally, I think Adeona would be generalized to allow a number of remote
storage interfaces. If I understood the system correctly, data is encrypted
before being stored. The privacy paranoid would be able to store location data
on their own servers, or encrypted email, etc.

So is there something I'm missing? A competing product maybe? Or perhaps the
viewpoint of law enforcement; the academic papers seem to neglect recovery
rates and concerns from police. Or perhaps something technical. I'm hardly a
crypto expert, and currently security researchers seem to be focusing on a
[proprietary application.][4]

   [1]: http://adeona.cs.washington.edu/

   [2]: http://adeona.cs.washington.edu/papers/adeona-usenixsecurity08.pdf

   [3]: kitenet.net/~joey/blog/entry/Palm_Pre_privacy

   [4]: http://www.google.com/hostednews/ap/article/ALeqM5gDEcxr3CSkM0RlVSqVzNWlccf6XwD99P33N82

