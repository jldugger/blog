Title: An electronic diversion
Date: 2009-07-26

I've always felt a bit mystified with analog electronics. Sure, I had a few
chances to figure it out, but these sorts of things require an experienced
guide. When I was a child, I received a Christmas gift of an AM radio kit. It
didn't work; my father suggested the crystal diode was broke but we never got
it working. He once brought back from a garage sale a kit that's now [a
collectors item][1], but it was missing a manual and a few parts. I suppose I
can't really fault a guy with an Accounting degree for inadequately explaining
what a transistor was without using the term "conductance band", but at the
time, the idea of electricity stopping the flow of electricity confused the
hell out of me.

So even as I was taking embedded programming courses in college, I was
uncomfortable with some of the stuff I would be working with. Sure, all CS
grads are required to take a digital logic class, but it didn't cover the
basics, like the purpose of ground (science education mostly talks about
positive and negative and circuits), or elementary parts like diodes,
transistors and resistors. Now that I'm at a point in life that I have a bit
of money to spend, I've been looking at intro electronic hobby kits, and
watching [MIT 6.002 lectures][2].

### The parts

Of the many kits available at local stores and online, one that that caught my
eye was a kit on Maker's Shed, a [from Sparkle Labs][3]. Most kits are focused
on a single project like an AM radio. This kit, however, is described as a
"curated selection of parts". It comes with a breadboard and lot of just
normal parts, which is great.

[![][4]][5]

The picture does a better job explaining what's in it than I can. All of the
basics are present: resistors, capacitors, diodes, buttons, LEDs, wires. It
also comes with potentiometers, transistors and photoresistors. Finally, it
comes with a 556 chip (a pair of 555 timers), which turns out to be a real
treat. The 556 isn't the sort of thing I would have found in a textbook or in
online lectures, but appears to be extremely versatile. And apparently the 555
very high selling IC.

### The manual

Interestingly, Sparkle Labs is mainly a Design-with-a-capital-D outfit,
judging by their published[portfolio][6]. This emphasis on visual design shows
in their manual, which features lots of stylized 3d renders of circuits
alongside traditional circuit diagrams. I'd be very interested to learn how
the renders were made, as they're very nice and nearly solve the challenge of
translating circuit diagrams to a breadboard.

The manual explains most of the parts included, and offers example circuits to
demonstrate their use. For example, when discussing resistors, it mentions
industrial color band labeling. The first circuit you build is a handy power
supply from a 9V battery down to 5V. Other circuits include a dark detector
and light detector. It comes with some transistors, but not enough to build
logic gates or simple adders.

The manual ends with a circuit to build a signal generator out of a [556
timer][7]. It's a variant on the [Atari Punk Console][8] that uses photodiodes
for no reason I can discern. I replaced them with potentiometers (as hinted
at), and it works fairly well. I know I've seen other circuits out there and
I'm tempted to try them out.

The manual does have some shortcomings though. A few parts included get no
mention in the manual, which is a bit puzzling. A couple of diodes are
included, presumably for radio, since turning AC current into DC current is a
recipe for death in household scenarios. And the section on the 556 comes with
a few impressive and fun circuits, but really doesn't explain the function and
pinouts in sufficient detail.

From a graphic design perspective, a few of the colors are a bit off. The
manual comes with a resistor decoding chart, but doesn't quite match up with
the resistors provided. The unprepared may be expecting a far greater contrast
between red and brown, and confuse the two. After the manual introduces
resistor color coding, 3d renders are done with a generic resistor color
banding, which is just mean to lazy people like me.

### My final words

Overall, this kit is not a bad deal for a hobbyist. The parts are a cheaper
deal for the money than at places like Octoparts and Digikey, and the manual
can easily be supplemented by the internet and libraries. If Sparkle Lab's
main goal is to corner an "educational" market, the manual might need some
revision, or a supplemental website. But my main purpose was to be more
comfortable with analog components, in preparation of building a [USB powered
Sensor Bar][9] for my [Wiimote+Ubuntu][10] setup. Mission accomplished.

   [1]: http://en.wikipedia.org/wiki/Gakken_EX-System

   [2]: http://ocw.mit.edu/OcwWeb/Electrical-Engineering-and-Computer-Science/6-002Spring-2007/VideoLectures/index.htm

   [3]: http://kits.sparklelabs.com/

   [4]: //pwnguin.net/photos/sparkle_labs_kit_thumbnail.jpg

   [5]: //pwnguin.net/photos/sparkle_labs_kit.jpg

   [6]: http://www.sparklelabs.com/v2/work.php

   [7]: http://en.wikipedia.org/wiki/555_timer_IC

   [8]: http://www.jameco.com/Jameco/PressRoom/punk.html

   [9]: http://ca.rroll.net/2008/03/22/custom-built-usb-sensor-bar/

   [10]: //pwnguin.net/a-cheap-media-remote.html

