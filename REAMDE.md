# Goggle sport scraping

Scrapt data to get result of rugby game

## Getting started

- Clone repo
- Create venv environment \
    Linux
    ```Bash
    python3 -m venv env
    source env/bin/activate
    ```

    Windows
    ```Bash
    python3 -m venv env
    env\Scripts\activate
    ```

- Install dependencies 
    ```
    pip install -r requirements.txt
    ```

- Add .env file at root (ask for the file at someone who have it)



pip freeze > requirements.txt

I am webscraping google page after a search. I want to use python, selenium and bs4. Currently, I would like to do the search and show the webpage that I receive. However, I have the following error selenium.common.exceptions.WebDriverException: Message: Process unexpectedly closed with status 127 when webdriver.Firefox(). Can you solve it or tell me how to use another headless broswer like chrome ? I have linux manjaro.





I am doing webscraping with selecium and beautifulsoup. I have multiple element like this one. For each element, extract both team and their logo, the score for each team if it exist, the date of the game and the link of the vidéo if it exist.


<table class="KAIX8d"><tbody><tr class="S6bEgc"><td class="lc"></td><td></td><td class="imspo_mt__rg"></td><td class="h8T7ab"></td><td class="imspo_mt__sc"></td><td class="G6pHwb" style="width:0px"></td></tr><tr><td class="BAX2sc jelnITEVbpQ__rugby-league-status" colspan="6"></td></tr><tr><td colspan="3"></td><td class="kwbMAe" rowspan="5"></td><td rowspan="5" class="GOsQPe imspo_mt__wt"><div class="imspo_mt__ms-w"><div><div class="imspo_mt__ns-pm-s"><div class="imspo_mt__pm-inf imspo_mt__pm-infc imspo_mt__date imso-medium-font">Sam. 02/09</div><div class="imspo_mt__ndl-p imspo_mt__pm-inf imspo_mt__pm-infc imso-medium-font">15:00</div></div></div></div></td><td></td></tr><tr><td></td></tr><tr class="L5Kkcd"><td class="imspo_mt__lgc lc" data-df-team-mid="/m/0gz08s"><img class="imso_btl__mh-logo" alt="" src="//ssl.gstatic.com/onebox/media/sports/logos/rugby/bz7IBGAyOrjgDXoXgCTaVQ_48x48.png" style="width:24px;height:24px"></td><td class="tns-c imspo_mt__tt-w imspo_mt__dt-t"><div class="ellipsisize" data-df-team-mid="/m/0gz08s"><div class="liveresults-sports-immersive__hide-element">Oyonnax</div><span aria-hidden="true">Oyonnax</span></div></td><td class="imspo_mt__rg"></td></tr><tr class="L5Kkcd"><td class="imspo_mt__lgc lc" data-df-team-mid="/m/02yybv"><img class="imso_btl__mh-logo" alt="" src="//ssl.gstatic.com/onebox/media/sports/logos/rugby/h4vDbxK8-Si1XJcozKWBfQ_48x48.png" style="width:24px;height:24px"></td><td class="tns-c imspo_mt__tt-w imspo_mt__dt-t"><div class="ellipsisize" data-df-team-mid="/m/02yybv"><div class="liveresults-sports-immersive__hide-element">Toulouse</div><span aria-hidden="true">Toulouse</span></div></td><td class="imspo_mt__rg"></td></tr><tr><td></td></tr><tr class="bN3Vue"></tr></tbody></table>
