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
  if [[ "$new_position_raw" -lt 0 ]]; then
    if [[ "$current_position" -eq 0 ]]; then
      new_zeros=$(((new_position_raw / DIAL_SIZE) * -1))
    else
      new_zeros=$((((new_position_raw / DIAL_SIZE) - 1) * -1))
    fi
  elif [[ "$new_position_raw" -eq 0 ]]; then
    new_zeros=$(((new_position_raw / DIAL_SIZE) * -1 + 1))
  else
    new_zeros=$((new_position_raw / DIAL_SIZE))
  fi
  zero_count=$((zero_count + new_zeros))
  new_pos_mod_partiel=$((new_position_raw % DIAL_SIZE))
  new_pos_pre_final=$((new_pos_mod_partiel + DIAL_SIZE))
  new_position=$((new_pos_pre_final % DIAL_SIZE))

  current_position=$new_position

done

echo $zero_count
