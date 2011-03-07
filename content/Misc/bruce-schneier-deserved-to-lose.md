Title: Bruce Schneier deserved to lose
Date: 2010-06-19

NPR held and broadcasted [a debate][1] on the resolution, "The cyber war
threat has been grossly exaggerated," and invited a sophisticated panel to
debate for and against it. The format of Intelligence2 debates is two panels
of speakers competing to change the audience opinion. So even if the audience
comes in with a massive majority opinion, the merit of the debaters is judged
by the change in opinion after the debate concludes.

NPR's debate organizers do a good job of recruiting people with experience on
the subject rather than experience with policy debate and the more [estoeric
philosophical techniques][2] to "win". The team arguing cyberwar is a bogeyman
consists of [Bruce Schneier][3] and [Marc Rotenberg][4]. The team arguing that
cyberwar is real and dangerous is [John M. "Mike" McConnell][5] and [Jon
Zittrain][6]. I've actually heard of two of these people, which makes me feel
just a bit smarter. As I subscribe to Schneier's blog (squids or not), I was
rooting for his side to win. Alas, **rather than pursuading the undecided
audience, his team lost a few supporters to the other side**, and lost by the
rules of the debate.

But having listened to it, it's pretty clear Schneier's team made several key
mistakes. Firstly, they let the other team decide what statements were under
scrutiny. If all your opponent has to do is not make exaggerated claims during
the debate to win, you'll lose pretty easily. You can see this principle in
action as Schneier tries to quote McConnell, only to have McConnell dismiss it
as out of context and a misquotation. Instead, they should have gone after
public figures and decision makers not present — McConnell isn't the only
politician or bureaucrat talking up cyberwar. I'm not about to go through
CSPAN transcripts, but surely Lieberman, who's introduced a bill I understand
would authorize the president to use an internet kill switch (and effectively
censor people) made an exaggerated claim to support that broad reaching power.

Meanwhile, Zittrain and McConnell pretty much offered a no contest argument.
They admitted that newspapers wrote exaggerated headlines, that the "cyberwar"
attacks against Georgia may have been self inflicted, and that the main risk
was not to our military but to high profile financial targets. By carefully
avoiding any sensational or _exaggerated claims_ they gave the other team
nothing credible to point at as evidence. McConnell's main cyberwar threat
example was catastrophic data loss at US moneycenter banks who handle
trillions of dollars daily, and Zittrain's was the Youtube-BGP screwup.

In closing statements, Schneier and Rotenburg attempted to argue against the
policy that would emerge from a loss, effectively an appeal to heads in sand.
**Instead of focusing on the negative policy outcomes, they should have
addressed the likelihood of the oppositions's two threats** in closing
statements. I was never on a debate team but that seems like an obvious thing
to do! The banking argument is a classic confusion of consequences for risk
that Schneier is renowned for pointing out. The Lieberman bill even makes [the
distinction][7]:

> 18) RISK.—The term "risk" means the potential for an unwanted outcome
resulting from an incident, as determined by the likelihood of the occurrence
of the incident and the associated consequences, including potential for an
adverse outcome vulnerabilities, and consequences associated with an incident.

As determined by _likelihood_ and _adverse outcomes_. Consider a common
example, one my own website faces and which I think McConnell alluded to with
his "millions of attacks daily" comment: brute force SSH login attempts. They
happen quite frequently, but because they are easily [guarded][8]
[against][9], I argue the threat is low. With the proper safeguards in place,
what is the remaining likelihood of a brute force attack succeeding? Slim to
none, because I have no guessable common system accounts and the [keysize is
massive enough][10] to make such attacks infeasible. The consequences are high
but the likelyhood is miniscule, so the risk is low. I'm much more worried
about keeping all my webapps patched than this SSH spam attack.

So what is the likelihood of the threats presented? A major bank losing all
customer data is pretty slim I'd say. They have incremental backups and
transaction logs and firewalls, and redundant file systems and offsite
backups, and [things I'm missing][11] because I haven't spent a lifetime
working for the financial sector. It would take more than the "two weeks"
Zittrain suggests for a crack tiger team to construct a plan to completely
wipe out customer records in seconds. Cyberwar could still do some damage,
but, importantly, no more than they experience and plan for daily. Computers
today are failure prone, even without script kiddies and trained military
strikes, so private firms have all kinds of insurances, countermeasures and
recovery plans in place. The consequence might be 7 trillion dollars, but the
risk of complete loss of records is minuscule, so the threat is small and
therefore exaggerated. Unregulated credit default swap markets present a
greater risk to banks than this.

Meanwhile the Youtube-BGP attack was resolved [within two hours][12], and
early warning systems (more like fast after-the-fact alerts, really) are in
place to watch for bogus announcements. So the outages from a network routing
attack can be resolved relatively quickly. When the beer passing brigade fails
en masse the companies that profit from it figure it out and quickly. The
internet was built to be resilient to attack and Zittrain even admitted an
adhoc networks were a sensible approach to a destabilized internet.

In conclusion, I think the cyberwar threat is overstated, but the weak case
Schneier and Rotenburg presented at the debate was sufficient cause for them
to lose both the debate and majority consensus. This doesn't mean we should be
arming the president with a kill switch or ignore the dangers of fraud and
hacking, but we should prioritize based on risks rather than consequence, and
the risk is far greater elsewhere.

   [1]: http://www.npr.org/templates/story/story.php?storyId=127861446

   [2]: http://en.wikipedia.org/wiki/Kritik

   [3]: http://www.schneier.com/

   [4]: http://en.wikipedia.org/wiki/Marc_Rotenberg

   [5]: http://en.wikipedia.org/wiki/John_Michael_McConnell

   [6]: http://futureoftheinternet.org/blog

   [7]: http://hsgac.senate.gov/public/index.cfm?FuseAction=Files.View&FileStore_id=4ee63497-ca5b-4a4b-9bba-04b7f4cb0123

   [8]: http://www.fail2ban.org/wiki/index.php/Main_Page

   [9]: http://www.debian-administration.org/article/SSH_with_authentication_key_instead_of_password

   [10]: http://en.wikipedia.org/wiki/Key_size#Asymmetric_algorithm_key_lengths

   [11]: http://en.wikipedia.org/wiki/Disaster_recovery

   [12]: http://www.ripe.net/news/study-youtube-hijacking.html

