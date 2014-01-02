BidManager
==========

A Django based project for managing bids and rfp's

Requirements
------------
* Python 2.6+
* Whoosh + haystack for search engine
* See requirements.txt for virtualenv packages

Project Structure
-----------------
### Front End Web Application ###
Django app that end users and system admins interact with to manage bids

### Back End Crawling Engine ###
Sample crawling engines to pull bids in from external site.
Crawling kicked off via mgmt command `manage.py crawl`

### Sample sites ###
Sample sites to crawl against

ToDos
------
* User alerts (paid service) - sign up for alerts on search
* Swappable pay plans (for possible changeing over time)
** Cheaper yearly vs month to month, M 6M Y signups
