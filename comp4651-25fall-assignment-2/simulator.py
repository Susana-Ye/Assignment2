"""
COMP4651 Assignment 2 - Part 4
Virtualization: Trap-and-Emulate Simulation
"""

def simulator():
    # Initialize the accumulator
    acc = 0
    
    # Read the file
    file = open('guest_program.txt', 'r')
    lines = file.readlines()
    file.close()
    
    # Process each instruction
    for line in lines:
        # Clean and parse the instruction
        line = line.strip()
        if not line:  # Skip empty lines
            continue
            
        parts = line.split()
        instruction = parts[0]
        
        # Handle non-privileged instructions (execute directly)
        if instruction == "add":
            if len(parts) < 2:
                print(f"Error: 'add' instruction requires a value")
                continue
            if parts[1].isdigit() or (parts[1][0] == '-' and parts[1][1:].isdigit()):
                value = int(parts[1])
                print(f"[Guest] Executing: add {value}")
                acc += value
            else:
                print(f"Error: invalid value for 'add' instruction: {parts[1]}")
                
        elif instruction == "print":
            print("[Guest] Executing: print")
            print(f"Accumulator value: {acc}")
        
        # Handle privileged instructions (trap and emulate)
        elif instruction == "scan_disk":
            print("[VMM] Trapped privileged instruction 'scan_disk', emulating...")
            # In a real VMM, this would perform safe disk I/O emulation
            # For this simulation, we just log the trap
            
        elif instruction == "halt":
            print("[VMM] Trapped privileged instruction 'halt'. Halting guest.")
            # Stop processing further instructions
            break
            
        else:
            print(f"Unknown instruction: {instruction}")

if __name__ == "__main__":
    simulator()