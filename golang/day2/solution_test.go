package main

import (
	"testing"
)

func TestSolution1Func(t *testing.T) {
	var tests = []struct {
		input     string
		expected1 bool
		expected2 bool
	}{
		{"abcdef", false, false},
		{"bababc", true, true},
		{"abbcde", true, false},
		{"aabcdd", true, false},
		{"abcdee", true, false},
		{"ababab", false, true},
	}

	for _, test := range tests {
		output1, output2 := Solution1Func(test.input)
		if output1 != test.expected1 || output2 != test.expected2 {
			t.Error("Test Failed: {} input, {} {} expected, recieved: {} {}", test.input, test.expected1, test.expected2, output1, output2)
		}
	}
}

func TestNumDifferences(t *testing.T) {
	var tests = []struct {
		input1    string
		input2    string
		expected1 int
		expected2 string
	}{
		{"abcdef", "abcdef", 0, "abcdef"},
		{"abcde", "abcdef", -1, ""},
		{"abcde", "axcye", 2, "ace"},
		{"fghij", "fguij", 1, "fgij"},
	}

	for _, test := range tests {
		output1, output2 := NumDifferences(test.input1, test.input2)
		if output1 != test.expected1 || output2 != test.expected2 {
			t.Error("Test Failed: {} {} input, {} {} expected, recieved: {} {}", test.input1, test.input2, test.expected1, test.expected2, output1, output2)
		}
	}
}

func TestSolution2(t *testing.T) {
	var tests = []struct {
		input    []string
		expected string
	}{
		{
			[]string{"abcde",
				"fghij",
				"klmno",
				"pqrst",
				"fguij",
				"axcye",
				"wvxyz"},
			"fgij"},
	}

	for _, test := range tests {
		output := Solution2(test.input)
		if output != test.expected {
			t.Error("Test Failed: {} input, {} expected, recieved: {}", test.input, test.expected, output)
		}
	}
}

/*func TestLoadFile(t *testing.T) {
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
}*/
