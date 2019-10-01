"""
Functions for generating an argument parser for the img2ascii2svg script
"""

import argparse


def build_parser():
    """Build the arguments parser for img2ascii2svg."""
    parser = argparse.ArgumentParser(
        prog="img2ascii2svg", description="Converts an image to ASCII, and then to SVG."
    )

    parser.add_argument("infile", help="Path to the image to read from.")

    parser.add_argument(
        "-d",
        "--drop",
        nargs=1,
        default=[-1],
        type=float,
        help="When this flag is set, all pixels with a value at or below "
        + "the DROP threshold (where 0 <= DROP <= 1) are represented "
        + "with an empty space ' ' in the ASCII portrait. This can help "
        + "reduce clutter.",
    )

    parser.add_argument(
        "-i", "--invert", action="store_true", help="Invert the color scheme."
    )

    # Add argument groups
    add_output_formats_to_parser(parser)
    add_scaling_arguments_to_parser(parser)
    add_advanced_options_arguments_to_parser(parser)

    return parser


def add_output_formats_to_parser(parser):
    """Add flags for output formats to the arguments parser."""
    output_formats_group = parser.add_argument_group(
        "Output formats",
        "Specify whether (and if so, where and and in what format) "
        + "you want to save the ASCII image.",
    )

    output_formats_group.add_argument(
        "--svg",
        nargs=1,
        default=None,
        help="Specify a path to save the image as an .svg file after "
        + "converting it to ASCII. If left unspecified, the image "
        + "won't be saved as SVG.",
    )

    output_formats_group.add_argument(
        "--ascii",
        nargs=1,
        default=None,
        help="Specify a path to the the ASCII image as a .txt file. "
        + "If left unspecified, the image won't be saved as .txt "
        + "(although it will still be displayed on-screen).",
    )


def add_scaling_arguments_to_parser(parser):
    """Add flags for image scaling arguments to the arguments parser."""
    scaling_group = parser.add_argument_group(
        "Scaling factors",
        "Horizontal and vertical scaling factors for the output image(s).",
    )

    scaling_group.add_argument(
        "-vs",
        "--vscale",
        nargs=1,
        default=[1],
        type=float,
        help="Vertical scaling factor (default: 1).",
    )

    scaling_group.add_argument(
        "-hs",
        "--hscale",
        nargs=1,
        default=[1],
        type=float,
        help="Horizontal scaling factor (default: 1).",
    )


def add_advanced_options_arguments_to_parser(parser):
    """Add flags for advanced options to the arguments parser."""
    advanced_options_group = parser.add_argument_group(
        "Advanced options", "Hyperparameters for fine-tuning your image."
    )

    advanced_options_group.add_argument(
        "--min-intensity",
        nargs=1,
        default=[0.05],
        type=float,
        help="Smallest pixel value in the image after rescaling "
        + "pixel intensities (default: 0.05). Should be between "
        + "0 and 1.",
    )

    advanced_options_group.add_argument(
        "--max-intensity",
        nargs=1,
        default=[0.40],
        type=float,
        help="Largest pixel value in the image after rescaling "
        + "pixel intensities (default: 0.40). Should be between "
        + "0 and 1.",
    )
