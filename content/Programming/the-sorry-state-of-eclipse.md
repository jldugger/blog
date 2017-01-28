Title: The sorry state of Eclipse
Date: 2009-06-26

So Wednesday marked [the official release of Eclipse 3.5][1] (codename:
Galileo). Eclipse is an integrated source code editor and debugger. It's
roughly comparable to Visual Studio; it supports a number of languages through
plugins (PHP, for example), and tools (JUnit, for example). It's also one of
the few Open Source tools that goes beyond text editing and debugging comes
close to supporting Software Engineering tools like UML and formal
specifications.

Eclipse proved an invaluable platform for a compilers class, where ANTLR plug-
ins gave excellent tools to review the grammar stripped of the handling code.
It's also handy for embedded platforms, where the alternatives are even worse.
I last wrote about eclipse approximately [a year ago][2]. I haven't revisited
the subject of the CDT, but I hope it's improved with time.

The problem is, the Ubuntu package of Eclipse has not improved with time, but
stood still. 3.2.2-5ubuntu3 is the current package version, and been there
since Hardy. Importantly, when Hardy was released, Eclipse 3.2 was already 2
years old. The current proposal from [this bug report][3] is to remove it
entirely. And it seems like a reasonable suggestion. Why leave a package that
many revisions behind for people to find and suffer from? It's a sentiment
that [Debian agrees][4] with.

A tragic question comes to mind: if Eclipse is a tool that programmers want or
need, why is Eclipse neglected in volunteer groups like Debian or MOTU? It's
not the case that Eclipse is too fast moving; they have a yearly release
cycle. It's not that there aren't dozens of interested people; the "upgrade
Eclipse" bug has countless subscribers. Is it that Debian and Ubuntu
developers don't need Eclipse, or maybe even dislike tools beyond vim/emacs?
Or maybe Eclipse's challenge is that building software with Eclipse is simple,
but building Eclipse itself is not. **Is it possible to build Eclipse with
Eclipse?**

Given the apparent neglect, it's probably time to remove it from the archive,
acknowledge that users will be grabbing from upstream directly and **start
dealing with the consequences**. Eclipse forms an ecosystem of plug-ins, with
a rather sparse set of core features in their absence. Plug-ins don't appear
to make many assumptions about the host platform; one bug reporter notes that
[Eclipse SVN plug-ins][5] use Subversion 1.6 libraries, which upgrade working
directories to 1.6. This breaks compatibility with the SVN shipped with
Ubuntu.

I assume it's much easier to backport SVN 1.6 than fix Eclipse packaging, so
perhaps the barrier would be lower if we acknowledged this external dependency
exists. **So who should be consulted on removing Eclipse**? MOTU? The Java
Team? The Eclipse Team?

   [1]: http://www.eclipse.org/org/press-release/20090624_galileo.php

   [2]: //www.pwnguin.net/eclipse-disaster.html

   [3]: https://bugs.launchpad.net/ubuntu/+source/eclipse/+bug/123064?comments=all

   [4]: http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=526489

   [5]: https://bugs.launchpad.net/ubuntu/%2Bsource/subversion/%2Bbug/382048

