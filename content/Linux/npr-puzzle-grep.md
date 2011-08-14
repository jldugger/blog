Title: Solving the Sunday Puzzle with coreutils
Date: 2011-05-16

Not too long ago, a puzzler admitted to solving the NPR Sunday Puzzle with a
computer. Since I hate word puzzles quite a bit, I'd taken similar steps in the
past. For example, this recent challenge: 

Fill in the 4x4 square crossword with common uncapitalized words, using no 
letter more than once:
NAGS
E
W
T

My secret weapon? [GNU coreutils][1]. Regex are a great tool, but I rarely have
to use some of the more obscure features, which hurts on the occasions where
they're called for. So the NPR puzzle can be a good way to practice and learn!

1. I'm using the American English dictionary provided by Ubuntu 
`/usr/share/dict/words`. The format of this file is one word per line. Every 
form of a word, including contractions and possessives, gets its own line. We 
use `|` (pipe) to chain the output of one command as the input of the next. 
Cat simply outputs a file, and wc -l counts the lines in it.

    laptop:~$ cat /usr/share/dict/words | wc -l
    98569

2. I assume no apostrophes are in the puzzle. Grep reads input and outputs only
those lines that match a regular expression (regex).  Using the -v option to 
grep changes it to output only lines that don't match our pattern.

    laptop:~$ cat /usr/share/dict/words | grep -v "'" | wc -l
    74059

3. That's a lot of words to fuddle around with, so lets winnow this down. 
Firstly, we only care about 4 letter words. We can use grep to give us only 
these words, using the regular expression "^....$". Caret (^) represents 
the start of a line, and $ represents the end of one. Each period is a single 
free choice character for grep, matching exactly one character in the input. 


    laptop:~$ cat /usr/share/dict/words | grep -v "'" | grep "^....$" | wc -l
    3174

4. Having cut the search space by 96 percent, we now turn to the clues for... 
clues. Fortunately, nags and newts define which letters every word can start 
with. Grep treats symbols within [] as alternatives, meaning any any one 
symbol within can match the input. Below alters the regex from 3 to only match 
words starting with a, g, s, e, w or t.

    laptop:~$ cat /usr/share/dict/words | grep -v "'" | grep "^[agsewt]...$" | wc -l
    777

5. Rules say no two letters repeat in the puzzle, so we'll exclude all words 
with the letters from nags and newts anywhere other than the first letter. As 
an alternative to -v, we can use carets inside brackets to indicate "not". 

    laptop:~$ cat /usr/share/dict/words | grep -v "'" | grep "^[agsewt][^nagsewt][^nagsewt][^nagsewt]$" | wc -l
    131

6. Next, we can rule out words with repeated letters, like solo and wool. To do
this quickly, we'll need to use [backreferences][2]. Backreferences can be 
[slow][3], but since our dataset is so tiny, it will be fine to add it to the
end of the pipeline.

    cat /usr/share/dict/words | grep -v "'" | grep "^[agsewt][^nagsewt][^nagsewt][^nagsewt]$" | grep -vE "([a-z]).*(\1)" | wc -l
    106

7. Starting to get close! From here on out, this plays a lot like sudoku. Our 
goal is now to start constructing regex for each word. We replace the leading 
alternative for a specific letter. To start off, we've only got 7 options for 2
across:

    laptop:~$ cat /usr/share/dict/words | grep -v "'" | grep "^e[^nagsewt][^nagsewt][^nagsewt]$" | grep -vE "([a-z]).*(\1)"
    echo
    ecru
    emir
    epic
    euro
    evil
    expo

We now write a different regex without negations to get the same list. 
    laptop:~$ cat /usr/share/dict/words | grep "^e[cmpuvx][hipr][cloru]$" | grep -vE "([a-z]).*(\1)" | wc -l
    7

Now we build a similar regex for 2 down. Adding in what we know about it's 
intersection with 2 across (cmpuvx) is the sudoku like step:
    laptop:~$ cat /usr/share/dict/words | grep -v "'" | grep "^a[cmpuvx][^nagsewt][^nagsewt]$" | grep -vE "([a-z]).*(\1)"
    achy
    acid
    amid
    amok
    avid

We rewrite this one as 

    laptop:~$ cat /usr/share/dict/words | grep -v "'" | grep "^a[cmv][hio][dky]$" | grep -vE "([a-z]).*(\1)" | wc -l
    5

Applying the same logic to 3 down yields "^g[ir][lriu][bdlmp]$", and 4 down 
yields "^s[lu][cilmoru][bdfhkmopr]$". 

8. The last positions in each down regex constructs a new regex for 4 across:

    cat /usr/share/dict/words | grep -v "'" | grep "^t[dky][bdlmp][bdfhkmopr]$" | grep -vE "([a-z]).*(\1)"
    typo

A unique solution to 4 across!

9. Revisiting 2 down with this new fact also yields a unique answer. I leave
it from here as an exercise to the reader to solve the entire puzzle.

   [1]: http://www.gnu.org/s/coreutils/
   [2]: http://www.regular-expressions.info/brackets.html
   [3]: http://swtch.com/~rsc/regexp/regexp1.html
