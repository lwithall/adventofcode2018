package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

// LoadFile Load a file
func LoadFile(filename string) (result []string) {

	f, err := os.OpenFile(filename, os.O_RDONLY, os.ModePerm)
	if err != nil {
		log.Fatalf("open file error: %v", err)
		return result
	}
	defer f.Close()

	sc := bufio.NewScanner(f)
	for sc.Scan() {
		result = append(result, sc.Text())
	}

	return result
}

// Solution1Func will return number of two counts and three counts in word
func Solution1Func(word string) (twoCount bool, threeCount bool) {
	var count = make(map[rune]int)

	for _, c := range word {
		if _, ok := count[c]; ok {
			count[c]++
		} else {
			count[c] = 1
		}
	}

	for _, value := range count {
		if value == 2 {
			twoCount = true
		} else if value == 3 {
			threeCount = true
		}
	}

	return twoCount, threeCount
}

// Solution1 Calculate the solution for part 1
func Solution1(arr []string) (result int) {
	var twoCountTotal int
	var threeCountTotal int
	for _, word := range arr {
		twoCount, threeCount := Solution1Func(word)
		if twoCount {
			twoCountTotal++
		}
		if threeCount {
			threeCountTotal++
		}
	}
	return twoCountTotal * threeCountTotal
}

// NumDifferences returns the number of differences between
// the two strings
func NumDifferences(s1 string, s2 string) (count int, same string) {

	if len(s1) != len(s2) {
		return -1, ""
	}

	for i := range s1 {
		if s1[i] != s2[i] {
			count++
		} else {
			same += string(s1[i])
		}
	}

	return count, same
}

// Solution2 Calculate the solution for part 2
func Solution2(arr []string) string {

	for i := range arr {
		for j := i + 1; j < len(arr); j++ {
			if differences, same := NumDifferences(arr[i], arr[j]); differences == 1 {
				return same
			}
		}
	}

	return ""
}

func main() {
	fmt.Printf("%v\n", Solution1(LoadFile("input.txt")))
	fmt.Printf("%v\n", Solution2(LoadFile("input.txt")))
}
