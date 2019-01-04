package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

// LoadFile Load a file
func LoadFile(filename string) (result []int) {

	f, err := os.OpenFile(filename, os.O_RDONLY, os.ModePerm)
	if err != nil {
		log.Fatalf("open file error: %v", err)
		return result
	}
	defer f.Close()

	sc := bufio.NewScanner(f)
	for sc.Scan() {
		i, _ := strconv.Atoi(sc.Text())
		result = append(result, i)
	}

	return result
}

// Solution1 Calculate the solution for part 1
func Solution1(arr []int) (result int) {
	for _, element := range arr {
		result += element
	}
	return result
}

// Solution2 Calculate the solution for part 2
func Solution2(arr []int) int {
	var seen = make(map[int]bool)
	seen[0] = true

	var result int
	var found bool = false
	for !found {
		for _, element := range arr {
			result += element
			if seen[result] {
				found = true
				break
			}
			seen[result] = true
		}
	}
	return result
}

func main() {
	fmt.Printf("%v\n", Solution1(LoadFile("input.txt")))
	fmt.Printf("%v\n", Solution2(LoadFile("input.txt")))
}
