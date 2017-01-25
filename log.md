# 100 Days Of Code - Log

### Day 2: January 25, 2017

**Today's Progress**: Started using bower which led me into gulp

**Thoughts**: Thinking of automating javascript files to public directory

**Link(s) to work**: [Bower](https://bower.io/), [Concatenate & Minify Javascript with Gulp, Improve Site Performance](http://codehangar.io/concatenate-and-minify-javascript-with-gulp/)


### ~~Day 16:~~ Day 1: January 24, 2017

**Today's Progress**: Helped a mate with setting up SSL certificates

**Thoughts**: I really should focus on one thing. Developing good habits.

**Link(s) to work**: [The Node.js Engineer's Guide To Stripe](http://www.scotthasbrouck.com/books/)


### Day 15: January 17, 2017

**Today's Progress**: Extracted express to app.js. And got GunDB to work

**Thoughts**: So I'll have an admin panel that will to help gather data with GunDB, while also having another site to do the same thing.

**Link(s) to work**: [Extract express to app.js](https://github.com/michaelsunb/seek-fb/commit/42f0ab7c1d3ed1a12a653ceb416d367bb55c7d97)


### Day 14: January 16, 2017

**Today's Progress**: Installed express handlebars and GunDB.

**Thoughts**: I might use GunDB to help find jobs.

**Link(s) to work**: [Write Templates Like A Node.js Pro: Handlebars Tutorial](https://webapplog.com/handlebars/), [gun/examples at master · amark/gun](https://github.com/amark/gun/tree/master/examples)


### Day 13: January 15, 2017

**Today's Progress**: Started working on Anki flash cards.

**Thoughts**: I don't know if it should be cosidered as coding.

**Link(s) to work**: [Anki Tutorial](https://www.youtube.com/watch?v=q08x4t7zhcw), [Create Anki Cards Quickly using CSV](https://www.youtube.com/watch?v=BwGNP3GXmxg)


### Day 12: January 14, 2017

**Today's Progress**: Took a break from my personal project to work on some coding questions given to me.

**Thoughts**: I recently watch a YouTube video about extracting and refactoring code. But the presentator argued readability over refactored code and the stages of programmers. I was torn between "easy to read" code and refactored code. I had a peace of code with a lot of "if" statements and it could be refactored into a hash map and made polymorphic. But for the sake of the readability I choose readable code because the refactored code would be a bit hard to read if fresh eyes where to look at it.

**Link(s) to work**: [Straight-line code over functions - FunFunFunction #3](https://www.youtube.com/watch?v=Bks59AaHe1c), [The growth stages of a programmer - FunFunFunction #6](https://www.youtube.com/watch?v=2qYll837a_0)


### Day 11: January 13, 2017

**Today's Progress**: Looked into GunDb

**Thoughts**: GunDB is interesting. Maybe I'll look into implementing it somehow.

**Link(s) to work**: [GunDB](http://gun.js.org/enterprise/)


### Day 10: January 12, 2017

**Today's Progress**: Can now message a user

**Thoughts**: I can now message myself but haven't pushed that part of the code because it contains my Facebook user ID. Plan to use a different server with PHP5.4 to grab the information needed to send to a Facebook user

**Link(s) to work**: [Start creating message model](https://github.com/michaelsunb/seek-fb/commit/d8293ffe7831a8a71b1b40d934168253546d425a), [messenger-bot-tutorial](https://github.com/jw84/messenger-bot-tutorial/blob/master/index.js#L57)


### Day 9: January 11, 2017

**Today's Progress**: Refactored code and created helpers

**Thoughts**: Going not as fast as I would like it to be. Looked into messaging backt to the user.

**Link(s) to work**: [Refactor code and create helpers](https://github.com/michaelsunb/seek-fb/commit/c05162d6ffc29942edbb5e7bce2e3cae9211226f)


### Day 8: January 10, 2017

**Today's Progress**: Created development server with VirtualBox

**Thoughts**: Didn't do any coding but I finally created my own development server using VirtualBox. Yay :)

**Link(s) to work**: [Set virtualbox network for Ubuntu 16.04 client](https://superuser.com/questions/1080675/set-virtualbox-network-for-ubuntu-16-04-client), [Ubuntu Server 16.04 LTS Install & VirtualBox Guest Additions](https://www.youtube.com/watch?v=9kiY_uyWQhM), [How to Share Folders in Ubuntu Guest with Windows 7 Host using VirtualBox](https://www.youtube.com/watch?v=I5cV0V7vLJw), [Installing VirtualBox Guest Additions on Ubuntu Server](http://en.ig.ma/notebook/2012/virtualbox-guest-additions-on-ubuntu-server), [How to install VirtualBox Guest Additions for Ubuntu 16.04](https://askubuntu.com/questions/792832/how-to-install-virtualbox-guest-additions-for-ubuntu-16-04)


### Day 7: January 9, 2017

**Today's Progress**: Created tests for webhook route

**Thoughts**: Make tests because I want to stop relying on testing in the frontend and testing with Facebook.

**Link(s) to work**: [Introduce webhook tests](https://github.com/michaelsunb/seek-fb/commit/0ed1d81904dcdab048d7d8535fa376793a5dcda7), [Code clean up & add test for post to /webhook](https://github.com/michaelsunb/seek-fb/commit/8f16631793954822e592de62683912cc22906449), [Test a Node RESTful API with Mocha and Chai](https://scotch.io/tutorials/test-a-node-restful-api-with-mocha-and-chai)


### Day 6: January 8, 2017

**Today's Progress**: Move model functionality to models

**Thoughts**: Make controllers as thin as possible. Also in theory if we want to just database, all we'd have to do is change the functions in app/models/.

**Link(s) to work**: [Move model functionality to models](https://github.com/michaelsunb/seek-fb/commit/cfebceae6e93d39303e53053fa6ebfbee1df9796)


### Day 5: January 7, 2017

**Today's Progress**: Change Model and controller to only insert a Facebook user ID once.

**Thoughts**: Felt extremely tired. Found the courage to continue on the 100 days code streak so I did what I could do. For tomorrow, I need to develop a Facebook OAuth with [passportjs](http://passportjs.org/docs/facebook) and if I get that done, I will develop a way to send [list templates](https://developers.facebook.com/docs/messenger-platform/send-api-reference/list-template) to users.

**Link(s) to work**: [Message inserts FB user id if does not exist in db](https://github.com/michaelsunb/seek-fb/commit/ef9ffc61c78e570bf06fbc10649a7f1bd583914a), [PassportJS with Facebook](http://passportjs.org/docs/facebook)


### Day 4: January 6, 2017

**Today's Progress**: Reverted repo name and changed index.js to server.js. Looked into sending list in Facebook messenger. Also [rules.md](https://github.com/michaelsunb/100-days-of-code/blob/master/rules.md) has been corrected.

**Thoughts**: Met up with a few friends today so I only managed to get an hours work in. When sending a [List Template](https://developers.facebook.com/docs/messenger-platform/send-api-reference/list-template), any URLs being sent through the message needs to be [domain whitelisted](https://developers.facebook.com/docs/messenger-platform/thread-settings/domain-whitelisting). [Kallaway/100-days-of-code](https://github.com/Kallaway/100-days-of-code) needs to accept multiple [pulls requests](https://github.com/Kallaway/100-days-of-code/pulls) to [update rules.md](https://github.com/Kallaway/100-days-of-code/pull/26)

**Link(s) to work**: [Rename repo and index.js](https://github.com/michaelsunb/seek-fb/commit/7c9005f1116c5991d42eb82e90fc6055cfe6d855), [#7 Fix rules.md markdown typo](https://github.com/Kallaway/100-days-of-code/pull/7), [#20 Update rules.md](https://github.com/Kallaway/100-days-of-code/pull/20), [#26 Update rules.md](https://github.com/Kallaway/100-days-of-code/pull/26)


### Day 3: January 5, 2017

**Today's Progress**: Restructured code into a MVC structure. Also swapped repositories from [michaelsunb](https://github.com/michaelsunb) to [s3110401](https://github.com/s3110401)

**Thoughts**: The [michaelsunb](https://github.com/michaelsunb) repo let's me create private respositories whereas [s3110401](https://github.com/s3110401) does not. So I moved all my old university projects into [s3110401](https://github.com/s3110401) and any projects not from RMIT University will from now on go to [michaelsunb](https://github.com/michaelsunb). With the MVC structure I hope to have a good separation of concerns. I should in theory be able to swap out MongoDB with say MySQL, or Express-handlebars with Jade.

**Link(s) to work**: [Refactor to a MVC structure](https://github.com/michaelsunb/seek-fb/commit/c639ee01d96c1cf061dfec2c66888aec61c80107),  [Instagram #day3](https://www.instagram.com/p/BO4Vb1xBHFJ)


### Day 2: January 4, 2017

**Today's Progress**: Moved port to config, fixed captilisation and made gitignore ignore all files in config/ except for config/default.json.

**Thoughts**: Tested out Facebook messenger [Quick Replies](https://developers.facebook.com/docs/messenger-platform/send-api-reference/quick-replies). Now looking at [List Template](https://developers.facebook.com/docs/messenger-platform/send-api-reference/list-template)

**Link(s) to work**: [Move port from index.js to config files](https://github.com/michaelsunb/seek-fb/commit/7eac06e520e9cc369dc5c15c8fe16679cbe0a719)


### Day 1: January 3, 2017

**Today's Progress**: Created AWS server, bought a SSL certificate, and created a basic fb messenger logging server with nodejs.

**Thoughts**: When showcasing work on [instagram](https://www.instagram.com/p/BOzTY6ohjmR/) hide important details.
* Guides to create SSL
  1. [Add SSL to EC2 Instance](http://iwearshorts.com/blog/add-ssl-to-ec2-instance/)
  2. [Tutorial: Configure Apache Web Server on Amazon Linux to use SSL/TLS - Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/SSL-on-an-instance.html)
* Guides for moving MongoDB to EBS
  1. [Running MySQL on Amazon EC2 with EBS (Elastic Block Store)](https://aws.amazon.com/articles/1663)
  2. [Install MongoDB on Amazon EC2](https://mongodb-documentation.readthedocs.io/en/latest/ecosystem/tutorial/install-mongodb-on-amazon-ec2.html)
* Guides to create basic fb messenger bot
  1. [Quick Start - Messenger Platform - Documentation - Facebook for Developers](https://developers.facebook.com/docs/messenger-platform/guides/quick-start)
  2. [Pair Programming a Facebook Messenger Bot - FunFunFunction #28](https://www.youtube.com/watch?v=zFO1cRr5-qY)

**Link to work:** [Create facebook messenging logger](https://github.com/michaelsunb/seek-fb/commit/aaffbef0d6d50855631296a51b42708753e4fa88)
