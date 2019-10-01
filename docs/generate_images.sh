#!/bin/bash
../img2ascii2svg.py ./img/mew_pokemon_red.png \
    -vs 12 -hs 12 \
    --ascii ./ascii/mew_pokemon_red.txt --svg ./svg/mew_pokemon_red.svg

../img2ascii2svg.py ./img/mew_pokemon_yellow.png \
      -hs 16 -vs 16 -d 0 \
      --ascii ./ascii/mew_pokemon_yellow.txt --svg ./svg/mew_pokemon_yellow.svg

../img2ascii2svg.py ./img/kyubey.gif \
      -vs 3 -hs 1.8 \
      --min-intensity 0 --max-intensity 0.4 \
      --ascii ./ascii/kyubey.txt --svg ./svg/kyubey.svg

../img2ascii2svg.py ./img/ralsei.png \
      -vs 2 -hs 2 \
      --min-intensity 0 --max-intensity 0.7 \
      --ascii ./ascii/ralsei.txt --svg ./svg/ralsei.svg
