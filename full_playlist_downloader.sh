#!/bin/bash
let count=0
code=""
while IFS= read -r line; do
    # echo $count
    if (( $count % 2 == 0 ))
    then
        v2=$(echo -e "$line" | tr -d '[:space:]')
        # v2="$v2.txt"
    fi
    if (( $count % 2 == 1 ))
    then
        v1=$line
        echo $v1 $v2
        ./run.sh $v1 $v2
    fi

    ((count++))
done < "$1"