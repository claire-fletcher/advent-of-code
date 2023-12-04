// Package elfmanager provides functions to manage elven adventures.
package elfmanager

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

// ReadFileLines reads the input file into a slice of each line.
func ReadFileLines(path string) ([]string, error) {

	file, err := os.Open(path)
	if err != nil {

		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return lines, scanner.Err()
}

// CombineElfInventory Reads all of the elf data for their inventories and combines.
func CombineElfInventory(elfCalories []string) ([]int, error) {

	var combinedCalories []int
	var currentTotal int

	// Add values until reach blank line
	for _, calorie := range elfCalories {

		if calorie == "" {
			combinedCalories = append(combinedCalories, currentTotal)
			currentTotal = 0

			continue
		}

		convertedCalorie, err := strconv.Atoi(calorie)
		if err != nil {
			fmt.Println("error during conversion: %w", err)

			return nil, err
		}

		currentTotal += convertedCalorie
	}

	return combinedCalories, nil
}

// TopElves will combine the top n elf calories for efficient adventure planning.
func TopElves(combinedCalories []int, numberElves int) int {

	// Sort in reverse order so id 0 is the highest
	sort.Sort(sort.Reverse(sort.IntSlice(combinedCalories)))

	// Get the top n elf values
	topElves := combinedCalories[:numberElves]

	sum := 0
	for i := range topElves {
		sum += topElves[i]
	}

	return sum
}
