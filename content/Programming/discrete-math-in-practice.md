Title: Discrete Math in Practice
Date: 2008-08-14

[Jucato][1] asks:

> “What are the practical applications of discrete math in actual software
development?”

**Discrete math is everywhere in programming and Computer Science.** Its
probably more applicable in general to programming than calculus is. There are
several simple but significant situations where discrete math suits software.
The simplest case is Big O notation in loops, where Riemann sums are used to
formalize programmer intuition. But almost nobody cares about intelligent
program analysis anymore. We measure programs in terms of lines of code and
cost to write, not cost to run, and God forbid we prove anything correct. I
think that says something damning about the state of the art.

But that's just a start. Graphs in computation (specifically DAGs - directed
acyclic graph) is a subject I've [touched on][2] before, mainly as an
alternative model of computation. But we use graphs in general all over the
place in software, frequently as **models**. There's a famous graph of system
calls to serve a web page in Apache on Linux versus Windows; optimal layout of
such a monstrosity is a graph theory problem that programs like GraphViz were
built to solve. We model lots of things in programming with graphs, and rely
on graph theory to do interesting things with them. UML is a famous example of
graphs in software development. If you want to write [OCL][3] about UML and
have a program verify that the software matches, you better hope the guys who
wrote the _verifier_ thought discrete math was practical. But then again,
nobody in the open source world uses UML. And OO itself is not without its
[detractors][4].

Okay, so how about something fundamental to UNIX in practice: **regular
expressions**. It is a central theorem that regular expressions can be
represented using any of a number of kinds of simple **finite automata** (and
that you can represent those diagrams as regular expressions). If your program
wishes to handle regular expressions, an NFA is suitable for the job. It's
important to note that a regular expression match runtime should be linear in
the length of the input, and not affected much by the length of the regular
expression. But this is yet another [lesson lost][5] on today's practitioners
of software development.

This is getting pretty dismal, no? There's hope yet. Imagine if you built a
**dependency graph** from the Debian archive, where every package was a node
and every dependency was a directed edge. We wish to find an order in which to
install these such that no installed package ever depends on something not
installed. A naive implementation would be slow and possibly never terminate.
An implementation informed by graph theory would reduce the problem to
topological sort. Every DAG has a topological ordering, placing nodes into
"layers," where each "layer" depends only on the "layer" before it. Thus you
can install the innermost layer first, and work your way out. But _only_ if
you have a DAG; detecting and resolving cycles is the better half of solving
this problem in real life, and is no less a graph theory problem.

This principle applies in many places. CPU instruction reordering.
Spreadsheets. Makefiles. Other examples from the Wikipedia article. But maybe
you just want to play a game inspired by fundamental discrete math. For your
consideration, [gPlanarity][6] (package name: gplanarity).

   [1]: http://jucato.org/blog/some-short-updates/

   [2]: http://pwnguin.net/cooking-for-everybody.html

   [3]: http://en.wikipedia.org/wiki/Object_Constraint_Language

   [4]: http://steve-yegge.blogspot.com/2006/03/execution-in-kingdom-of-nouns.html

   [5]: http://swtch.com/~rsc/regexp/regexp1.html

   [6]: http://web.mit.edu/xiphmont/Public/gPlanarity.html

