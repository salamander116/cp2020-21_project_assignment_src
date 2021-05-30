#!/bin/bash
COUNTER=1
THREADS=(4 8 16 32)


cat test_files/index.txt | while read line
do	
	echo "Running test battery # "$COUNTER


		if [ "$COUNTER" -eq "3" ]; then 

			./energy_storms_seq $line >> "test_files/results/03".txt

			./energy_storms_omp 2 $line >> "test_files/results/03".txt

			./energy_storms_omp 4 $line >> "test_files/results/03".txt
		fi
		

		if [ "$COUNTER" -eq "4" ]; then 

			./energy_storms_seq $line >> "test_files/results/04".txt

			./energy_storms_omp 2 $line >> "test_files/results/04".txt

			./energy_storms_omp 4 $line >> "test_files/results/04".txt

		fi

		if [ "$COUNTER" -eq "5" ]; then 

			./energy_storms_seq $line >> "test_files/results/05".txt

			./energy_storms_omp 2 $line >> "test_files/results/05".txt

			./energy_storms_omp 4 $line >> "test_files/results/05".txt

		fi

		if [ "$COUNTER" -eq "6" ]; then 

			./energy_storms_seq $line >> "test_files/results/06".txt

			./energy_storms_omp 2 $line >> "test_files/results/06".txt

			./energy_storms_omp 4 $line >> "test_files/results/06".txt

		fi

		if [ "$COUNTER" -eq "9" ]; then 
			
			./energy_storms_seq 16 $line >> "test_files/results/09".txt
			./energy_storms_seq 17 $line >> "test_files/results/09".txt
			
			
			for T in "${THREADS[@]}"; do
				

				./energy_storms_seq 16 $line >> "test_files/results/09".txt

				./energy_storms_omp $T 16 $line >> "test_files/results/09".txt

				./energy_storms_omp $T 17 $line >> "test_files/results/09".txt

			done


			else

				for T in "${THREADS[@]}"; do

					./energy_storms_seq $line >> "test_files/results/$COUNTER".txt

					./energy_storms_omp $T $line >> "test_files/results/$COUNTER".txt

				done
		fi

	COUNTER=$((COUNTER+1))

done