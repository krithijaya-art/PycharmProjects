import array

seats = array.array('i',[101, 102, 103, 104, 105, 106, 107, 108])

# Print the total seat
print(seats)

try:
    guest_seat_old = 104
    idx = seats.index(guest_seat_old)
    seats[idx] = 110
    print(seats)
except ValueError:
    print("Seat not found")

first_four_seats = seats[:4]
print("The first four seats are:",first_four_seats)

last_three_seats = seats[-3:]
print("The last three seats are:", last_three_seats)

reserved = array.array('i',[102,106])
for seat in seats:
    if seat in reserved:
        print(f"Seat {seat} - reserved")
    else:
        print(f"Seat {seat} - not reserved")

start_seat = 105
def next_available(start_seat, seats, reserved):
    for seat in seats:                  # check every seat one by one
        if seat >= start_seat:          # is seat number big enough?
            if seat not in reserved:    # is it NOT reserved?
                return seat             # yes → return immediately
    return None                         # if nothing found

result = next_available(start_seat, seats, reserved)
print("Next available seat:", result)