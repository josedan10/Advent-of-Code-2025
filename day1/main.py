# The dial starts in 50.
# The dial goes from 0 to 99.
# If the dial is at 0, the previous number is 99.
# If the dial is at 99, the next number is 0.
# The input file contains lines with a direction (R or L) and a count.
# First part: Count how many times the dial is 0.
# Second part: Count how many times the dial crosses 0.

def move_to_right(dial, count):
  new_dial = dial + count
  crossed_zero_times = 0 

  if new_dial > 99:
    crossed_zero_times += count // 100
    new_dial = new_dial % 100

    # Check rest
    rest = count - crossed_zero_times * 100

    if dial + rest > 99:
      crossed_zero_times += 1

    # print(f'Crossed zero going right, new_dial: {new_dial}')

  return new_dial, crossed_zero_times



def move_to_left(dial, count):
  new_dial = dial - count
  crossed_zero_times = 0 

  if new_dial == 0:
    crossed_zero_times += 1

  if dial == 0:
    crossed_zero_times -= 1

  while new_dial < 0:
    new_dial += 100
    crossed_zero_times += 1
    # print(f'Crossed zero going left, new_dial: {new_dial}')

  if new_dial == 0 and count > 99:
    crossed_zero_times += 1

  return new_dial, crossed_zero_times

def move_dial(dial, direction, count):

  if direction == 'R':
    new_dial, crossed_zero_times = move_to_right(dial, count)

  else:
    new_dial, crossed_zero_times = move_to_left(dial, count)

  if count > 99 and direction == 'L':
    print(f'Moved from {dial} to {new_dial} going {direction}{count}, crossed zero {crossed_zero_times} times')

  return new_dial, crossed_zero_times


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
      dial, crossed_zero_times = move_dial(dial, direction, count)

      count_zeros += crossed_zero_times

      # if (dial == 0):
        # count_zeros += 1


  print(f'The final position of the dial is: {dial}')
  # print(f'The number of times the dial landed on 0 is: {count_zeros}')
  print(f'The number of times the dial crossed 0 is: {count_zeros}')

if __name__ == '__main__':
  main()