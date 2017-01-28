Title: Cooking for Everybody
Date: 2008-07-02

One of the reasons I love open source is its entrepreneurial spirit. If you
don't like the way a company is handling their print driver, [go off and write
an operating system that meets your definition of liberation][1]. If a project
manager is refusing your favorite UI patches, you can fork the UI while still
sharing the underlying [networking libraries][2]. But critics of this right-
to-fork suggest that most people can't do this; they just don't have the
skills. In many cases, they're right. I don't think I'll ever be capable of
contributing directly to emacs, for example. Or to gcc. Sure, the right to
fork has benefited me by allowing smart people to write egcs, I can donate
money to help defray costs of hosting and conferences etc., and I can hire
someone to write the code for me, but these challenges are amplified in small
or trivial projects; there's an amount of learned helplessness from decades of
"software users" and "software developers". I think overcoming this state of
learned helplessness requires that people write at least one program to do
whatever it is _they_ want.

### Cooking for Engineers

Let me now introduce an analogy. Programs are at their heart, a sequence of
instructions, with the goal of transforming a set of inputs into a relevant
output. Everyone and their dog makes the following tired analogy, but I
promise to make a meal out of this: cooking at its heart is a sequence of
instructions, with goal to transform a set of ingredients into a tasty dish.
And for every _Joy of Cooking_ soldier who claims cooking is an art, there's
at least one chemical engineer making a science of it. If you've seen enough
engineers at work, you know when it comes to calculations they generally have
one hammer at their disposal, to be used on everything in sight: Spreadsheets.
They take their years of education and experience with formulas and systems
and cram them into a spreadsheet. Sure, many of them were required to take a
"C for Engineers" course (from the same train of thought that will some day
bring us "Partial Differential Equations for Elementary Educators"), but if
the subject's not on the FE exam, who cares? So it comes as no surprise to me
to see this particular abuse: [Cooking For Engineers][3]. I'll use [one
particularly tasty example][4].

I've upset more than one engineer who tried to show this "new" site to me,
expecting shocks of horror or awe, but getting a slight ribbing in return
instead. For extra credit, take a look at [this recipe for chicken pot
pie][5]. Here's the deal: the leftmost column are ingredients, and each column
after that is an instruction with inputs on the adjacent rows of the column to
the left. Essentially, this is taking a beautiful data structure and cramming
it into a table. This looks like an engineering tactic through and through,
but one minor flaw stands out: many recipes use only Imperial units, instead
of metric. This reads like cooking for web designers, and the [ bio][6]
confirms it:

> He has worked as a network engineer, software programmer, PDA hardware
designer, computer vision researcher, and, most recently, notebook hardware
application engineer. Michael holds a Bachelor of Science from the College of
Engineering at University of California, Berkeley in Electrical Engineering
and Computer Science.

### Cooking for Computer Scientists

This is a guy who ought to know better. He did ask [an expert][7] for advice,
but one of those two misunderstood the other (or possibly both did). I won't
bother trying to spend a lot of time trying to rescue the format, other than
to say that overlapping colors _might_ make groupings more obvious. Instead
I'm going to propose we go back to the basics &mdash parse trees.

[![cheese cupcake recipe][8]][9]

Please forgive my poor lineart (I have no idea what to put for "place" or
"top"), and focus on the information being conveyed here. The relationships
between ingredients and actions are now explicit, ingredients are visually
distinct than actions; since the information needed is different, this will be
handy. Equally important is that the input and output have the same type. In
the extra credit example, this is done implicitly in order to fit the recipe
into a table without getting ridiculous. You can probably spend all day
dreaming up just the perfect way to diagram that recipe, but I only spent two
hours with Inkscape on it. You could add cooking instruments, balance the
spacing and alignment, redesign the horizontal layout to represent time, you
could make it interactive and double click to expand or collapse parts of the
diagram; lots of random stuff with just the visual layout without changing the
underlying instructions. But I'll leave the advanced transmission of
information to humans to the Edward Tufte's of the world.

But it's also important to notice that we have standard algorithms for
manipulating that data structure; there's all sorts of things you can do. You
can store the measurements in metric and translate units based on a would-be
chef's preference. You can scale up or down a recipe to N people. You can even
translate it into a standard numbered step recipe. Or you could translate it
into instructions for two people (parallelism!). You could calculate the
number of cupcakes you can make if you only have so much of each ingredient.

At its core, that picture models the flow of ingredients through a set of
simple processes. I haven't shown you any recipes where this matters, but we
don't need a tree structure, just a [DAG.][10] The package diagrams from
[earlier][11] are also DAGs. The important thing about DAGs is that paths can
cross, but never loop. Languages designed to handle the flow of data through a
network are called [Dataflow Languages][12], though many also handle full
graph structures. Restricting the model of computation to a DAG then means
it's technically Turing incomplete; this has both good and bad consequences. I
should note that it's been proven that spreedsheets, that hammer in every
engineer's pocket, is also fundamentally a DAG. Here's a spreadsheet I used to
split the bills with my roommates visualized:

[![bills][13]][14]

So why am I picking on poor engineers, if it's all the same? Because
spreadsheets are terrible on understandability. Spreadsheets marry
presentation with calculation, and I think it's a fundamental mistake. They
form a DAG, but via well hidden textual pointers. If you accidentally form a
cycle, it's probably unwanted, but good luck tracking down where things went
wrong. Moreover, they're oriented towards a single set of data points. I made
a new spreadsheet page every month based on a template, because Calc doesn't
work the way I'd like.

