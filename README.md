# What is this tool ?

With this tool you can be notified when new item will be inserted in [Subito.it](https://www.subito.it/)



# Usage

Two type of notification:
1. Email. Insert in ```email.txt``` your Outlook email and password.
2. Telegram. Insert in ```telegram.txt``` your token and chatid

You can use both.
Test if the credentials are correct with your setup using option "--test": ```python main.py --price 200,400 --link https://www.subito.it/annunci-italia/vendita/informatica/?q=computer --timeout 5 --test```


Example: ```python main.py --price 200,400 --link https://www.subito.it/annunci-italia/vendita/informatica/?q=computer --timeout 5```

Where:
* --price, set the minimum and maximum price to search.

* --link, set the url to create the request. Don't insert all the link from Subito.it, only the "prefix" until '&'. If the link is ```https://www.subito.it/annunci-italia/vendita/informatica/?q=computer&qso=true&shp=true&order=datedesc&ps=200&pe=500``` you need to insert ```https://www.subito.it/annunci-italia/vendita/informatica/?q=computer```.

* --timeout, set the timeout between searches, in minutes.


