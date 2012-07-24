Title: What programmer things should every sysadmin know in 2012?
Date: 2012-07-24

*The following is an update to a [post originally made to ServerFault][1] in 2009.*

System administration is more than clicking Next, [cutting your fingers on cagenuts][3], 
and 3am pager alerts. Sysadmins can borrow many of the same skills and tools that 
programmers use daily can be to make themselves more productive, and build a deeper 
understanding of the systems they manage. So without further ado, the list:

**Version Control.**  Be able to generate, read and apply patches. In 2012, it's vital that 
your version control system present a repo wide version history. You should be able to 
write descriptive changelogs and why you want them. Whatever your technology (I recommend 
[git][5] by default), know how to search the repository's logs for keywords and time frames.

**Scripting.** Do something once and be on your way. Do it twice or more, do it once then 
write a script. If you're not using [Powershell][6] or bash, you're working too hard.

**Debugging.** Know how to read a stack trace and how to report relevant errors to your 
software support contact. Documenting the error is easy and helpful, but knowing how to 
fix it takes a lot of investment in reading the code base. Do the part that's easy for you, 
and let the devs handle the part that's easy for them.

**Testing.** Repurpose integration tests for [continuous integration testing][4]. Used in 
conjunction with version control and testing, you have a strong idea of what may have gone 
wrong when and what changed at that time. 

**Peer Review.** Keep your system configuration in revision control, and turn on commit 
mail. Change is core to system administration, not just an agenda item at the weekly staff 
meeting. Do not let Change Management degrade into political battles or displays of 
bureaucratic power.

**Study Cryptography.** System administrators are charge of networked resources; adding 
security as a final step is somewhere between impossible and a very expensive proposition. 
Given how central the role is to . Understanding public key cryptography, password 
handling practices, and encryption in general are be extremely valuable in debugging the 
metric.


 [1]: http://serverfault.com/a/11167/919
 [2]: http://auxesis.github.com/cucumber-nagios/
 [3]: http://www.reddit.com/r/sysadmin/comments/wzs8k/rack_bite_am_i_the_only_one/
 [4]: http://auxesis.github.com/cucumber-nagios/
 [5]: http://www.amazon.com/gp/product/1430218339/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=1430218339&linkCode=as2&tag=jlduggesblog-20
 [6]: http://www.amazon.com/gp/product/1935182137/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=1935182137&linkCode=as2&tag=jlduggesblog-20
