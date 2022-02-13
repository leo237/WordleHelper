## Wordle Helper

### Introduction

A script to help you guess words in the famous game [Wordle](https://www.powerlanguage.co.uk/wordle/). This will help you narrow down the word options based on the letters you start playing with. 

Typically I start with words "ADIEU", "CRANE" and "STORY" and based on the results from there, I start the script and it helps me narrow down the potential words. 


### How to use
To use the script, 


```
python3 wordle_helper.py
```

Follow the prompts. First enter the word. Then enter whether each character was GREY (x), YELLOW (y) or GREEN (g) in the next line. 

Each 


Example script for game 238

```
✘ leo@Abhilashs-MacBook-Pro  ~/Developer/WordleHelper   mainline ±✚  python3 wordle_helper.py
Enter word you entered : crane
Enter the colors for each letter. Use key (x) for grey, (y) for yellow and (g) for green. No spaces e.g. xyxxgx :xyyxx
{'foray', 'parka', 'tardy', 'rapid', 'radii', 'harsh', 'viral', 'moral', 'ralph', 'fairy', 'ratio', 'rival', 'marry', 'rural', 'valor', 'major', 'dairy', 'radar', 'parry', 'augur', 'rumba', 'abhor', 'straw', 'vapor', 'karma', 'raspy', 'warty', 'solar', 'molar', 'mayor', 'harry', 'aorta', 'savor', 'hairy', 'agora', 'rabbi', 'hardy', 'sugar', 'ultra', 'royal', 'satyr', 'stray', 'tarot', 'rally', 'larva', 'rajah', 'mural', 'ratty', 'marsh', 'radio', 'abort', 'favor', 'strap', 'tapir', 'altar', 'razor', 'labor', 'flora', 'rabid', 'polar', 'party', 'umbra', 'spray', 'harpy', 'borax'}
Continue playing? y/n : y
Enter word you entered : party
Enter the colors for each letter. Use key (x) for grey, (y) for yellow and (g) for green. No spaces e.g. xyxxgx :xyyyx
{'abort', 'ultra', 'altar'}
Continue playing? y/n : n
```


### Future Work

These are the following features that are yet to be incorporated 

1. Feature to sort words based on probability (depending on words that appeared previously)