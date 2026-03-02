Digital Toolbox: Equipment Status Tracker
You're working as a systems support engineer for a digital lab maintenance team. Your company keeps an equipment inventory stored in nested dictionaries. Each category like "Tools", "Cables", and "Sensors" contains items marked either as "Working" or "Faulty".

Your job is to create a status report for each category:

Count how many items are working.

If a category has 0 working items, try to replace it with a backup dictionary.

If more than 1 faulty item is found in any category, immediately skip further checking using break.

Use continue to skip any irrelevant or unsupported item types in the future.

You will use everything you've learned so far: nested dictionaries, conditions, break/continue, and dictionary operations.



Program Output:

Too many faulty items in Cables, skipping further checks.

Final Equipment Status Report:

Tools: 2 items working

Cables: Replaced with backup

Sensors: 2 items working

