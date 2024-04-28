def banker_algorithm():
    # Get user input for number of processes, number of resources, and maximum resources
    num_processes = int(input("Enter the number of processes: "))
    num_resources = int(input("Enter the number of resources: "))
    max_resources = [int(i) for i in input("Enter the maximum resources available for each resource type: ").split()]

    print("\n-- Allocated resources for each process --")
    # Get allocated resources for each process
    currently_allocated = [[int(i) for i in input(f"Process {j + 1} allocation: ").split()] for j in range(num_processes)]

    print("\n-- Maximum resources needed for each process --")
    # Get maximum resources needed for each process
    max_need = [[int(i) for i in input(f"Process {j + 1} maximum need: ").split()] for j in range(num_processes)]

    # Calculate total allocated resources
    allocated_resources = [0] * num_resources
    for i in range(num_processes):
        for j in range(num_resources):
            allocated_resources[j] += currently_allocated[i][j]
    print(f"\nTotal allocated resources: {allocated_resources}")

    # Calculate total available resources
    available_resources = [max_resources[i] - allocated_resources[i] for i in range(num_resources)]
    print(f"Total available resources: {available_resources}\n")

    # Initialize running processes
    running_processes = [True] * num_processes
    count = num_processes
    while count != 0:
        safe_state = False
        # Check if a process can execute
        for i in range(num_processes):
            if running_processes[i]:
                can_execute = True
                # Check if process can execute safely
                for j in range(num_resources):
                    if max_need[i][j] - currently_allocated[i][j] > available_resources[j]:
                        can_execute = False
                        break
                if can_execute:
                    # Execute the process
                    print(f"Process {i + 1} is executing")
                    running_processes[i] = False
                    count -= 1
                    safe_state = True
                    for j in range(num_resources):
                        available_resources[j] += currently_allocated[i][j]
                    break
        if not safe_state:
            print("The processes are in an unsafe state.")
            break

        print(f"The system is in a safe state.\nAvailable resources: {available_resources}\n")

if __name__ == '__main__':
    banker_algorithm()
