# Epic_checker
This tracker is designed specifically for the following site- https://www.shopblt.com/cgi-bin/shop/shop.cgi?action=thispage&thispage=011003000505_B2KQ135P.shtml&order_id=272896820&sitem=B2KQ135#Availability 

The tracker mainly utilizes Beautifulsoup4, Websessions, and requests. 

The main driver behind the tracker is the "Web-sessions" which opens a headless Mozilla Browser and accesses the site. The reason for electing to have it be a websession as opposed to a standard request is due to the security of Cloudflare, as cloudflare has native detection for normal requests made from Python, and other basics of network accesability in code. To address this, we needed to have the script "appear" as a normal user. 
To that end we used "web-session" to open up a headless Mozilla browser, and attempt to access the site, doing it this way is affectively not all to disimiliar to how a normal user would access the site, but this method isn't fool proof, as it can still be caught if using specific versions of Mozilla, Chrome, ETC. But in our research we found a specific version of Mozilla wasn't being cauight by cloudflare, and managed to workaround the issue. 

Initially we used selenium, as this would have been prfered over a generic websession, but all attempts at using selenium against the site lead to an instant block by cloudflare. as such we then determined to stick to websession as that provided a solution to the problem. HOWEVER, it is worth noting that this may be a temp solution, as I do not believe the specific version of mozilla will remain unblocked forever, and this solution may become useless should cloudflare find a way or decide to outright block this method. 

Once the headless browser opens, it then perform the requests against the URLs

We have 4 different URLs that were stored in "shoplist.yaml" the script will go, and reach out to each URL to pull the following information 
Availability
Backorder
Total incoming
ETA

From there it wraps the info into a JSON request and posts it to the specified discord URL, where the script then sleeps for a random amount of time, between 30 to 60 mins. 

The reason it is random so it can be harder to detect that a script is targetting the site, and so it looks more like a person is checking it. (however it wouldn't be hard to spot the pattern as it's doing it every 30-60 mins, and it's going at a consistent basis throughout the night, meaning all someone would need to do is see "Hey this thing checks every half hour to an hour. Let's block it." ideally it would be a wider range of random, so most likely every 1-6 hours, so as to appear much more like a real person. but given the rapid updates of the site, it needed to be every 30-60 mins so as to be ahead on updates.)

TO DO IN FUTURE: 
- Add change detection: We would prefer to have it only post updates if there are any changes, initially we wanted to have it do that right from the get-go but this resulted in the site not giving us back correct information, or the web-session it self, terminating, we intially troubleshooted the issue, but couldn't quite pindown why this was occuring, but given that the site was not blocking us when the script ran for a week+, this was put onto a future to do list. 
- Redo code: I would prefer if this code could be more flexible so it could be used for othger sites, where we could potentially point it to other sites and yank information from it, HOWEVER the issue there is every site is different, uses different methods of storing data, and is all structed differently, NOT to mention the differences in security, monitoring, ETC. so this idea is most likely a dead-on-arrival type of idea, but still an ambition I would like to persue in future. However what I could do is make it more "boiler-plate" and to that end make it more of a template that can be pulled, and editted to fit the situation we require it for, this would be the more realistic approach, as opposed to a "One size fits all" approach.
