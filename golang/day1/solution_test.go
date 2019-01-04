package main

import (
	"reflect"
	"testing"
)

func TestSolution1(t *testing.T) {
	var tests = []struct {
		input    []int
		expected int
	}{
		{[]int{}, 0},
		{[]int{1, 1, 1}, 3},
		{[]int{1, 1, -2}, 0},
		{[]int{-1, -2, -3}, -6},
	}

	for _, test := range tests {
		if output := Solution1(test.input); output != test.expected {
			t.Error("Test Failed: {} input, {} expected, recieved: {}", test.input, test.expected, output)
		}
	}
}

func TestSolution2(t *testing.T) {
	var tests = []struct {
		input    []int
		expected int
	}{
		{[]int{1, -1}, 0},
		{[]int{3, 3, 4, -2, -4}, 10},
		{[]int{-6, 3, 8, 5, -6}, 5},
		{[]int{7, 7, -2, -7, -4}, 14},
	}

	for _, test := range tests {
		if output := Solution2(test.input); output != test.expected {
			t.Error("Test Failed: input={", test.input, "}, expected={", test.expected, "}, recieved={", output, "}")
		}
	}
}

func TestLoadFile(t *testing.T) {
	var tests = []struct {
		input    string
		expected []int
	}{
		{"test1.txt", []int{1, 1, 1}},
		{"test2.txt", []int{1, 1, -2}},
		{"test3.txt", []int{-1, -2, -3}},
	}

	for _, test := range tests {
		if output := LoadFile(test.input); !reflect.DeepEqual(output, test.expected) {
			t.Error("Test Failed: {} input, {} expected, recieved: {}", test.input, test.expected, output)
		}
	}
}
