# 100 Days Of Code - Log

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
