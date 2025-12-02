#!/bin/bash

INPUT_RANGES=$(cat $1)

INVALID_IDS_FOUND=""

IFS=',' read -ra RANGES <<<"$INPUT_RANGES"

TOTAL_SUM=0
for range in "${RANGES[@]}"; do
  start_id=$(echo "$range" | cut -d- -f1)
  end_id=$(echo "$range" | cut -d- -f2)

  i=$start_id
  while [ 1 ]; do
    if [[ $i -eq $end_id ]]; then
      break
    fi

    id_str=$i
    len=${#id_str}

    if ((len % 2 == 0)); then
      half_len=$((len / 2))
      part1=${id_str:0:half_len}
      part2=${id_str:half_len}

      if [ "$part1" == "$part2" ]; then
        TOTAL_SUM=$(($TOTAL_SUM + $id_str))
      fi
    fi

    i=$(($i + 1))
  done
done

echo $TOTAL_SUM
