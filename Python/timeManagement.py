minute = int(input("What Minute do we have?"))
hour = int(input("What hour?"))
second = int(input("What minute?"))


if second == 59:
    second = 0
    minute += 1
    if minute == 60:
        minute = 0
        hour += 1
        if hour == 24:
            hour = 00
else:
    second += 1
print(f"The time is: {hour:02}:{minute:02}:{second:02}")
