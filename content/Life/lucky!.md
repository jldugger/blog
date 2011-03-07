Title: Lucky!
Date: 2010-01-08

[SparkFun][1] held a "Free Day" on Jan 7th, giving away up to 100 dollars in
goods per order (to a max of $100,000). With a bit of planning, an employment
snow day and a lot of luck, I managed to snag one of the spots, and will
recieve an Arduino and stuff. I'm in no hurry to receive it, but it should
make for a nice diversion. Well, _another_ nice diversion; I've already got a
hackable phone, a website, and console games to finish. When the goods do
arrive, I suppose that will be a good time to investigate how easy this is out
of the box with Ubuntu.

Their [postmortem][2] gave a few statistics on the event, but it's not clear
what exactly caused them to slow down so much. Personally, I figure they were
over-subscribed 100:1 and everyone knew it, causing people to flood the site
beyond an overly optimistic worst case scenario (f5 refresh galore!). Not to
mention the extra 75,000 visiters were likely all trying to do purchase
transactions simultaneously, which involves SSL overhead and substantial DB
writes. They didn't post the architecture or individual server stats you'd
need to determine whether it was CPU, IO or network bound. Some bitter parties
accuse them of intentionally crippling the site as a stunt to avoid an anti-
climatic instant sellout. Or that they failed to utilize any caching control
on server or client side.

Anyways, thanks to SparkFun for the toys, I'll be sure to put them to good
use.

   [1]: http://www.sparkfun.com/

   [2]: http://www.sparkfun.com/commerce/news.php?id=322

