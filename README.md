# Browsmos for Reinforcement Learning

The game should send status information via WebSockets to a Python client and shall receive the player's commands, i.e. (re)start game and click somewhere.

How to use:
1. `pip3 install --user websockets asyncio`
2. `python3 python/client.py`
3. in another terminal: `python3 -m http.server`
4. Open http://localhost:8000 in your web browser

You should see status information like cell location, and win/lose in the output of `python3 python/client.py`.

# Browsmos Original README

## Play

http://stepheneisenhauer.com/demos/browsmos/

## About

Browsmos is a game the web browser, made entirely using HTML5, and inspired 
heavily by the gameplay of Osmos.

The rules are simple; click to propel yourself around, and try to absorb 
smaller cells until you become the biggest. Watch out for larger cells, or 
they will absorb you!

## Install

Browsmos can also be installed as an app in Chromium or Google Chrome, 
requiring no internet connectivity to play. It can be installed via the 
Chrome Web Store here:

[![Available in the Chrome Web Store](https://developer.chrome.com/webstore/images/ChromeWebStore_Badge_v2_206x58.png)](https://chrome.google.com/webstore/detail/browsmos/kmijdbjgikpiadlbldnmldfgfepigkip)

## Screenshots

![Screenshot 1](http://stepheneisenhauer.com/images/screenshots/browsmos.png)

## Other Links

* Homepage: http://stepheneisenhauer.com/browsmos/

## License

Any JavaScript sources within Browsmos are hereby licensed under the 
Simplified BSD License. You are free to modify and redistribute Browsmos, 
but, if you do, please:

* don't distribute modifications as though they are my own
* consider including an attribution, preferably linking to this page
