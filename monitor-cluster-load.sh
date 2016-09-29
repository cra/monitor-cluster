#!/bin/bash

JOBCOUNT=$(squeue -u $USER -h | wc -l)
RUNCOUNT=$(squeue -u $USER -h --states running | wc -l)
EMPTY_NODES_CPU=$(sinfo -t idle -p CPU-part | awk '{print $4}' | tail -n1)

echo "-- Overall cluster occupancy"
sinfo -h #-p CPU-part GPU-part
echo

echo -e "-- Cluster terrorists (total nodes occupied > 6):\n`squeue -h -t R --format '%P %u %T %D' | cluster_terrorists.py`\n"

echo -e "-- Empty nodes in CPU-part: ${EMPTY_NODES_CPU}\n"

echo -e "-- Number of my jobs in SLURM queue: -->> ${JOBCOUNT} (running: ${RUNCOUNT}) <<--\n"
echo -e "-- Jobnames of my running jobs:\n`squeue -u $USER -t R -h --format '%i %P %40j %u %T' | job_count.py`\n"

echo -e "-- My pending jobs:\n`squeue -u $USER -t PD -h --format '%i %P %40j %u %T' | job_count.py`\n"
