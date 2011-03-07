Title: Chromium Build Instructions?
Date: 2008-09-02

I have located the [Linux build instructions][1] for Chromium, what you might
know as Google Chrome.

Interesting notes thus far:

  * Instructions include a reference to "Ubuntu 8" for retrieving build
dependencies ;)

  * an SVN checkout that retrieves ANOTHER set of source code management tools
not in wide use

  * uses bison for grammars; I've become a big fan of ANTLR for describing a
grammar

  * "BSD licensed," so it should be license compatible with Mozilla (and IE
and opera)

  * checkout of source code takes 16 minutes to grab 666MB and crashes:

> Traceback (most recent call last):

>File "home/jldugger/Desktop/chromium/depot_tools/release/gclient.py", line
925, in  result = Main(sys.argv)

>File "home/jldugger/Desktop/chromium/depot_tools/release/gclient.py", line
921, in Main return DispatchCommand(command, options, args)

>File "home/jldugger/Desktop/chromium/depot_tools/release/gclient.py", line
885, in DispatchCommand return command_map[command](options, args)

>File "home/jldugger/Desktop/chromium/depot_tools/release/gclient.py", line
837, in DoUpdate return update_all(client, options, args)

>File "home/jldugger/Desktop/chromium/depot_tools/release/gclient.py", line
713, in UpdateAll deps = get_all_deps(client, entries)

>File "home/jldugger/Desktop/chromium/depot_tools/release/gclient.py", line
576, in GetAllDeps solution_deps = get_default_solution_deps(client,
solution["name"])

>File "home/jldugger/Desktop/chromium/depot_tools/release/gclient.py", line
537, in GetDefaultSolutionDeps deps = scope["deps"] KeyError: 'deps'

  * **Once built, Chromium will do nothing of value to Linux users today.**

Currently, I'm downloading their tarball, hoping that it works better than the
checkout instructions did.

   [1]: http://dev.chromium.org/developers/how-tos/build-instructions-linux

