Title: Blog Stack
Date: 2016-10-04 19:00
Category: Eitan Posts

How to set up a static generated blog in literally 10 minutes.  


1. Get an account at *www.digitalocean.com* and get a minimal VPS for 5 dollars a month.
2. Get a domain at *www.namecheap.com* for 5 dollars a year.
3. Install *python 3* because you're not an asshole who keeps the python 2 ecosystem alive.
4. Install *virtualenv* and *virtualenvwrapper*, because you're not a barbarian. This isn't Java, we have easy to manage virtual environments.
5. Install *pip3* because come on. Maven? Get real, guys.
6. *pip install pelican*
7. Fumble around with *ufw* firewall rules until you somehow, by sheer luck and magic, get port 8000 open. Do it again for port 80.
8. Google for how to forward traffic from 80 to 8000. We're using the test server packaged with pelican, we don't have time for anything else.
9. You want an awesome theme for your blog. So steal the most minimal, sleekest one wholesale from the themes repository, and drop it into your blog directory so you can inevitably change something you weren't supposed to touch later, thus breaking the blog. Don't worry, a reinstall takes 10 minutes.
10. Just make up some posts. Honestly, I could write them all in advance, and no one would know any better.
11. Generate the blog content and host it.
12. Shit, we forgot to run in a screen window.
13. Re-run in a screen session.
14. Google those stupid screen shortcuts. Control + a, d...
15. Serve the blog out of the wrong content directory
16. Kill the process
17. Serve the blog out of the correct content directory
18. Wait 20 minutes for the domain to properly register and forward the traffic.