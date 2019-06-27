#!/bin/bash
let count=0

while IFS= read -r line; do
    # echo $count
    if (( $count % 2 == 0 ))
    then
        v2=$(echo -e "$line" | tr -d '[:space:]')
        v2="$v2.mp4"
    fi
    if (( $count % 2 == 1 ))
    then
        v1=$line
        echo $count : $v2
        curl $v1 \
        -H 'Accept-Encoding: identity;q=1, *;q=0' \
        -H 'Accept-Language: en-US,en;q=0.9' \
        -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/75.0.3770.90 Chrome/75.0.3770.90 Safari/537.36' \
        -H 'Accept: */*' \
        -H 'Connection: keep-alive' \
        -H 'Range: bytes=0-' \
        --compressed \
        --output $v2

        # curl $v1 --output $v2
    fi

    ((count++))
done < "$1"

# echo $code
