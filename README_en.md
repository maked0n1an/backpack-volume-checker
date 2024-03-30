<h1 align="center">Backpack Volume Checker<h1>

The README in Russian can be found here: [README.md](https://github.com/maked0n1an/backpack-volume-checker/blob/main/README.md).

## 🔗 Links
🔔 Channel: 
[![Telegram channel](https://img.shields.io/endpoint?url=https://runkit.io/damiankrawczyk/telegram-badge/branches/master?url=https://t.me/crypto_maked0n1an)](https://t.me/crypto_maked0n1an)

<h2>Description</h2>

The bot is created to check the volume in [Backpack](https://backpack.exchange/refer/maked0n1an)
All data from the console is written to 'user_data/logs/main.log'. The code is executed asynchronously, the data matches 100% with the site.

For work you need to insert:
- cookies in 'input_data/cookies'; 
- proxies in 'input_data/proxies.txt'; 
- account names in 'input_data/account_names.txt' (optionally, read 'input_data/config.py')

Fork from the author: https://github.com/3asyPe/backpack-volume-checker

How to get a cookie?
1. Log in to each project account;
2. Press F12;
3. Go to the 'Network' tab any file that will .
3. Click the 'Fetch/XHR' filter just below;
4. Take any file that will have an orange sign and no extension (like the 'user' or 'capital' or 'assets' file).
5. In Request Headers, find the header/section called 'Cookie' and copy its value completely
6. Paste into 'input_data/cookies', one cookie is one line

See the screenshot below for more details:

![](https://github.com/maked0n1an/backpack-volume-checker/blob/main/instruction.png)


## Installation and launch
If you don’t have knowledge about installing Python and running it, then go to the section [Links](#links):

* Install libs:
<pre><code>pip install -r requirements.txt</code></pre>
* Go to 'backpack-volume-checker' folder:
<pre><code>cd backpack-volume-checker</code></pre>
* Read 'input_data/settings.py' carefully and set settings you need.
* Launch in terminal:
<pre><code>python main.py</code></pre>

## Donats (EVM):
<pre><code>0x74eEfCAD1Ad18705596106703A3036BaAD6B3145</code></pre>

## Disclaimer and Safety Advice

Any use of this product is at the discretion of the end user. This usage includes, but is not limited to, the areas of virginity loss, financial means, and superstitious practices.
Please note that we are not responsible for lost money resulting from the use of the product. We recommend that you carefully read the product code, perform a full inspection of it, and make sure that data is not transferred or “leaked” during its operation.

## Links
<a name="Links"></a>
- https://t.me/crypto_maked0n1an
- [Guide to auditing software for scams. Python. (RU)](https://teletype.in/@brokeboi/dsxymHafdZb)
- [The ultimate guide to running scripts. Python. (RU)](https://teletype.in/@hodlmod.eth/how-to-run-scripts)