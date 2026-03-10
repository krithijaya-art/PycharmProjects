def check_temperature(temperature):
    if temperature > 90:
        return "Stop Immediately"
    else:
        if temperature > 70:
            return "Cooling Needed"
        else:
            return "OK"

def monitor_machine(temperature):
    status = check_temperature(temperature)
    print(f"Temperature: {temperature} o C")
    print(f"Machine status: {status}")
    return status
