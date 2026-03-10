import time
import random

# Add Machine Temperature
# temperature = 85

print("Warehouse Monitoring System:")
print("============================")

try:
    while True:
        #Simulated sensor temperature reading
        temperature = random.randint(60,105)
        print("Current Machine Temperature:", temperature)

        # Decision using if and else
        if temperature > 90:
            status = "Stop immediately"
        else:
            if temperature > 70:
                status = "Machine needs cooling"
            else:
                status = "OK"

        print("Machine status:", status)

        # wait 3 seconds before next reading
        time.sleep(3)

except KeyboardInterrupt:
    print("\n Monitoring stopped by user.")
