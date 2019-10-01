"""
Code for image -> ASCII art conversion

Loosely adapated from:
   https://code.activestate.com/recipes/580702-image-to-ascii-art-converter/
"""

from PIL import Image, ImageDraw, ImageFont
import numpy as np

"""
Global variables
"""
DEFAULT_CHARSET = (
    r"_t(~vw,=d.W\nQ%^VpBqg1Co92{8Uy*$]!+Tnh&u)GSzmkZl4D@EHic? aI}:XY|s3`-;j#e"
)

"""
Helper functions
"""


def compute_character_weights(charset):
    """
    Calculate weights of ASCII chars
    """
    font = ImageFont.load_default()  # load default bitmap monospaced font
    (chrx, chry) = font.getsize(" ")

    weights = np.zeros(len(charset))
    for (ii, c) in enumerate(charset):
        chrImage = font.getmask(c)
        ctr = 0
        for y in range(chry):
            for x in range(chrx):
                if chrImage.getpixel((x, y)) > 0:
                    ctr += 1
        weights[ii] = float(ctr) / (chrx * chry)

    return weights


def read_pixels(args):
    """
    Read image from a file and grab pixel values from it.
    """
    font = ImageFont.load_default()
    (chrx, chry) = font.getsize(" ")

    image = Image.open(args.infile)
    (imgx, imgy) = image.size
    imgx = int(imgx / chrx * args.hscale[0])
    imgy = int(imgy / chry * args.vscale[0])

    # NEAREST/BILINEAR/BICUBIC/ANTIALIAS
    image = image.resize((imgx, imgy), Image.BICUBIC)
    image = image.convert("L")  # convert to grayscale

    return np.asarray(image).astype(np.float32)


def rescale_pixels(pixels, min_intensity, max_intensity):
    # Warp pixel values into the range [min_intensity, max_intensity]
    pixels = (pixels - pixels.min()) / (pixels.max() - pixels.min())
    pixels = pixels * (max_intensity - min_intensity) + min_intensity

    return pixels


"""
Main image -> ASCII conversion function.
"""


def pixels_to_ascii(pixels, charset, weights):
    """
    Takes an array of pixels, a character set, and a list of weights for those
    characters, and finds the characters that are closest in pixel intensity.
    """
    imgy, imgx = pixels.shape

    # find closest weight match
    closest_diffs = np.ones((imgy, imgx))
    closest_chars = np.chararray((imgy, imgx))

    for (c, wc) in zip(charset, weights):
        diffs = np.abs(wc - pixels)
        closest_chars[diffs < closest_diffs] = c
        closest_diffs = np.minimum(closest_diffs, diffs)

    return np.array(list(map(lambda c: c.decode("utf-8"), closest_chars)))
