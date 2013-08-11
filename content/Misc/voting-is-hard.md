Title: Voting Is Hard
Date: 2008-11-05

Brandon Holtsclaw, an acquaintance of mine, writes that [ATMs are error free,
so why not voting machines][1]? He's not the only one I've seen making this
comparison, and it's a fundamentally misguided analogy.

### Sins of the past

To describe why voting is hard it's nessecary to discuss the capacity for evil
in the system. For much of America's history, voting was done by voice (_viva
voce_), in public. You might be hassled by party members on your way to
vote, who would attempt to intimidate or bribe you. You then stood before a
judge and declared your vote, or later, turned in a paper ballot. You can
imagine the kind of pettiness that might ensue after you vote against the
interests of your employer or landlord. Eventually this behavior became
commonplace enough that a voting system from Australia was imported: secret
ballot. You voted in privacy, expecting to be shielded from the vice grips of
political machines.

A few problems arose. Ballot stuffing and repeat voting was easy to stop by
handing out a ballot only once to registered voters. **Chain voting**
represented a much harder threat to solve. In chain voting, one person needs
to smuggle out a single official ballot. Our villain then marks the ballot,
and offers it to people along with a promise to buy an unmarked ballot from 
them. In this way you can buy up a series of votes, based on that one smuggled
ballot.

The solution here gets very tricky. You need to make sure that the ballot
turned in matches the ballot given to the voter, which requires inspection of
the ballot at some level. Paper ballots will have a tear away tab with a
ballot ID on it, and fold over, so that poll workers who verify ballots cannot
see the vote.

From the study of the history of fraud we find the need for three fundamental
properties of a voting system:

  * **countability**: the vote has to be countable in a transparent fashion.
This seems obvious, but is a central problem with voting machines

  * **integrity**: the vote must be resistant to fraud, from voters,
candidates or election officials

  * **anonymity**: no individual voter should be able to prove they voted a
certain way

### An Example

Debian elections publish all votes, using an MD5 hash of the ID and secret key
to protect a voter's identity. It seems like overkill, but for DDs it means
that their employer can't find out if they vote against the current interests
of the company. I haven't thought too much about it, but the Debian vote can't
scale, for simple matter of md5sum collisions. The birthday paradox suggests
that as the voting base grows, the likelihood of collisions is higher.
Anywhere two collisions have the same vote is an opportunity to change one of
the votes.

There are more problems, but that isn't the point. The point that Debian
elections may lack complete integrity is to illustrate the difficulty to
engineer something secure, even ignoring implementation flaws and publishing
theoretical systems alone. Intelligent critics of the American election status
quo have proposed systems that have been discovered to come up short to those
three basic demands, and not for a lack of understanding or trying. It just
turns out that **voting is hard**.

### The better analogy

Voting machines are like an ATM that has to keep accurate account balances
without verifying who deposited how much or giving the customer a receipt
proving the deposit ever happened.

   [1]: https://www.imbrandon.com/2008.11.03/ive-never-been-shorted.html

