Title: SQLite + SchemaSpy
Date: 2011-01-23

A little over a year ago, I shared a neat technique to generate [DB diagrams
for databases,][1] with a focus on SQLite. At the time, SchemaSpy had much
better output but didn't have a good SQLite driver. Well, a recent commenter
asked if it was possible, and fortunately, that's recently changed. It's not
as easy as possible but it's at least more possible than before.

### Prep

First, you'll need some compilers. Easy on Ubuntu: apt-get install
openjdk-6-jdk gcc.

Second you'll need to download development headers for SQLite. Again, on
Ubuntu apt-get install libsqlite3-dev.

Next, download the [javasqlite.tar.gz][2] from Christian Werner. This package,
when built, will provide a a Java native interface to access SQLite databases
with. It's a straight forward build assuming you've got all the dependencies.
I'm not clear on where to install this so java finds it or how to best set up
env vars to where SchemaSpy needs less help; I'm sure it's possible though.

Finally, download the [latest SchemaSpy jar][3].

### Usage

The invocation is a little bit confusing. LD_LIBRARY_PATH seems required for
the JNI to work. The -dp is required for SchemaSpy to find the drivers.
There's probably a directory it could be installed to instead. -nowrows turns
off row counts, and -hq turns on high quality Graphviz output. I used the
following command line to diagram Banshee's database (YMMV):

> LD_LIBRARY_PATH=/usr/local/lib java -jar ~/tmp/schemaSpy_5.0.0.jar -t sqlite
-db ~/.config/banshee-1/banshee.db -o banshee -sso -dp
~/src/javasqlite-20110106/sqlite.jar -hq -norows

The diagram output:

[![][4]][5]

There's more to the output than just a diagram, like a clickmap to browse
individual table definitions, and warnings about ["Columns that are flagged as
both 'nullable' and 'must be unique'".][6]

### Issues

The SQLite driver isn't perfectly matched, and there's a number of warnings
generated. Firstly, there's rarely any documented key constraints, so
SchemaSpy has to infer relationships based on field and table names, and does
so poorly at times. Secondly, it fails to collect row counts, and gives you -1
instead if you ask it to try. Finally, it fails to determine autoincrement
status. Really, we should be thankful it works as well as it does, given the
SQLite design philosophy.

Well, hopefully you'll find a lot of opaque embedded databases just got a bit
easier to comprehend!

   [1]: //pwnguin.net/generating-database-schema-with-sql-and-graphviz.html

   [2]: http://www.ch-werner.de/javasqlite/

   [3]: http://sourceforge.net/projects/schemaspy/files/

   [4]: //pwnguin.net/media/photologue/photos/cache/relationships_implied_compact_display.png

   [5]: //pwnguin.net/albums/photologue/photo/banshee-db-schema/

   [6]: http://www.sqlite.org/faq.html#q26

