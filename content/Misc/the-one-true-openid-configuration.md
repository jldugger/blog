Title: The One True OpenID configuration
Date: 2010-08-10

I like the OpenID concept, but by now it's clear that there's far more Issuing
Parties than Relying Parties. In layman's terms, there's more sites that want
you to use your account with them on other sites than sites that let use an
account from elsewhere. Which defeats the whole point in dramatic fashion.
[The Password Thicket: Technical and Market Failures in Human Authentication
on the Web][1] [[via][2] Bruce Schneier] examines the marketplace and offers
the following conclusion:

> In the meantime, this perspective supports the claim [[15][3]] that
deployment of an open, federated identity protocol such as OpenID will be
opposed by current stakeholders on the web. Federated login not only removes
sites’ pretext for collecting personal data but their ability to establish a
trusted relationship with users.

This is only the most recent accusation, as the citation indicates. And
there's plenty of economic incentive to refuse OpenID; you'll have no pretext
for asking for email addresses or Favorite Movie 'security questions' that
will help you sell targeted advertising. But there's another reason OpenID is
struggling in the marketplace that isn't mentioned: OpenID is **hard** for
users to deploy correctly. There is One True Way to configure your OpenID
safely, which I will document for myself and posterity:

  1. Buy a domain name. This domain is your openID.

  2. Find some hosting for this domain. Preferably with exclusive access so
only you can modify it.

  3. Purchase and install an SSL certificate for your domain.

  4. Locate or install an authentication system that supports OpenID

  5. On the page accessible on your domain, place an OpenID delegate relation
link to that authentication system.

  6. Make sure both your OpenID URL and the delegate use HTTPS and are
invulnerable to the cornucopia of web attacks.

  7. Cry as you realize that few of the OpenID providers you could have
delegated to will accept your OpenID.

Skip any of these steps and there is a world of pain waiting for you. And
there's plenty of smart people who [miss important points][4]. If you don't
buy a domain and just use a site like LiveJournal or Gmail directly, you're at
the mercy of your provider's implementation and longevity. If you need a real
example, provider Vidoop [gave people a real scare][5].

Reviewing the steps above, it's obvious why Verisign was an early partner with
OpenID; they had a lot to gain up until their expert jumped ship for Facebook.

   [1]: http://weis2010.econinfosec.org/papers/session3/weis2010_bonneau.pdf

   [2]: http://www.schneier.com/blog/archives/2010/07/website_passwor_1.html

   [3]: http://techcrunch.com/2008/03/24/is-openid-being-exploited-by-the-big-internet-companies/

   [4]: http://www.reddit.com/r/programming/comments/vder/how_to_actually_use_openid/cvgdn

   [5]: http://factoryjoe.com/blog/2009/06/05/the-fall-of-vidoop/

