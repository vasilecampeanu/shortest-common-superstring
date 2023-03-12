import time
import matplotlib.pyplot as plt
from ShotgunSequencing import *

def time_function(func, num_runs=100):
    """ Times the execution of a given function and returns the elapsed time.

    Args:
        func (callable): The function to time.
        *args: The positional arguments to pass to the function.
        num_runs (int): The number of times to run the function.
        **kwargs: The keyword arguments to pass to the function.

    Returns:
        float: The average elapsed time (in seconds) over num_runs.
    """

    elapsed_times = []
    generator = ShotgunSequencing(100, 2, 25, 50)

    for i in range(num_runs):
        start_time = time.perf_counter()
        dna_reads = generator.generate_shotgun_reads()
        func(dna_reads)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        elapsed_times.append(elapsed_time)

    return elapsed_times

def plot_elapsed_times(elapsed_times, title=None):
    """Plots the elapsed times as a line chart.

    Args:
        elapsed_times (list of float): The elapsed times to plot.
        title (str): The title of the plot.
    """

    plt.plot(elapsed_times)
    plt.xlabel("Run Number")
    plt.ylabel("Elapsed Time (s)")

    if title:
        plt.title(title)

    plt.show()
