Title: Eclipse Update
Date: 2009-07-20

> <doko> tjaalton, pwnguin: and I'm filing a bug report to
remove this package again, because it does include a handful or more third
party libs inside the eclipse package. if you want to keep eclipse, please fix
these bugs, hint, hint ;) 


 Matthias Klose (doko) has [uploaded a new version of Eclipse][1] to Karmic.
However, things could be better. Firstly, there's still 3.5 to contend with.
Moreover, as the quote above indicates, the current package violates Debian
Policy, in particular, [4.13: Convenience copies of code][2]:

> Some software packages include in their distribution convenience copies of
code from other software packages, generally so that users compiling from
source don't have to download multiple packages. Debian packages should not
make use of these convenience copies unless the included package is explicitly
intended to be used in this way. If the included code is already in the Debian
archive in the form of a library, the Debian packaging should ensure that
binary packages reference the libraries already in Debian and the convenience
copy is not used. If the included code is not already in Debian, it should be
packaged separately as a prerequisite if possible.


 The Debian project prefers explicit copies of third party libs to be in a
systemwide package, for sanity's sake. The reasons are fairly good:


   * Firstly, it's inefficient. Duplicated libraries can't be shared with
other executables, on disk or in RAM.

   * Most UNIX programs already do this, so it's an expected norm. If a Debian
Developer is looking for source code to a library to track down a bug, it's
easy to accidentally assume the existing package was used.

   * Without a package and corresponding metadata, there's no way to search
for all instances of a given library. If you do find a bug in a library, you'd
like it to be fixed everywhere at once.

   * One reason you might absolutely need to fix a bug everywhere at once is
security flaws. With the stated policy, it's much easier to verify that it's
fixed everywhere.


 Since doko's upload, [another upload][3] took care of some build
dependencies, but nothing has addressed the library issue, likely because
nobody's been informed (directed comments on IRC doesn't count as notice!),
and unlike doko's comment suggests, no bug has been filed. If anyone wants to
tackle this, #ubuntu-motu is the place to look for guidance.

   [1]: https://launchpad.net/ubuntu/+source/eclipse/3.4.1-0ubuntu1

   [2]: http://www.debian.org/doc/debian-policy/ch-source.html#s-embeddedfiles

   [3]: https://edge.launchpad.net/ubuntu/+source/eclipse/3.4.1-0ubuntu2

