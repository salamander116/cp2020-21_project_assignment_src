#!/bin/bash
COUNTER=1
ARRSIZE=$1


mkdir -p "test_files/results/size_$ARRSIZE"
cat test_files/index.txt | while read line
do	
	echo "Running test battery # "$COUNTER

	if [ "$COUNTER" -eq "9" ]; then 
			echo "xd"

			./energy_storms_seq 16 $line >> "test_files/results/09_16".txt

			./energy_storms_omp 16 $line >> "test_files/results/09_16".txt

			./energy_storms_seq 17 $line >> "test_files/results/09_17".txt

			./energy_storms_omp 17 $line >> "test_files/results/09_17".txt


		else

			./energy_storms_seq $line >> "test_files/results/$COUNTER".txt

			./energy_storms_omp $line >> "test_files/results/$COUNTER".txt
	fi

	COUNTER=$((COUNTER+1))

done