#!/usr/bin/env python3
"""
Script to create template files for a new Advent of Code day.

Usage:
    python create_day.py <day_number> [language]
    
Examples:
    python create_day.py 5          # Creates day05 with Python template
    python create_day.py 12 js      # Creates day12 with JavaScript template
    python create_day.py 3 go       # Creates day03 with Go template
"""

import os
import sys
from pathlib import Path


PYTHON_TEMPLATE = '''#!/usr/bin/env python3
"""
Advent of Code 2025 - Day {day}
"""


def read_input(filename='input.txt'):
    """Read and parse the input file."""
    with open(filename, 'r') as f:
        return f.read().strip()


def part1(data):
    """
    Solve part 1 of the puzzle.
    
    Args:
        data: The puzzle input
        
    Returns:
        The solution to part 1
    """
    # TODO: Implement part 1 solution
    pass


def part2(data):
    """
    Solve part 2 of the puzzle.
    
    Args:
        data: The puzzle input
        
    Returns:
        The solution to part 2
    """
    # TODO: Implement part 2 solution
    pass


def main():
    """Main function to run the solutions."""
    data = read_input()
    
    # Part 1
    result1 = part1(data)
    print(f"Part 1: {{result1}}")
    
    # Part 2
    result2 = part2(data)
    print(f"Part 2: {{result2}}")


if __name__ == '__main__':
    main()
'''

JAVASCRIPT_TEMPLATE = '''#!/usr/bin/env node
/**
 * Advent of Code 2025 - Day {day}
 */

const fs = require('fs');

/**
 * Read and parse the input file
 * @param {{string}} filename - Input file name
 * @returns {{string}} File contents
 */
function readInput(filename = 'input.txt') {{
    return fs.readFileSync(filename, 'utf8').trim();
}}

/**
 * Solve part 1 of the puzzle
 * @param {{string}} data - The puzzle input
 * @returns {{*}} The solution to part 1
 */
function part1(data) {{
    // TODO: Implement part 1 solution
    return null;
}}

/**
 * Solve part 2 of the puzzle
 * @param {{string}} data - The puzzle input
 * @returns {{*}} The solution to part 2
 */
function part2(data) {{
    // TODO: Implement part 2 solution
    return null;
}}

/**
 * Main function to run the solutions
 */
function main() {{
    const data = readInput();
    
    // Part 1
    const result1 = part1(data);
    console.log(`Part 1: ${{result1}}`);
    
    // Part 2
    const result2 = part2(data);
    console.log(`Part 2: ${{result2}}`);
}}

if (require.main === module) {{
    main();
}}

module.exports = {{ part1, part2 }};
'''

GO_TEMPLATE = '''package main

import (
	"fmt"
	"os"
	"strings"
)

// readInput reads and parses the input file
func readInput(filename string) string {{
	data, err := os.ReadFile(filename)
	if err != nil {{
		panic(err)
	}}
	return strings.TrimSpace(string(data))
}}

// part1 solves part 1 of the puzzle
func part1(data string) interface{{}} {{
	// TODO: Implement part 1 solution
	return nil
}}

// part2 solves part 2 of the puzzle
func part2(data string) interface{{}} {{
	// TODO: Implement part 2 solution
	return nil
}}

func main() {{
	data := readInput("input.txt")
	
	// Part 1
	result1 := part1(data)
	fmt.Printf("Part 1: %v\\n", result1)
	
	// Part 2
	result2 := part2(data)
	fmt.Printf("Part 2: %v\\n", result2)
}}
'''

README_TEMPLATE = '''# Day {day}: [Problem Title]

[Link to problem](https://adventofcode.com/2025/day/{day_no_zero})

## Problem Description

### Part 1

[Description of part 1 will go here]

### Part 2

[Description of part 2 will go here]

## Solution Approach

### Part 1

[Explanation of the approach for part 1]

### Part 2

[Explanation of the approach for part 2]

## Usage

```bash
{run_command}
```

## Notes

- [Any additional notes or observations about the problem]
'''


def create_day_directory(day_num, language='python'):
    """
    Create directory structure for a new day.
    
    Args:
        day_num: Day number (1-25)
        language: Programming language to use
    """
    day_str = f"day{day_num:02d}"
    day_path = Path(day_str)
    
    if day_path.exists():
        print(f"Error: Directory '{day_str}' already exists!")
        return False
    
    # Create directory
    day_path.mkdir()
    print(f"Created directory: {day_str}/")
    
    # Create README.md
    language_commands = {
        'python': 'python solution.py',
        'py': 'python solution.py',
        'javascript': 'node solution.js',
        'js': 'node solution.js',
        'go': 'go run solution.go'
    }
    
    run_command = language_commands.get(language.lower(), f'# Run the {language} solution')
    
    readme_content = README_TEMPLATE.format(
        day=day_str,
        day_no_zero=day_num,
        run_command=run_command
    )
    (day_path / 'README.md').write_text(readme_content)
    print(f"Created: {day_str}/README.md")
    
    # Create solution file based on language
    templates = {
        'python': ('solution.py', PYTHON_TEMPLATE),
        'py': ('solution.py', PYTHON_TEMPLATE),
        'javascript': ('solution.js', JAVASCRIPT_TEMPLATE),
        'js': ('solution.js', JAVASCRIPT_TEMPLATE),
        'go': ('solution.go', GO_TEMPLATE)
    }
    
    if language.lower() in templates:
        filename, template = templates[language.lower()]
        solution_content = template.format(day=day_num)
        solution_file = day_path / filename
        solution_file.write_text(solution_content)
        # Make it executable
        os.chmod(solution_file, 0o755)
        print(f"Created: {day_str}/{filename}")
    else:
        print(f"Warning: Unknown language '{language}'. No solution file created.")
    
    # Create input files
    (day_path / 'input.txt').write_text('# Place your personal puzzle input here\n')
    print(f"Created: {day_str}/input.txt")
    
    (day_path / 'test_input.txt').write_text('# Example input from problem statement\n')
    print(f"Created: {day_str}/test_input.txt")
    
    print(f"\n✅ Successfully created template for Day {day_num}!")
    print(f"Next steps:")
    print(f"  1. cd {day_str}")
    print(f"  2. Update README.md with problem description")
    print(f"  3. Add your puzzle input to input.txt")
    print(f"  4. Implement the solution")
    
    return True


def main():
    if len(sys.argv) < 2:
        print("Usage: python create_day.py <day_number> [language]")
        print("\nExamples:")
        print("  python create_day.py 5          # Python template")
        print("  python create_day.py 12 js      # JavaScript template")
        print("  python create_day.py 3 go       # Go template")
        print("\nSupported languages: python, javascript (js), go")
        sys.exit(1)
    
    try:
        day_num = int(sys.argv[1])
        if not 1 <= day_num <= 25:
            print("Error: Day number must be between 1 and 25")
            sys.exit(1)
    except ValueError:
        print("Error: Day number must be an integer")
        sys.exit(1)
    
    language = sys.argv[2] if len(sys.argv) > 2 else 'python'
    
    create_day_directory(day_num, language)


if __name__ == '__main__':
    main()
