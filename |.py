from time import sleep

time = input("Enter Time: ")
type = type(time)

while time > 0:
  print(time)
  time -= 1
  sleep(1)