There's tons of other applications. I'd been taking notes about this and
brainstorming for a while now, but now that [Bryce is making overtures][15]
toward a new project doing precisely this, I think I'll share my notes with
everyone, in hopes that I get the program I want without having to write a
line of code ^_^. His writing seems to be more profound than he realizes
(emphasis mine):

> I could no longer do without one of these silly cron jobs than I could have
done **without Microsoft Excel** a decade ago. [...] The realization sank in
at that point, that our computer UI paradigm really stinks for what we
actually use our computers for.

Indeed, the internet has changed things dramatically and our computing hasn't
stopped to notice. He goes on to say that he used none of the desktop metaphor
to write his blog post. Bryce, you're doing it wrong. As I'm writing this, I
have several Firefox tabs viewing various research and reference pages, gedit
viewing some text notes I'd been keeping on this subject, Inkscape for drawing
the graphics, and an editor open to write this post! We do occasionally
originate documents, so don't throw the baby out with the bathwater. As reddit
user damienkats [notes][16], "Saying documents vs. streams is like saying cars
vs. highway."

### Cooking for Everybody

It is possible to expand the spreadsheet model into a stream processing model.
Each node repeatedly consumes the necessary inputs, runs an algorithm and
produces whatever intended output to the next process(es) in line. When the
inputs aren't available, the node blocks until they are. If one of the inputs
"runs out", the node halts. As an example, a processing node could read in RSS
XML one item node at a time, and split the output into items with enclosures
and those without. A more complicated example could be a node that takes RSS
XML items, and if the link property is a .torrent URL, moves that into an
enclosure field and sets the other enclosure properties accordingly.

This form of programming has some tremendously productive properties primarily
to the benefit of new programmers. Firstly, it's easy to trace a change in one
part of the program to where it affects the rest. You don't need to maintain a
ctags database and query it to determine what semantics other functions that
call the function you just changed rely on. Secondly, as Sean Parent of Adobe
Systems [noted (at 17:45 in through 22:00)][17], the acyclic property
eliminates the need for inductive reasoning about your program. Each node is
logically dependent on only those that came before it. Thirdly, it's simple to
see that as long as the input isn't infinite, these systems will halt.
Additionally, the looping structure makes common "one off" loop errors
basically impossible.

Many of the fundamental software design techniques still work, even if the
training wheels are on. Firstly, I don't think you'll need UML, but you could
still model your data, and your programs! You could still do "write, compile,
test" cycles. Peer review might be easier, if changes can be succinctly
described. You could still have revision histories and merge strategies. You
could still do test plans, construct test cases and file bug reports. You
could do formal correctness proofs. You could load up a debugger and
investigate the output and input of any given node. You could still time the
whole program for performance, and even analyze individual nodes for
bottlenecks. You could modularize, reuse and rewrite.

Such a design is also sufficiently advanced enough to cater to experts as
well. It's very difficult to design a UNIX pipeline that uses more than one
stdin or stdout, it defies the very meaning of "std." Taking another step
towards UNIX is plausible; there's no reason we can't have processing nodes
that buffers input until EOF, in fact sort would likely require that kind of
bottlenecking. Equally important is what I mentioned earlier; dataflow
languages not only handle parallelism, many were built for it! One naive way
is to run node as a process and use common IPC to pass data between them.
Pipes do this, but you could also use shared memory or threads, as long as the
system structure is adaquately defined.

And while the system itself can't form loops, experts should be able to write
new algorithms that do operate as a processing node and incorporate them into
designs or share them with others. They could can also provide some
information about the nodes themselves for use during design -- Big O runtime
analysis, multithread support, blocks until EOF, input types and ranges,
descriptions, revision control URL, etc.

All of this adds up to a healthy environment where maybe we can undo some of
the damage the past twenty years has taught people about the relationship
between them and their computers.

   [1]: http://www.gnu.org/gnu/gnu-history.html

   [2]: http://developer.pidgin.im/wiki/WhatIsLibpurple

   [3]: http://www.cookingforengineers.com/

   [4]: http://www.cookingforengineers.com/recipe/181/Cheesecake-Cupcakes

   [5]: http://www.cookingforengineers.com/recipe/42/Traditional-Chicken-Pot-Pie/trn

   [6]: http://www.cookingforengineers.com/article/138/About-Cooking-For-Engineers

   [7]: http://www.orthogonalthought.com/blog/index.php/2007/07/tufte/

   [8]: http://farm4.static.flickr.com/3161/2619872079_25dd4c5036_o.png

   [9]: http://www.flickr.com/photos/jldugger/2619872079/ (cupcake by jld5445, on Flickr)

   [10]: http://en.wikipedia.org/wiki/Directed_acyclic_graph

   [11]: //www.pwnguin.net/the-popular-emergence-of-apt-git.html

   [12]: http://en.wikipedia.org/wiki/Dataflow_programming#Languages

   [13]: http://farm4.static.flickr.com/3284/2619872075_fed5a76a48_o.png

   [14]: http://www.flickr.com/photos/jldugger/2619872075/ (bills by jld5445, on Flickr)

   [15]: http://bryceharrington.org/drupal/docs_vs_streams

   [16]: http://www.reddit.com/info/6owbv/comments/c04h2wb

   [17]: http://www.youtube.com/watch?v=4moyKUHApq4

