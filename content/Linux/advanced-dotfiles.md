Title: Advancing the state of the dotfiles repo art
Date: 2018-08-22

Tracking dotfiles with revision control is [old tech][2], with people originally
promoting the practice [using CVS][1]. **Customizing settings is a great productivity
booster**, but trying to remember how you configured `nethack` at your last job is a
huge frustration and time sink. Fortunately humanity has progressed, and at this point
the following can be considered table stakes:

- [git][3]
- [.gitignore][15] files

This can go a long ways, but here's some simple principles I've organized around to
make things rational over time.

## 1: Aggregate small files

Dotfiles [may][7] or [may not][9] be meant to be forked, but done right they can
certainly be shared, studied and adopted. Customizing your settings is a good way
to learn the application deeply and boost productivity. The first time you lose your
configs, the easiest path is to give up and just accept defaults. We use revision
control to retain our precious programs, and thanks to the UNIX 'everything is a file'
philosophy, we can **use standard software engineering practices** to **retain personal
configs.**

Small files make it easy to share snippets, bundle related settings, import outside
changes, and reduce merge conflicts. Well behaved programs **support include
directives**, allowing users to break monolithic configs into small files. So
naturally the challenge is that not all programs support include directives, and not
all that do support globbing. Globbing lets us specify a directory and inclued all
files within. This is the basis for bash-it, oh-my-zsh, and others, but can be
extended more generally than imagined. Three examples:

1. Git
    - supports including specific files, and ~, but not *. Not a deal breaker, but mildly annoying
2. SSH
    - supports includes on [7.3][10] and newer
    - supports globbing via *
3. Bash
    - supports includes, but not globbing
    - still achievable but [more complicated][14] than you'd expect

## 2: Keep it secret

The unspoken risk of publishing dotfiles to a public repo is exposing personal
passwords, private keys, and workplace secrets for all to see and exploit. If you
don't consider privacy at the forefront, you'll pay for it later. The first level of
secrecy is simply using **gitignore to exclude files** and directories from tracking.
You probably already use gitignore to hush editor backups, build artifacts, and log
files, but you can also use it to ignore history files, package caches, and a litany of
common private key file names.

At a secondary level, you can extend this practice using principle #1. In the same way
I have `.bashrc` set up to include all files in `.bash.d/`, I have a script in
`.bash.d/` set up to include all files inside `.bash.d/private/`. Those licence keys in
environment variables, and employer specific shell settings live outside the git repo,
but inside the aggregation system. And if you're so inclined, you can set up
`private/` as its own git repo somewhere more... *private*. Any system of
configuration that provides directives for including other configuration files supports
this method, although if wildcards are not supported you may need another layer of
indirection to avoid disclosing important data through file names.

## 3: multiple repositories

If you write a lot of software, you likely don't use a monolithic repo, and
tracking them all can be tricky. SVN gave us `svn:externals`, which greatly aided in
chaining together repositories and subrepos. In the grand UNIX tradition of doing one
thing well, git does this *other* thing poorly.

Fortunately, [myrepos][4] provides a similar functionality, and improves upon
svn:externals with features like:

- multiple disparate revision control systems
- recursive chains
- custom commands

It also has the benefit of working with the venerable [vcsh][16], which allows you to
mix and match dotfiles repos. For hackers with many hats, this is useful to track
common configurations and role specific settings that may clash or at least not make
sense in a global perspective.

## 4: Multi OS aware

Some of us are cursed to roam the earth across multiple operating systems. You may find
yourself managing Linux servers from a CentOS shell server, writing code on a Mac Book,
and tinkering with Ubuntu at home. In the face of **wildly different interpreter
versions, package managers and kernels, use [`env`][5]** to make things robust. You
may be familiar with it's primary feature of printing out environment variables, but
it has a second purpose: executing scripts with a given interpereter.

It's pretty simple to set up. Instead of hardcoding an interpreter path like with
`#!/bin/bash`, you should use `#!/usr/bin/env bash`, which will utilize PATH to find
the appropriate interpreter. Now **no matter where your preferred interpreter is
installed, it will run as normal**. `env` is basically guarenteed to be omnipresent, so
you can use those 'modern' bash 4 features regardless of how old the shipping OS
interpreter is.

Still, you may encounter from time to time platforms that need specific special casing
for your needs. When you can't find a solution using tools common to your platforms,
you can **special case using `uname`**; Linux platforms return 'Linux', while macOS
returns 'Darwin' for your scripting needs. If you happen to be running bash scripts on
Windows Subsystem for Linux, it also reports 'Linux', but maybe it's clean enough to
keep the illusion up for your scripts.

## 5: Testing

Shell settings in particular are a toxic combination of Turing completeness and obscure
edge cases. And once your shell breaks, it can be painful to fix. As your repo
grows, **[shellcheck][11] can help catch bugs** before they bite you. You'll learn far
more about shell scripting in the process than you bargained for. After scouring a
number of dotfile repos, I found a `test.sh` that runs shellcheck against all bash
scripts it finds and adopted that alongside Travis.

For actual testing, most scripting styles don't support the typical unit testing via
function calls. Fortunately [TAP][12] provides a method for black box testing, and
[BATS][13]. I honestly haven't used it much, but it's on the todo list now I guess.

### Wrap-up

These are my organizing principles. You're free to use them, or ignore them, but
hopefully it explaining it here makes my [own dotfiles repo][17] more nagivable.

   [1]: https://joeyh.name/cvshome/

   [2]: https://joeyh.name/svnhome/

   [3]: https://git-scm.com/book/en/v2

   [4]: https://myrepos.branchable.com/

   [5]: https://linux.die.net/man/1/env

   [6]: https://carlosbecker.com/posts/dotfiles-are-meant-to-be-forked/

   [7]: https://zachholman.com/2010/08/dotfiles-are-meant-to-be-forked/

   [8]: https://github.com/bats-core/bats-core

   [9]: https://www.anishathalye.com/2014/08/03/managing-your-dotfiles/

   [10]: https://www.openssh.com/txt/release-7.3

   [11]: https://www.shellcheck.net/

   [12]: https://testanything.org/

   [13]: https://github.com/bats-core/bats-core

   [14]: https://github.com/jldugger/dotfiles/blob/master/.bashrc#L59-L65

   [15]: https://www.youtube.com/watch?v=0WfDe51pUU0

   [16]: https://github.com/RichiH/vcsh

   [17]: https://github.com/jldugger/dotfiles/