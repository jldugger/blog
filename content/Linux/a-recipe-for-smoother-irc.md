Title: A recipe for smoother IRC
Date: 2008-08-29

IRC is a common method of communication within Ubuntu and many other projects.
I believe Ubuntu policy is that nothing is official unless it's on a mailing
list, but there's still some benefit to having a rendezvous communication like
IRC with others. But frequently, I see things like the following:

> `* novice has joined #ubuntu-foo`

> `< novice> Can anyone help me with bug #53632?`

> `< novice> I applied the patch, but it's not building correctly`

> `< novice> Am I doing something wrong?`

_ Five minutes of silence go by _

> `< novice> Is anybody here?!?!`

> `* novice has left #ubuntu-foo`

The first question can really be anything relevant to -foo, but the end result
is all too common; the person leaves before anyone glances at the channel to
respond. You might imagine it's a simple problem to solve with more
peoplepower, but it's more a question of latency than throughput. So having
tools to handle that latency is nice.

### The ingredients

  * A remote server running sshd

  * An account on said server

  * Screen and irssi installed on said server

  * ssh client on your local machine

### Steps to take

  1. ssh into the remote server: ssh host.com

  2. run screen: screen -S irc

  3. run irc: irssi -C freenode.net

  4. Hit Control-A followed by D to detach from the screen session. Irssi will
continue running until you reattach

  5. set up an GNOME launcher like the following:

[![Launcher Settings][1]][2]

  6. Click the icon, authenticate with the ssh server and presto, **IRC as if
you never left**

### Tips for maximal enjoyment

  * [Public Key encryption][3] can make life a bit simpler

  * Control-A followed by ? (question mark) will bring up the help dialog for
screen

  * alt-3 switches to window 3 in irssi, and so on. This continues for the
qwerty row as well

  * screen -x will attach multiple connections to the same session instead of
disconnecting the others

  * [This page][4] has a more detailed description of the above

### Enjoy!

Now you can just ask questions without having to leave, or monitor a channel
for relevant questions and messages without missing anything. Traditionally,
putting a nick in a message highlights the line on the intended recipient's
screen, or does [other interesting things.][5] A common technique to establish
rendezvous over IRC is a simple ping:

> crweb: ping? I have a question about Qt on embedded

If nobody gets back to you immediately, be prepared to wait, especially on
relatively small and slow channels. If you need to shut down your local
computer, just hit Control+A D to detach. On busy channels like #ubuntu, it's
wise to use nick: highlighting to sort out your conversation from the others.

   [1]: http://farm4.static.flickr.com/3233/2804667136_c993494cdb_o.png

   [2]: http://www.flickr.com/photos/jldugger/2804667136/ (Launcher Settings by jld5445, on Flickr)

   [3]: http://sial.org/howto/openssh/publickey-auth/

   [4]: http://quadpoint.org/articles/irssi

   [5]: http://code.google.com/p/irssi-libnotify/wiki/MainPage

