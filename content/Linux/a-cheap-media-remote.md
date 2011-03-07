Title: A cheap media remote
Date: 2008-12-19

It's been a while since I blogged about something I pay attention to in
Ubuntu, get ready! Today I talk about using a Wiimote to watch videos.

If you already own a Wii and a [cheap Bluetooth adapter][1], there's a
lot of fun stuff you can do in Linux with the Wiimote. The simplest and most
immediately useful is to use it as an [alternative input device][2].

A quick rundown: install package  wminput, modprobe uinput, and run sudo
wminput -d . wminput will listen on bluetooth for the wiimote, and translate
into mouse cursor movement and keystrokes according to it's default config
file. Press 1+2 on the WiiMote to put it into discovery mode, and it should
connect in a few seconds.

I use the following as my wminput config file:

    # remote - settings appropriate for totem/mplayer/mythTV

    Wiimote.A = KEY_SPACE
    Wiimote.B = KEY_ENTER
    Wiimote.Up = KEY_VOLUMEUP
    Wiimote.Down = KEY_VOLUMEDOWN
    Wiimote.Left = KEY_LEFT
    Wiimote.Right = KEY_RIGHT
    Wiimote.Minus = KEY_BACK
    Wiimote.Plus = KEY_FORWARD
    Wiimote.Home = KEY_ESC
    Wiimote.1 = KEY_F
    Wiimote.2 = KEY_PROG2

Put it in ~.cwiid/wminput/default and you won't have to specify it on the
command line! The idea is that D-pad left and right scan through the video, up
and down turn the volume down, A triggers pause/play, and 1 toggles
fullscreen. I don't know what KEY_PROG2 is good for, but it felt wrong to
leave a button unmapped. No tilt sensing or mousing here, since I want to be
able to set the wiimote down and enjoy the show.

Some might think that KEY_PLAYPAUSE would be more function specific than
KEY_SPACE, but they are wrong; none of the players appear to support that. My
hope is that in the future I can find settings more universal; my USB keyboard
has buttons that trigger rhythmbox, so maybe that mechanism can be exposed.

There hasn't been a lot of activity upstream, aside from applying a patch
from Mario Limonciello (superm1). I'm not sure if it's a sign of maturity or
of project failure.

   [1]: http://www.amazon.com/gp/product/B0019SI266?ie=UTF8&tag=jlduggesblog-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=B0019SI266

   [2]: https://help.ubuntu.com/community/CWiiD

