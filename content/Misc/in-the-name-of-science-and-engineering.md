Title: In the name of science and engineering
Date: 2008-12-17

In the [inaugurial post][1] in Aaron Toponce's series on compression, two
critical errors are made and highlighted by a [comment to his post][2]:

> "I wanted to see speed, and I figured what could be faster than a bunch of
identical data? I was way wrong."

Aaron, you say you wanted to see speed, but didn't tell the programs that.
Instead you asked for maximal compression. It should come as no surprise that
-1 through -9 are not calibrated among compression tools. -9 means "I don't
care how much the CPU costs over -8, find me those extra bytes." You really
shouldn't be surprised when an algorithm can take gobs of time **when asked to
do so**.

Your other mistake is about datasets. Lossless compression on completely
random data is held to be impossible; certainly the developers of bzip2, gzip
and lzma aren't after that goal. Each of these algorithms is designed to work
on some datasets better than others. We shouldn't expect the [Burrows-Wheeler
transform][3] to be a worthwhile investment on megabytes of zeros, for example
(though I still have a hard time believing it works _at all, on anything_).

In fact, the bzip2 implementation may be saved by what the [bzip2 author calls
a mistake][4]:

> The run-length encoder, which is the first of the compression
transformations, is entirely irrelevant. The original purpose was to protect
the sorting algorithm from the very worst case input: _a string of repeated
symbols_. But algorithm steps Q6a and Q6b in the original [Burrows-Wheeler
technical report (SRC-124)][5] show how repeats can be handled without
difficulty in block sorting.

(emphasis and link mine)

Still, I applaud your efforts to investigate and document, even if I think
conclusions should be withheld pending further investigation. It's likely my
own investigation was flawed in some way, but I don't think it's worth peer
review at this point: [GoodMerge][6] publishes it's [own findings][7].

It might be informative to:

  1. Publish your datasets. This may involve changing them slightly for
privacy and copyright ;)

  2. Graph the relationship between CPU time, compression ratio and -# option,
to illustrate the size of tradeoffs available.

   [1]: http://pthree.org/2008/12/14/lzma/

   [2]: http://pthree.org/2008/12/14/lzma/#comment-109012

   [3]: http://en.wikipedia.org/wiki/Burrows-Wheeler_transform

   [4]: http://www.bzip.org/1.0.3/html/misc.html

   [5]: http://www.cl.cam.ac.uk/teaching/2001/DSAlgs/SRC-124.pdf

   [6]: http://goodmerge.sourceforge.net/About.php

   [7]: http://goodmerge.sourceforge.net/Statistics.php

