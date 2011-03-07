Title: I wholeheartedly agree
Date: 2009-03-02

Colin puts together a coherent rant about [bug triage with Ubuntu.][1] I'm
glad he was able to meditate on the subject and produce a document with
clarity and specific improvements; I wrote a private rant that included the
phrase "Bug Assassination Squad: We kill bugs in their infancy". Probably not
diplomatic enough to publish.

More diplomatically, one thing I'd like to add to Colin's commentary is about
**bug duplicates**. Some people seem to be in the habit of marking duplicate
bugs invalid. Yes, there are a lot of bugs, so going to the effort of finding
the dupe and marking it means you'll be slower at closing bugs. But you'll
have a better bug database as a result. And it will spare me the effort of
searching through all the package's bugs to discover there is no such
duplicate. Certainly, if you believe there's a duplicate report, you have a
better idea of where the dupe is than the person who submitted the bug, who
went through LP's own dupefinder to report the bug in the first place.

While I do feel vindicated that this practice is contrary to [guidelines][2],
the fact that it [still happens][3] is not encouraging.

   [1]: http://www.chiark.greenend.org.uk/ucgi/~cjwatson/blosxom/2009/03/02#2009-02-27-bug-triage-rants

   [2]: https://wiki.ubuntu.com/Bugs/HowToTriage/#Duplicates

   [3]: https://bugs.launchpad.net/ubuntu/+bugs?field.searchtext=Thanks+for+the+bug+report.+This+particular+bug+has+already+been+reported+into+our+bug+tracking+system%2C+but+please+feel+free+to+report+any+further+bugs+you+find.&orderby=-datecreated&field.status%3Alist=NEW&field.status%3Alist=INCOMPLETE_WITH_RESPONSE&field.status%3Alist=INCOMPLETE_WITHOUT_RESPONSE&field.status%3Alist=INVALID&field.status%3Alist=WONTFIX&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=FIXRELEASED&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_supervisor=&field.bug_commenter=&field.subscriber=&field.component-empty-marker=1&field.status_upstream-empty-marker=1&field.omit_dupes.used=&field.omit_dupes=on&field.has_patch.used=&field.has_cve.used=&field.tag=&field.tags_combinator=ANY&field.has_no_package.used=&search=Search

