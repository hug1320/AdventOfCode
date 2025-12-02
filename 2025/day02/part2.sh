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
    half_len=$((len / 2))
    if [[ $(($half_len / 2)) -eq 1 ]]; then
      half_len=$(($half_len + 1))
    fi
    for j in $(seq $half_len); do
      if ((len % $j == 0)); then
        block_nb=$((len / $j))
        part1=${id_str:0:$j}
        equals=1
        for k in $(seq $(($block_nb - 1))); do
          lim1=$(($k * $j))
          part2=${id_str:${lim1}:$j}

          if [ "$part1" != "$part2" ]; then
            equals=0
            break
          fi
        done
        if [[ equals -eq 1 ]]; then
          TOTAL_SUM=$(($TOTAL_SUM + $id_str))
          break
        fi
      fi
    done
    i=$(($i + 1))
  done
done

echo $TOTAL_SUM
