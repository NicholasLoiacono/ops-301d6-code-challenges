#!/usr/bin/env python3

# Script: Ops 301d6 Class 11 Ops Challenge Solution
# Author: Nicholas Loiacono
# Date: 03/27/2023
# Purpose: Psutil
# Resources: Chat GPT


# Start

import psutil

# Get system CPU times
cpu_times = psutil.cpu_times()

# Print time spent by normal processes executing in user mode
print(f"Time spent by normal processes executing in user mode: {cpu_times.user:.2f} seconds")

# Print time spent by processes executing in kernel mode
print(f"Time spent by processes executing in kernel mode: {cpu_times.system:.2f} seconds")

# Print time when system was idle
print(f"Time when system was idle: {cpu_times.idle:.2f} seconds")

# Get per-CPU time spent by priority processes executing in user mode
cpu_times_per_cpu = psutil.cpu_times(percpu=True)
for i, cpu_times in enumerate(cpu_times_per_cpu):
    print(f"Time spent by priority processes executing in user mode (CPU {i}): {cpu_times.nice:.2f} seconds")

# Print time spent waiting for I/O to complete
print(f"Time spent waiting for I/O to complete: {cpu_times.iowait:.2f} seconds")

# Print time spent for servicing hardware interrupts
print(f"Time spent for servicing hardware interrupts: {cpu_times.irq:.2f} seconds")

# Print time spent for servicing software interrupts
print(f"Time spent for servicing software interrupts: {cpu_times.softirq:.2f} seconds")

# Print time spent by other operating systems running in a virtualized environment
print(f"Time spent by other operating systems running in a virtualized environment: {cpu_times.steal:.2f} seconds")

# Print time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
print(f"Time spent running a virtual CPU for guest operating systems: {cpu_times.guest:.2f} seconds")

# End