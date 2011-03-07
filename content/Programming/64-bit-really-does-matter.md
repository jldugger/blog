Title: 64-bit Really Does Matter
Date: 2011-02-04

In a stunning display of confidence, [Paul Tagliamonte][1] stops just short of calling for dropping 64bit 
Ubuntu desktops. Because PAE will save the day, naturally.

By day, I am a Java developer. This means I know the pains of memory constraints all too well. I recently 
upgraded my desktop, as Paul suggests developers do, to 64bit in order to accommodate the various RAM
hungry IDEs and VirtualBox VMs we employ. And at my previous job, I helped guide the plan of action when 
the Blackboard Angel app servers ran out of RAM. /3G (windows boxes) helped, but not enough. I told the 
sysadmin that /PAE wouldn't help at all, and it didn't.

Why not? Because the truth is more complicated than a number of bits. At this moment, the highly popular 
StarCraft 2 recommends 2GB of RAM. 4GB on OSX. World of Warcraft recommends the same. These are single 
applications, geared towards users, reaching the upper limits of the [default split][2] between RAM 
storage and "other" uses. I can't say when commercial games will break 3 or 4 GB, but it's coming. That 
milestone was a long way off in 2004, but certainly not outside hobbyist reaches shortly thereafter, 
and has been a virtual requirement in the datacenter for some time now. Open source won't be far behind, 
and in some ways, has been leading the charge.

The question is, what does PAE buy you? PAE gives you an extra level of indirection at the page table, 
but you must specifically program the OS for it. In effect, you can expand individual page tables, at 
a small CPU penalty. PAE is transparent to the application; as far as it's concerned there are no other 
processes or pagetables. So 4GB remains the ceiling here. That's why PAE didn't help our IIS boxes — 
once a single application wants more than that, the writing is on the wall. And that day is fast 
approaching.

In effect, your if your multitasking CPU is juggling processes, it can have multiple processes in the 
air no bigger than 4GB. But, you ask, if the OS can use the extra space, can't we provide a system call 
or workaround for the applications that want to grow beyond 4GB? Sure can. But nearly everything already 
builds on 64bit, so users might as well leapfrog the whole PAE mess. 64bit is far better tested than PAE 
deployments, and it's dramatically easier to build since compilers have a 64bit arch defined for you 
already, and will help you spot bad code. There's no reason to "port" applications to PAE when we've 
already got a full 64bit stack.

64bit mode has some downsides ("storing all those zeros"), but the simple matter is that we're going to 
be growing out of it soon. PAE is simply insufficient and should not be relied upon.

Except on my laptop, which doesn't support the whole 64-bit fad.

   [1]: http://blog.pault.ag/post/3107062816/why-64-bit-computing-is-really-dumb-right-now

   [2]: http://kerneltrap.org/node/2450