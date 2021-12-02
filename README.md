# Commerce design document

An eBay-like e-commerce auction site where users can create listings and bid on other listings. A listing can  be created by providing a title, description, starting bid and optional image. Users can add listings to their own watchlist and win auctions by having the highest bid when the auction is closed. To participate in bidding and creating auctions a user can register an account and log in.


## Impression of homepage

View of homepage when user is logged in. The user can take the following routes:
* register --> register.html -- submit --> index.html(logged in)
* login --> login.html --> submit --> index.html(logged in)

![logged in](images/logged.jpg?raw=true "logged in")

View of homepage when user is logged out. The user can take the following routes:
* log out --> index.html(logged out)
* wishlist --> wishlist.html
* Active listings --> active_listing.html
* create listing --> create_listing.html
* Listing # --> listing.html

![logged out](images/not_logged.jpg?raw=true "logged out")
## html pages

* index.html
* login.html
* register.html
* listing.html
* create_listing.html
* wishlist.html
* active_listings.html
## UML class diagram

This diagram shows the relations between django models

![UML diagram](images/UML_class_diagram.jpg?raw=true "UML diagram")
