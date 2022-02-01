## Wordle Helper

### Introduction

A script to help you guess words in the famous game [Wordle](https://www.powerlanguage.co.uk/wordle/). This will help you narrow down the word options based on the letters you start playing with. 

Typically I start with words "ADIEU" and "STORY" and based on the results from there, I start the script and it helps me narrow down the potential words. 


### How to use
To use the script, 


```
python3 wordle_helper.py
```


Example script for game 226

```
 leo@Abhilashs-MacBook-Pro  ~/Developer/WordleHelper   mainline  python3 wordle_helper.py
Enter new letters to include without spaces (include green). [Already included : []] [E.g. -- ro] : it
enter letters to exclude without spaces.[Already excluded : []] [E.g. xy] : adeusory
enter idx and letters found. space separated. Start with 0. [Already found : []] [E.g. 0r 1o 2b for rob__] :
{'thigh', 'thick', 'thing', 'night', 'might', 'light', 'tight', 'flint', 'wight', 'witch', 'blitz', 'think', 'fight', 'ninth', 'pitch', 'glint', 'hitch', 'filth', 'fifth', 'limit', 'twixt'}
Continue playing? y/n : y
Enter new letters to include without spaces (include green). [Already included : ['i', 't']] [E.g. -- ro] :
enter letters to exclude without spaces.[Already excluded : ['a', 'd', 'e', 'u', 's', 'o', 'r', 'y']] [E.g. xy] : mf
enter idx and letters found. space separated. Start with 0. [Already found : []] [E.g. 0r 1o 2b for rob__] :
{'light', 'witch', 'thigh', 'hitch', 'tight', 'blitz', 'think', 'thick', 'ninth', 'thing', 'glint', 'pitch', 'night', 'wight', 'twixt'}
Continue playing? y/n :
```


### Future Work

These are the following features that are yet to be incorporated 

1. Feature to take in "Yellow" letters. 
2. Feature to sort words based on probability (depending on words that appeared previously)