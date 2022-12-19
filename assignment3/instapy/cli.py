"""Command-line (script) interface to instapy"""

import argparse
import sys

import numpy as np
from PIL import Image

import instapy
from . import io


def run_filter(
    file: str,
    out_file: str = None,
    implementation: str = "python",
    filter: str = "color2gray",
    scale: int = 1,
) -> None:
    """Run the selected filter"""
    # load the image from a file
    image = Image.open(file)

    if scale != 1:
        # Resize image, if needed
        image = image.resize((image.width//scale, image.height//scale))
        image = np.asarray(image)

    # Apply the filter
    f = instapy.get_filter(filter, implementation)
    filtered = f(np.asarray(image))
    
    if out_file:
        # save the file
        image.save(out_file + ".jpg")
    else:
        # not asked to save, display it instead
        io.display(filtered)


def main(argv=None):
    """Parse the command-line and call run_filter with the arguments"""
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser()

    # filename is positional and required
    parser.add_argument("file", help="The filename to apply filter to")
    parser.add_argument("-o", "--out", help="The output filename")

    # Add required arguments
    parser.add_argument("-g", "--gray", help="Select gray filter", action = "store_true")
    parser.add_argument("-se", "--sepia", help="Select sepia filter", action = "store_true")
    parser.add_argument("-sc", "--scale", help="Select factor to resize image")
    parser.add_argument("-i", "--implementation", help="Select the implementation", choices = ["numba", "numpy", "python"])


    # parse arguments and call run_filter
    args = parser.parse_args()
    parser.print_help()

    scale = 1
    filter = "color2gray"
    implementation = "python"

    if args.gray == True:
        filter = "color2gray"
    elif args.sepia == True:
        filter = "color2sepia"
    if args.scale != None:
        scale = args.scale
    if args.implementation != None:
        implementation = args.implementation

    run_filter(args.file, args.out, implementation, filter, int(scale))
