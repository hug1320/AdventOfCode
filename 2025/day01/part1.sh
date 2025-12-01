#!/bin/bash

DIAL_SIZE=100

current_position=50

zero_count=0

while IFS= read -r rotation; do

  direction="${rotation:0:1}"
  distance="${rotation:1}"
  distance_val=$((distance))

  if [[ "$direction" == "L" ]]; then
    change=$((-distance_val))
  elif [[ "$direction" == "R" ]]; then
    change=$((distance_val))
  else
    continue
  fi

  new_position_raw=$((current_position + change))
  new_pos_mod_partiel=$((new_position_raw % DIAL_SIZE))
  new_pos_pre_final=$((new_pos_mod_partiel + DIAL_SIZE))
  new_position=$((new_pos_pre_final % DIAL_SIZE))

  current_position=$new_position

  if [ "$current_position" -eq 0 ]; then
    zero_count=$((zero_count + 1))
  fi

done <input

echo $zero_count
