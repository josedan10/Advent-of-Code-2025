# The dial starts in 50.
# The dial goes from 0 to 99.
# If the dial is at 0, the previous number is 99.
# If the dial is at 99, the next number is 0.

def move_dial(dial, direction, count):
  new_deal = 0

  if direction == 'R':
    # Sum
    new_dial = dial + count

    if new_dial > 99:
      new_dial = new_dial % 100

  else:
    # Subtract
    new_dial = dial - count

    while new_dial < 0:
      new_dial += 100

  return new_dial


def extract_data_from_file_line(line):
  direction = line[0]
  count = int(line[1:])

  return direction, count

def main():
  dial = 50

  count_zeros = 0

  with open('./input.txt', 'r') as file:
    for line in file:
      line = line.strip()
      direction, count = extract_data_from_file_line(line)
      dial = move_dial(dial, direction, count)

      if (dial == 0):
        count_zeros += 1

  print(f'The final position of the dial is: {dial}')
  print(f'The number of times the dial landed on 0 is: {count_zeros}')

if __name__ == '__main__':
  main()