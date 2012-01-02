Title: Tweaking
Date: 2003-07-24

I once said that the end use of Linux is to customize Linux, after observing my roommate and a friend obsess over 
little things like which screensavers should appear randomly and which shouldn't appear at all. I've tried to avoid
such vanity as tweaking options that only appear when I'm not using the computer, but I have been browsing around 
lately at some of the various performance tools. I've been toying with hdparm, but it seems its allready maxxed 
out there.

I've also been trying to recompile my kernel, and I've been getting closer. I've now actually gotten a kernel to 
boot, and most of the services to run. The hurdle right now is dhcp and dhclient. ifconfig reports the devices as 
up and running, but the card connected to the cable modem never recieves a lease. As you can imagine, debugging 
and online support are difficult when you can't get online. To complicate matters it seems I've nuked the old 
debian install; something about device drivers being overwritten I'm guessing.

Sometimes Debian pisses me off. GAIM has been acting up and crashing lately, so I thought I'd see if there's an 
upgrade. I know that GAIM does update regularly, several of my friends actually run builds from CVS. The latest 
version of GAIM in the unstable deb tree is about a month and two releases old. People bitch about Debian being 
slow to package, this is why. So I grab the 20 meg tarball, and follow the instructions the FAQ suggests while 
downloading. First problem: ./configure fails on a GLIB test. I've run into these sorts of problems before; 
usually the hard part is figuring out what the package you need is named. The package search utility on the Debian 
webpage is supposed to be helpful in this reguard but its usually underpowered. None of the glib results I get 
back are very helpful. I tell it to search descriptions and try again; the very last result is GAIM itself. From 
this page I discover the true name: libglib2-dev. They've conviently attached the lib prefixes to all packages 
reguardless of redundancy. Whispering the true name of the devil into apt-get, allows gaim to configure, build and 
install. But now the computer beeps every 30 minutes or so unexplicably. It takes me about a day to realize that 
its GAIM beeping about the online status of people in my list. After reading over the ./configure output again, it 
seems I'm missing the Audio File Library. Again, the beauty of the Debian package search shines through; search 
queries can only have a single word. I ask on #debian and someone suggests I should install libao. That doesn't 
work. The name, it so happens, is libaudiofile-dev. Now this is somewhat aggrevating since searching for 
"audiofile" returns No Results. Armed with this second library, I trudge onward. Everything appears to be in order 
now, but I'm sure GAIM and Debian haven't let this victory go unnoticed. Eve now, I'm sure the two of them are 
independently plotting, awaiting the oppertune time to strike...

And finally, Debian added some more themes to the base GNOME distrobition. These actually make the system not look 
like amateur crap! I think i've settled on a pretty combination of a few themes. 
