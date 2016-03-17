Title: Rule Zero of FinOpsDev
Date: 2016-03-16

I'm working on a personal finance project codenamed FinOpsDev (rebranding 
suggestions welcome), aiming to reduce drudgery to near zero with automation, 
and exploit the increased velocity to run automated tasks more often, etc. Like
DevOps for your checkbook. Or like Continous Accounting.

As a base, I'm using GNUCash backed by PostgreSQL. GNUCash provides the 
accounting principles and accounting concepts, and have used it for years.
Postgres makes the data available in a central location, with well understood
tools.

I'm not ready to announce any useful tools as a result of my tinkering quite 
yet. Instead, I want to reflect upon an old quote:

> To err is human; to really foul things up requires a computer.

Up till now I've been using those tools in a manual process, so it naturally
happens that my first foray ends up removing all data from the database.
Forcing a restore from a backup I made from last year. From this calamity,
a principle is born: no matter what the first financial automation to start
with, the zeroth should be backups. I still don't know how it happened,
which only underlines the importance of rule zero.

To commemorate the year of transactions I'm rebuilding, here's a clever little
logrotate script I found that gets the job done without any additional
dependencies:

    /var/backups/postgresql/postgresql-dump.sql {
            daily
            nomissingok
            rotate 30
            compress
            delaycompress
            ifempty
            create 640 postgres postgres
            dateext
            postrotate
                    /usr/bin/sudo -u postgres /usr/bin/pg_dumpall --clean > /var/backups/postgresql/postgresql-dump.sql
            endscript
    }

Obviously tools like barman and pg_backrest are great, but I like having a
quick, simple solution in place. Next on the plate is a cron job to exfiltrate
backups to another server for safe keeping.
