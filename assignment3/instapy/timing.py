"""
Timing our filter implementations.

Can be executed as `python3 -m instapy.timing`

For Task 6.
"""
import time
import instapy
from instapy import io
from typing import Callable
import numpy as np
from PIL import Image


def time_one(filter_function: Callable, *arguments, calls: int = 3) -> float:
    """Return the time for one call

    When measuring, repeat the call `calls` times,
    and return the average.

    Args:
        filter_function (callable):
            The filter function to time
        *arguments:
            Arguments to pass to filter_function
        calls (int):
            The number of times to call the function,
            for measurement
    Returns:
        time (float):
            The average time (in seconds) to run filter_function(*arguments)
    """
    # run the filter function `calls` times
    # return the _average_ time of one call

    image = arguments[0]

    start_time = time.time()
    for i in range(calls):
        img = np.array(image)
        filter_function(img)


    end_time = time.time()
    elapsed_time = end_time - start_time
    average = elapsed_time/calls
    
    return average


def make_reports(filename: str = "/Users/user/Documents/DigOk/3.år/IN3110/IN3110-zharabr/assignment3/test/rain.jpg", calls: int = 3):
    """
    Make timing reports for all implementations and filters,
    run for a given image.

    Args:
        filename (str): the image file to use
    """
    #creating report
    report = open("timing-report.txt", 'w')

    #load the image
    image = io.read_image(filename)

    # print the image name, width, height
    width, height = image.shape[:2]
    img_name = filename.split("/")
    
    report.write(f"The name of the image: {img_name[-1]}")
    report.write(f"\nThe width of the image: {width}")
    report.write(f"\nThe height of the image: {height}\n") 

    # iterate through the filters
    filter_names = ["color2gray", "color2sepia"]
    for filter_name in filter_names:
        # get the reference filter function
        reference_filter = filter_name
        # time the reference implementation
        reference_time = time_one(instapy.get_filter(reference_filter), image)
        report.write(
            f"\n\nReference (pure Python) filter time {filter_name}: {reference_time:.3}s ({calls=})"
        )
        # iterate through the implementations
        implementations = ["numpy", "numba"]
        for implementation in implementations:
            filter = filter_name
            # time the filter
            filter_time = time_one(instapy.get_filter(filter, implementation), image)
            # compare the reference time to the optimized time
            speedup = reference_time/filter_time
            report.write(
                f"\nTiming: {implementation} {filter_name}: {filter_time:.3}s ({speedup=:.2f}x)"
            )


if __name__ == "__main__":
    # run as `python -m instapy.timing`
    make_reports()
