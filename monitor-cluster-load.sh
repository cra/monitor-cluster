#!/bin/bash

JOBCOUNT=$(squeue -u $USER -h | wc -l)
RUNCOUNT=$(squeue -u $USER -h --states running | wc -l)

echo "-- Overall cluster occupancy"
sinfo -h -p CPU-part
echo

echo -e "-- Number of my jobs in SLURM queue: -->> ${JOBCOUNT} (running: ${RUNCOUNT}) <<--\n"
echo -e "-- Jobnames of my running jobs:\n`squeue -u $USER -t R -h --format '%i %P %40j %u %T' | job_count.py`\n"

echo -e "-- My pending jobs:\n`squeue -u $USER -t PD -h --format '%i %P %40j %u %T' | job_count.py`\n"
