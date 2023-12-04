package main

import (
	elfmanager "AOC/day_1/elf-manager"
	"fmt"
)

func main() {

	data, err := elfmanager.ReadFileLines("elf-input.txt")
	if err != nil {
		fmt.Println("error when reading file: %w", err)
		return
	}

	inventories, err := elfmanager.CombineElfInventory(data)
	if err != nil {
		fmt.Println("error when parsing top elf inventories: %w", err)
		return
	}

	topElf := elfmanager.TopElves(inventories, 1)
	fmt.Printf("Part one: Highest calories: %d \n", topElf)

	topThreeElves := elfmanager.TopElves(inventories, 3)
	fmt.Printf("Part two: Total Calories for top three: %d \n", topThreeElves)
}
