#!/usr/bin/env python3

from src import *

"""
main script
"""
if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()
    weights = compute_character_weights(DEFAULT_CHARSET)
    pixels = read_pixels(args)

    if args.invert:
        pixels = 1 - pixels

    min_intensity = args.min_intensity[0]
    max_intensity = args.max_intensity[0]

    if min_intensity >= max_intensity:
        print(
            f"Error: received min_intensity = {min_intensity} > max_intensity = {max_intensity}"
        )
        print("The minimum pixel intensity must be less than the maximum.")
        sys.exit(1)

    rescaled_pixels = rescale_pixels(pixels, min_intensity, max_intensity)

    # Convert the image to an ASCII portrait
    txt = pixels_to_ascii(rescaled_pixels, DEFAULT_CHARSET, weights)

    # Drop all pixels below the drop threshold specified in the arguments
    txt[pixels <= args.drop[0] * 255] = " "

    # Convert to string from numpy array
    txt = "\n".join("".join(row) for row in txt)

    print(txt)

    if args.ascii is not None:
        with open(args.ascii[0], "w") as output:
            output.write(txt + "\n")

    if args.svg is not None:
        with open(args.svg[0], "w") as output:
            svg = ascii_to_svg(txt)
            output.write(svg)
