Title: Undefined reference to personality?
Date: 2008-07-15

When I was a TA for an undergraduate course in operating systems, I'd often
field simple questions as this is sometimes students' first exposure to GNU
tools. One or two students invariably came to me with a problem exemplified by
the following:

> **hello.cc:**

    #include "hello.h" 
    using namespace std; 
    void Hello::print() { 
       cout << "Hello World!" << endl; 
       return;
    }


> **hello.h:**

    #include <iostream>
    class Hello {
       public:
       void print();
    };

> **main.cc:**

    #include "hello.h"
    int main() {
       Hello* h = new Hello();
       h->print();
       return 0;
      }


This code is fine, even by pedantic standards. However, new students often get
tripped up:

`jldugger@jldugger:~/test $ gcc hello.cc main.cc`

_several lines worth of linker errors ommited]_

`main.cc:(.text+0x176): undefined reference to 'std::ios_base::Init::~Init()'`

`tmp/cc2APvWV.o: In function 'main':`

`main.cc:(.text+0x195): undefined reference to operator new(unsigned int)'`

`/tmp/cc2APvWV.o:(.eh_frame+0x11): undefined reference to __gxx_personality_v0'`

`collect2: ld returned 1 exit status`

I stumble on this occasionally too, but it's not hard to diagnose if you know
much about C and C++ (for some students this is not the case!). Problems like
new being undefined and missing iostreams libraries suggest the linker
doesn't understand C++. Google is not always [helpful][1] in diagnosing these
errors. [Some documentation][2] is equally misleading; I recall a time in the
past where this was true, and the change has been confusing at times.

The [root of the problem][3] is that gcc correctly detects the language type
but does not inform the linker stage of compilation to use the standard C++
library. There are a number of fixes possible. One option is to compile with
gcc -c , and explicitly link at a later stage. This makes sense for large
projects; a Makefile can just compile the changed source and link in the rest
of the previous build for faster build times.

An option more suitable for novices is to use g++ explicitly. **If you're
using .cc files to indicate C++ source code, replace **gcc** with **g++** in
your commands and Makefiles.** Hopefully readers and Google searcher now
understand the problem. And beginning nachOS authors can begin to go on 
writing deadlocks and race conditions while their compiler chain happily 
obeys.

   [1]: http://www.google.com/search?q=%2Ftmp%2Fcc2APvWV.o%3A(.eh_frame%2B0x11)%3A+undefined+reference+to+%60__gxx_personality_v0%27

   [2]: http://www.delorie.com/djgpp/doc/ug/basics/compiling.html

   [3]: http://jldugger.livejournal.com/10965.html?thread=13269#t13269

