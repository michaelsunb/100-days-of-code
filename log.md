# 100 Days Of Code - Log

### Day 3: January 5, 2017

**Today's Progress**: Restructured code into a MVC structure. Also swapped repositories from [michaelsunb](https://github.com/michaelsunb) to [s3110401](https://github.com/s3110401)

**Thoughts**: The [michaelsunb](https://github.com/michaelsunb) repo let's me create private respositories whereas [s3110401](https://github.com/s3110401) does not. So I moved all my old university projects into [s3110401](https://github.com/s3110401) and any projects not from RMIT University will from now on go to [michaelsunb](https://github.com/michaelsunb). With the MVC structure I hope to have a good separation of concerns. I should in theory be able to swap out MongoDB with say MySQL, or Express-handlebars with Jade.

**Link(s) to work**: [Refactor to a MVC structure](https://github.com/michaelsunb/fb-me-seek-jobs/commit/c639ee01d96c1cf061dfec2c66888aec61c80107) [Instagram #day3](https://www.instagram.com/p/BO4Vb1xBHFJ)


### Day 2: January 4, 2017

**Today's Progress**: Moved port to config, fixed captilisation and made gitignore ignore all files in config/ except for config/default.json.

**Thoughts**: Tested out Facebook messenger [Quick Replies](https://developers.facebook.com/docs/messenger-platform/send-api-reference/quick-replies). Now looking at [List Template](https://developers.facebook.com/docs/messenger-platform/send-api-reference/list-template)

**Link(s) to work**: [Move port from index.js to config files](https://github.com/michaelsunb/seek-fb/commit/ed3b223c14769d0326d2dc0cc2c33a28e1f0a7e3)


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

**Link to work:** [Create facebook messenging logger](https://github.com/michaelsunb/seek-fb/commit/9d646ef9708ef182001bbcff2412f7acb558bed8)
