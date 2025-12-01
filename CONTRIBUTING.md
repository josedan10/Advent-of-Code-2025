# Contributing to Advent of Code 2025 Solutions

Thank you for your interest in contributing! This document provides guidelines for adding solutions to this repository.

## Structure Guidelines

Each day's solution should follow this structure:

```
dayXX/
├── README.md           # Problem description and approach
├── solution.[ext]      # Main solution file
├── input.txt          # Personal puzzle input (optional)
└── test_input.txt     # Example input from problem statement
```

## Adding a New Day's Solution

1. Create a new folder named `dayXX` where XX is the two-digit day number (e.g., `day01`, `day02`, ..., `day25`)

2. Copy the template structure from `day01/` as a starting point

3. Update the `README.md` with:
   - Problem title and link
   - Problem description (parts 1 and 2)
   - Your solution approach
   - Any interesting notes or observations

4. Implement your solution in your preferred language:
   - Use clear variable names
   - Add comments explaining complex logic
   - Include docstrings/comments for functions
   - Follow language-specific best practices

5. Update the progress table in the main `README.md`

## Code Style

- **Python**: Follow PEP 8 style guidelines
- **JavaScript**: Use modern ES6+ syntax
- **Go**: Follow standard Go formatting (gofmt)
- **Other languages**: Follow community-standard style guides

## Testing

- Include the example input from the problem in `test_input.txt`
- Verify your solution works with the example input
- Test with your personal input before committing

## Commit Messages

Use clear, descriptive commit messages:
- ✅ Good: "Add Day 5 solution using dynamic programming"
- ✅ Good: "Optimize Day 3 Part 2 with hash map"
- ❌ Bad: "Update files"
- ❌ Bad: "Day 5"

## Privacy

- **Do not** share your personal puzzle input publicly if you want to keep it private
- Consider adding `*/input.txt` to `.gitignore` if you prefer
- Test inputs from problem statements can be shared

## Multiple Solutions

Feel free to add multiple solution approaches:
- `solution_v1.py` - First approach
- `solution_v2.py` - Optimized version
- `solution_recursive.py` - Alternative approach

## Questions?

If you have questions or suggestions for improving this repository, feel free to open an issue!

Happy coding! 🎄
