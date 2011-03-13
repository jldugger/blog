Title: A comparison of compression schemes
Date: 2008-01-17

## The Scenario

I have about 10GB of SNES games sitting on a storage drive. As I've recently
experienced a scare with my storage disk, I've decided to put as much as I can
on DVDs. Unfortunately, even with Dual Layer DVDs, one can only put about 8GB
on a single disk. Since joda has recently switched to releasing his torrent
packs in 7z form, I've thought I'd try switching my other archives. The
results are amazing.

In a bit more detail, the dataset we're working with is the SNES GoodSet, give
or take a few. The goodset includes nearly every revision of every game known
to the set's editors. So every language, every beta, every bug fix, every
translation and every mod. That's a lot. In fact, the size above is actually
from taking every game and its variants and zipping that group individually.
It's probably twice as big uncompressed.

For testing purposes, I took the first dozen or so groups to create a smaller
test set to work with. I then compressed them with various strategies and
algorithms.

## The compression algorithms

I tested the following compressions where appropriate:

  * .zip

  * .7z

  * .rar

  * .tar.gz

  * .tar.bz2

## The Organization Strategies

### Single Flat Directory, Single file

In this strategy, take all 82 files and place it into a single directory, then
compress the directory. gzip and bz2 don't support this AFAIK, so they were
not tested.

### Grouped Directories, Single file

In this strategy, place all files for a single game into a single directory,
and place all 14 directories into a top level directory to compress. Again,
gzip and bz2 commonly rely on tar to work across multiple files / directories,
so this doesn't really apply.

### Individual Groups compressed

Compress each of the 14 group directories individually. For for gzip and bz2,
tar them first.

### Tarred/Group Tarred

These are two very similar tests with very similar results. Take the
organization strategies from the first two and tar them, then use the
compression. This is motivated by two things. Firstly, it helps put bz2 and
gzip on an even footing with rar/zip/7z. Secondly, as from the 7za man page:

> DO NOT USE the 7-zip format for backup purpose on Linux/Unix because :

>

>   * - 7-zip does not store the owner/group of the file.

>

> On Linux/Unix, in order to backup directories you must use tar :

>

>   * - to backup a directory : tar cf - directory | 7zr a -si
directory.tar.7z

>   * - to restore your backup : 7zr x -so directory.tar.7z | tar xf -

So if you want to automate backup perhaps these tests are a useful insight
into 7zip viability.

### The Data


><td>

Total Size (in MB)

Compression ratio


><td>

117.7

100.00%


><td>


><td>


><td>

_Single Flat Directory, Single file (for supporting formats)_


><td>


><td>

one big zip

62.1

52.76%

one big 7z

50.6

42.99%

one big rar

58.8

49.96%


><td>


><td>


><td>

_Grouped Directories, Single file (for supporting formats)_


><td>


><td>

one big zip

61.2

52.00%

one big 7z

12.2

10.37%

one big rar

58.5

49.70%


><td>


><td>


><td>

_Individual Groups compressed_


><td>


><td>

zipped groups

62.1

52.68%

7zipped groups

10.7

9.09%

tar.gz'd groups

62.1

52.68%

tar.bz2'd groups

65.6

55.23%

rar'd groups

68.5

58.20%


><td>


><td>


><td>

_Tarred_


><td>


><td>

tar.gz

62.1

52.76%

tar.bz2

65.7

55.82%

tar.zip

61.9

52.59%

tar.7z

29.8

25.32%

tar.rar

12.3

10.45%


><td>


><td>


><td>

_Group Tarred_


><td>


><td>

tar.gz

62.1

52.76%

tar.bz2

65.7

55.82%

tar.zip

61.9

52.59%

tar.7z

28.8

24.47%

tar.rar

11.1

9.43%

## Analysis of results

The ultimate victor is 7zip, when compressing each group of related files
separately. RAR does great in the other cases, but surprisingly fares worst
here. Additional information:

  * Clearly, grouping provides 7zip with substantial benefit. It's not hard to
come up with possible reasons: since the games are very much the same with
only fonts and text changed in most cases, it would be simple to define very
large dictionary blocks with very short lines, effectively turning the
dictionary into the main file, and the actual file streams as diffs.

  * This theory also explains why the large single archive fails 7z:
eventually the program decides to limit its dictionary size, causing it to use
smaller words.

  * The individual archives for each group approach theoretically allows one
to cherry pick the best compression for each group, but given how much better
7z is, I doubt any individual groups would actually benefit.

  * In fact, Paul Sladen speculates that [7zip already cherry picks
compression algorithms][1]. He also suggests that order does matter, causing
substantial improvements in backups if you order the tarball by filetype.

## Conclusion

Based on these results, I decided to recompress my 10GB archive with 7z,
leaving the grouping intact. The final size: 3.9GB. Fantastic. And in fact, it
appears that one can do even better, getting [down to 1.6GB][2]. Handy. I just
used the default settings, so perhaps it's time to fiddle with the advanced 7z
settings to compress with. [Addendum: Using smarter options leads to
comparable compression ratios.][3]

   [1]: http://www.paul.sladen.org/projects/compression/

   [2]: http://www.mininova.org/det/1102879

   [3]: //pwnguin.net/addendum.html

