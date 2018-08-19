Title: Dispelling the Git Illusion
Date: 2018-08-19

The DevOps world is wonderful. Amazing! Life changing, even! You practice [Infrastructure As Code][1], so if you want 
to make a change, you write some [Puppet][2] code, merge the commit into master, and within an hour your fleet of 
servers has your change, and the world is a little bit better for it.

This is a wonderful, simple workflow with a dangerous illusion: the git repo *is* the system. This **git illusion**
can lead developers astray. An object wasn't in the git repo before, and now it does, so now it is in the system. So
logically, deleting code from the system should be the same as deleting code from production, right? This theory sadly
does not hold, as you may discover after pushing out a bad puppet module. `git revert` will *not* nessecarily cure
your ills!

At the heart of this illusion is a false dichotomy. Server state resides in *three* possible states, not two:

1. Managed
2. Deleted
3. *Unmanaged*

This hidden Unmanaged state is the default state of the system, and so when you git revert, you revert to the
Unmanaged state, not a deleted state. And as you might imagine, a long running system living can accumulate garbage
(residual configurations) over time. Here's three approaches to taking out the garbage:

1: The "clean up after yourself" principle
------------------------------------------

Any time a PR intends to remove a resource from code, **explicitly delete the object from code.**

This is doable when you know when resources are being removed. But it has a couple of drawbacks. Firstly, it sucks to
add code to the system to handle things you no longer need. Secondly, over time your codebase is a record of dead
things. You'll want to shake out your code base from time to time, effectively shifting the cleanup problem to the
code base rather than solving it. But at least you have a single point of truth to audit, rather than thousands. 

2: The Cattle principle
-----------------------

After any PR is merged, **delete everything.**

When you have only a handful of servers, it's tempting to treat them like pets. Give them cute names, and give them
loving care and special attention when they get sick. As your operation grows, it's pretty common to start treating
servers like cattle. Serialized numbers, standardized configurations, and when they get sick, it's cheaper to take
them out back behind the barn and prepare them for the glue factory. Effectively, you're deleting everything and
starting over to maintain the illusion.

To pull this off, you'll need surplus capacity for a rolling upgrade, and need it for a longer duration than if you
simply upgraded in place. And if you're dealing with state backends like [SQL servers][4] or file systems, then you 
need *very* careful planning to avoid data loss.

3: The Garbage Collection principle
-------------------------------

Automatically **reap unmanaged resources** via code

In some cases, you pretty much know where the garbage churns. A web server is likely to collect sites in
`sites-available`. Scheduled tasks are likely to aggregate in `/etc/cron.d/`. We can bake this domain knowledge into
the code base, using widely available tools. The `file` resource supports a [`purge`][3] option which implements this
exact policy.

This policy has some caveats of course. You actually have to know what's safe to purge, and which locations are not
purged. You have to be prepared to delete things that weren't in explicitly created via Puppet. Even if you're
confident nobody on your team will 'forget to add the conifg to Puppet', you'll have to deal with complex interactions
between the purge system and system packages that install things outside Puppet, which typically leads to relying on
them less.

To summarize: **Unmanaged is not the same as deleted**.

   [1]: https://devops.com/meet-infrastructure-code/

   [2]: https://puppet.com/

   [3]: https://puppet.com/docs/puppet/5.3/types/file.html#file-attribute-purge

   [4]: https://vimeo.com/21372341
