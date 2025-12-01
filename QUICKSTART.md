# Quick Start Guide

Welcome to the Advent of Code 2025 repository! This guide will help you get started quickly.

## 🚀 Creating a New Day's Solution

### Using the Template Generator (Recommended)

The easiest way to create a new day is using the `create_day.py` script:

```bash
# Create Day 3 with Python template
python create_day.py 3

# Create Day 5 with JavaScript template
python create_day.py 5 js

# Create Day 10 with Go template
python create_day.py 10 go
```

This will automatically create:
- `dayXX/` directory
- `README.md` with problem template
- Solution file with boilerplate code
- `input.txt` for your puzzle input
- `test_input.txt` for example input

### Manual Setup

If you prefer to create files manually:

1. Create a folder: `mkdir dayXX`
2. Copy template files from `day01/`
3. Update the files with your solution

## 📝 Solving a Problem

1. **Get your puzzle input:**
   - Visit https://adventofcode.com/2025/day/X
   - Copy your personal puzzle input to `dayXX/input.txt`
   - Copy the example input to `dayXX/test_input.txt`

2. **Update the README:**
   - Add the problem title
   - Describe parts 1 and 2
   - Note your approach

3. **Implement your solution:**
   - Fill in the `part1()` and `part2()` functions
   - Test with example input first
   - Run with your personal input

4. **Run your solution:**
   ```bash
   cd dayXX
   python solution.py    # For Python
   node solution.js      # For JavaScript
   go run solution.go    # For Go
   ```

## ✅ Testing Your Solution

1. First, test with the example input:
   ```python
   # Temporarily change in your solution file
   data = read_input('test_input.txt')
   ```

2. Verify the output matches the example result

3. Switch back to your personal input:
   ```python
   data = read_input('input.txt')
   ```

## 📊 Updating Progress

After completing a day, update the progress table in the main `README.md`:

```markdown
| [Day X](dayXX/) | ⭐ | ⭐ | Python | Used dynamic programming |
```

## 💡 Tips

- **Start simple:** Get part 1 working before thinking about part 2
- **Use test input:** Always verify with example input first
- **Read carefully:** Problem statements can be tricky
- **Don't peek:** Try to solve it yourself before looking at hints
- **Have fun:** It's okay to get stuck - learning is the goal!

## 🔗 Useful Links

- [Advent of Code 2025](https://adventofcode.com/2025)
- [r/adventofcode](https://www.reddit.com/r/adventofcode/) - Community discussions
- [Advent of Code Wiki](https://www.reddit.com/r/adventofcode/wiki/)

## 🆘 Need Help?

- Check the problem's example carefully
- Try a smaller test case
- Draw out the problem on paper
- Search for hints on r/adventofcode (after attempting!)

Happy Coding! 🎄
