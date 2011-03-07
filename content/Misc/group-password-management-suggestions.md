Title: Group Password Management Suggestions?
Date: 2009-04-08

In IT, it's common to segregate responsibilities not to individuals, but
groups of people. This is handy for vacations, conferences, meetings or
promotions -- power isn't endowed to a specific person and the redundancy
means high throughput when necessary.

One problem is that not all systems we work with understand groups. In
particular, they don't support clustering identities into identical roles.
Active Directory and Unix have Organizational Units and groups, so for most of
our systems, this is not a problem. But for websites, it's often the case that
a single account is created, forcing us to "share" authentication amongst the
group. Moreover, these systems are proliferating, increasing the number of
shared secrets we need to keep.

Password proliferation is not just limited to groups; many people have dozens
of passwords for various websites. Web browsers are including tools to
remember these things, and there's several existing tools for individuals such
as [PasswordSafe][1] or [Seahorse][2].

However, you will quickly run into trouble extending this software to team
use. Publishing updates is tricky; the worst situation is having multiple
versions of an encrypted flat text file floating around (do I have the latest?
did Bob update his version before he published the new version?). If you
centralize the file, you have to think carefully about remote update or risk
overwriting the only place that anyone actually knew the password.

My question is, is there any password management published and ready for use,
which makes the leap from single users to groups? Bonus points if your team
actually uses it. If a clear victor emerges, I'll make sure to blog a more
detailed review.

   [1]: http://passwordsafe.sourceforge.net/

   [2]: http://packages.ubuntu.com/jaunty/seahorse

