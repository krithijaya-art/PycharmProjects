# -----------------------------
# Import deepcopy to safely copy nested dictionaries
# -----------------------------
import copy

# -----------------------------
# Equipment inventory of the lab
# Each category contains items with name and status
# -----------------------------
equipment_inventory = {
    "Tools": {
        "item1": {"name": "hammer", "status": "working"},
        "item2": {"name": "screwdriver", "status": "working"},
        "item3": {"name": "wrench", "status": "faulty"}
    },
    "Cables": {
        "item1": {"name": "USB", "status": "faulty"},
        "item2": {"name": "Fibre", "status": "faulty"},
        "item3": {"name": "Panel Wire", "status": "working"}
    },
    "Sensors": {
        "item1": {"name": "Temperature", "status": "working"},
        "item2": {"name": "Pressure", "status": "working"}
    }
}

# -----------------------------
# Backup inventory: default items if a category fails completely
# -----------------------------
backup_inventory = {
    "item1": {"name": "Backup Cable 1", "status": "working"}
}

# -----------------------------
# Final report to store working/faulty status per category
# -----------------------------
category_report = {}

# -----------------------------
# Loop through each category in the inventory
# -----------------------------
for category, items in equipment_inventory.items():

    # Counters to track working and faulty items
    working_count = 0
    faulty_count = 0

    # -----------------------------
    # Loop through each item in the current category
    # -----------------------------
    for item_id, details in items.items():

        # Defensive check: skip items that are not dictionaries
        if not isinstance(details, dict):
            continue  # skip to next item

        # Check the status safely using .get()
        status = details.get("status")

        if status == "working":
            working_count += 1
        elif status == "faulty":
            faulty_count += 1

        # -----------------------------
        # If more than 1 faulty item found, replace category with backup and stop checking further
        # -----------------------------
        if faulty_count > 1:
            category_report[category] = "Replaced with backup"
            # Use deepcopy so backup is independent
            equipment_inventory[category] = copy.deepcopy(backup_inventory)
            break  # stop checking items in this category

    # -----------------------------
    # This else runs only if the 'break' above did NOT trigger
    # -----------------------------
    else:
        if working_count == 0:
            # No working items → replace category with backup
            category_report[category] = "Replaced with backup"
            equipment_inventory[category] = copy.deepcopy(backup_inventory)
        else:
            # Otherwise, report how many items are working
            category_report[category] = f"{working_count} items working"

# -----------------------------
# Print final equipment status report
# -----------------------------
print("Final Equipment Status Report:")
for category, status in category_report.items():
    print(f"{category}: {status}")