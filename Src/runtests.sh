COUNTER=1
ARRSIZE=$1

mkdir -p "test_files/results/size_$ARRSIZE"
cat test_files/index.txt | while read line
do	
	echo "Running test battery # "$COUNTER


	./energy_storms_seq $ARRSIZE $line >> "test_files/results/size_$ARRSIZE/$COUNTER".txt

	./energy_storms_omp $ARRSIZE $line >> "test_files/results/size_$ARRSIZE/$COUNTER".txt

	COUNTER=$((COUNTER+1))

done