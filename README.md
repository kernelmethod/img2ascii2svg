# img2svg2ascii
A script that will convert an image to ASCII art, and then to an SVG file.

## Why?
I wanted to put some ASCII art on my website (https://kernelmethod.dev) but ran into a few problems:

- ASCII art is difficult to scale to different screen sizes, and there are a lot of corner cases in which they can be rendered in undesirable ways.
  - Easy fixes to this problem, like screenshotting your art, aren't great because they lose a lot of the quality of the original art. They also result in files that are significantly larger than the raw ASCII text.
- It's also harder to customize. For instance, I wanted to perfectly enclose my ASCII art in a pair of concentric circles.
- Finally, ASCII art generators vary widely in quality. They also tend not to provide a lot of options for customization.

`img2ascii2svg.py` is a script that addresses each of these problems, by creating ASCII art and then converting it to an SVG file that scales well for different browsers. Usually these files are 80-90% smaller after gzip compression, giving them a significant size and quality advantage over other methods for serving ASCII art.

## Examples
**Note**: currently, img2ascii2svg uses a small amount of JavaScript to ensure that images fit in a square container. If you want to change the dimensions, you should do that in your CSS.

In environments that render the image without running JavaScript, I've attempted to define my parameters in such a way that the SVG renders in a way that is reasonably close to the ASCII art. That said, there are edge cases in which the right portion of the image gets clipped off. I'm currently trying to identify whether it would be possible to fix this issue with pure SVG and/or CSS.

![Image of Mew in Pokemon Red](https://raw.githubusercontent.com/wshand/img2ascii2svg/master/docs/img/mew_pokemon_red.png)
- **Command**: 
```
./img2ascii2svg.py ./mew_pokemon_red.png \
    -vs 12 -hs 12 \
    --ascii mew_pokemon_red.txt --svg mew_pokemon_red.svg
```
- [ASCII output](https://raw.githubusercontent.com/wshand/img2ascii2svg/master/docs/ascii/mew_pokemon_red.txt)
- [SVG output](https://github.com/wshand/img2ascii2svg/blob/master/docs/svg/mew_pokemon_red.svg)

![Image of Mew in Pokemon Yellow](https://raw.githubusercontent.com/wshand/img2ascii2svg/master/docs/img/mew_pokemon_yellow.png)
- **Command**: 
```
./img2ascii2svg.py ./mew_pokemon_yellow.png \
      -hs 16 -vs 16 -d 0 \
      --ascii mew_pokemon_yellow.txt --svg mew_pokemon_yellow.svg
```
- [ASCII output](https://raw.githubusercontent.com/wshand/img2ascii2svg/master/docs/ascii/mew_pokemon_yellow.txt)
- [SVG output](https://github.com/wshand/img2ascii2svg/blob/master/docs/svg/mew_pokemon_yellow.svg)

![Image of Kyubey](https://raw.githubusercontent.com/wshand/img2ascii2svg/master/docs/img/kyubey.gif)

(Note that this script will accept GIFs, although it will only convert the first frame to ASCII art.)
- **Command**:
```
./img2ascii2svg.py ./kyubey.gif \
      -vs 2 -hs 2 \
      --min-intensity 0 --max-intensity 0.4 \
      --ascii kyubey.txt --svg kyubey.txt`
```
- [ASCII output](https://raw.githubusercontent.com/wshand/img2ascii2svg/master/docs/ascii/kyubey.txt)
- [SVG output](https://github.com/wshand/img2ascii2svg/blob/master/docs/svg/kyubey.svg)

![Image of Ralsei](https://raw.githubusercontent.com/wshand/img2ascii2svg/master/docs/img/ralsei.png)
- **Command**: 
```
./img2ascii2svg.py ./ralsei.png \
      -vs 2 -hs 2 \
      --min-intensity 0 --max-intensity 0.7 \
      --ascii ralsei.txt --svg ralsei.svg
```
- [ASCII output](https://raw.githubusercontent.com/wshand/img2ascii2svg/master/docs/ascii/ralsei.txt)
- [SVG output](https://github.com/wshand/img2ascii2svg/blob/master/docs/svg/ralsei.svg)

## Usage

```
usage: img2ascii2svg [-h] [-d DROP] [-i] [--svg SVG] [--ascii ASCII]
                     [-vs VSCALE] [-hs HSCALE] [--min-intensity MIN_INTENSITY]
                     [--max-intensity MAX_INTENSITY]
                     infile

Converts an image to ASCII, and then to SVG.

positional arguments:
  infile                Path to the image to read from.

optional arguments:
  -h, --help            show this help message and exit
  -d DROP, --drop DROP  When this flag is set, all pixels with a value at or
                        below the DROP threshold (where 0 <= DROP <= 1) are
                        represented with an empty space ' ' in the ASCII
                        portrait. This can help reduce clutter.
  -i, --invert          Invert the color scheme.

Output formats:
  Specify whether (and if so, where and and in what format) you want to save
  the ASCII image.

  --svg SVG             Specify a path to save the image as an .svg file after
                        converting it to ASCII. If left unspecified, the image
                        won't be saved as SVG.
  --ascii ASCII         Specify a path to the the ASCII image as a .txt file.
                        If left unspecified, the image won't be saved as .txt
                        (although it will still be displayed on-screen).

Scaling factors:
  Horizontal and vertical scaling factors for the output image(s).

  -vs VSCALE, --vscale VSCALE
                        Vertical scaling factor (default: 1).
  -hs HSCALE, --hscale HSCALE
                        Horizontal scaling factor (default: 1).

Advanced options:
  Hyperparameters for fine-tuning your image.

  --min-intensity MIN_INTENSITY
                        Smallest pixel value in the image after rescaling
                        pixel intensities (default: 0.05). Should be between 0
                        and 1.
  --max-intensity MAX_INTENSITY
                        Largest pixel value in the image after rescaling pixel
                        intensities (default: 0.40). Should be between 0 and
                        1.
```

## TODO
- Right now, the algorithm for generating art is roughly based off of https://code.activestate.com/recipes/580702-image-to-ascii-art-converter/, although it's been vectorized to run much faster. This algorithm works by matching pixels with characters that have the closest pixel intensities, which tends to work fairly well. However, it would be interesting to explore alternatives, e.g. using maximum inner product search (MIPS) on pixel patches to identify which characters are the best match within those patches.
- There are some edge cases in which the SVG conversion doesn't work well, e.g. when the image has a much larger width than height. I don't know too much about SVG, so please submit a PR if you have suggestions about how I can get around these edge cases. :)
