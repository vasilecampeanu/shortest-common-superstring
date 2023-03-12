import time
import matplotlib.pyplot as plt

# define the number of runs to average over
num_runs = 100000

# initialize a list for storing the elapsed times
elapsed_times = []

for i in range(num_runs):
    # Start the timer
    start_time = time.perf_counter()
    
    # Get shortest path
    # Call the algorithm here
    
    # End the timer
    end_time = time.perf_counter()
    
    # Compute the elapsed time and add it to the list
    elapsed_time = end_time - start_time
    elapsed_times.append(elapsed_time)

# Plot the elapsed times using a line chart
plt.plot(elapsed_times)

# Add a title and labels for the axes
plt.title("Elapsed Times for TSP Function")
plt.xlabel("Run Number")
plt.ylabel("Elapsed Time (s)")

# Show the plot
plt.show()