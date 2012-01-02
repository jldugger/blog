Title: Kernel Ninja
Date: 2003-10-31

It's been a while, but I've gotten back into a tweaking mood. Since the last posting I've managed to recover to a 
Debian build, build a working NAT to share the cable modem, and left for school in August. Linux has held up fairly
well; the dorms have started to get very nervous about windows install insecurity. A friend of mine accidentally 
left the network cable plugged in when he decided to remove XP for win2k, and got blaster as a result. They've had 
him shut off for a week now, partially because the tech they sent out didn't actually remove blaster. Why they 
don't just block the port in the first place is beyond me. In contrast, linux grabbed an ip lease early on, and 
hasn't had any problems since (that weren't my own doing).

So earlier this week I decided to enroll in the graphics course next semester, and having an openGL stack the 
professor likes lent me the motivation to try attacking the kernel again. For a moment I forgot that I ever built 
my own kernel sucessfully, perhaps because QNX threw me for such loops when I decided to try it out on the second 
disk (I was working with some developers to hex edit the boot sector-- eventually I decided that I could do
without QNX and its delicious GUI). Anyways I ran into the same old problem with dhcp never getting a lease on my 
own build; compiling the drivers into the kernel resulted in reversing the aliases, it seems. So what was eth0 is 
eth1, and vice versa. To fix this, its time to build modules. Then its off to accellerated X and finally GL. Then 
I can go online and brag about how I have the lowest and therefore least valuable glgears score ever!

Sadly, I was not able to use my picross idea as an AI project; instead I'm working with Thaddaeus Frogley's C++ 
Fight! framework. I swear, I didn't make up that name. He say's his parents made it up, and I believe him, since 
they are English, after all ;) So for now, the wx picross project is on the back burner. Interestingly enough, 
Thaddeus has some stuff with wxWindows on his page, mostly how to set it up in VS6. It's not his fault though, 
he's spent the last few years working on Grand Theft Auto for XBox and other games, so he gets a get out of 
DLL-Hell free card.

Oh, its Halloween too. As usual for Kansas, the weather took a sharp cold turn just in time to ruin all the 
children's day of candy feasting. I remember one time my brother went trick or treating in the snow as a ninja.
Well, at least, he was a ninja underneath the down overcoat. Stealth frozen ninja sneak attack! 
