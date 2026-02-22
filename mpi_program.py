from mpi4py import MPI

# Initialize communicator
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Master Process
if rank == 0:
    print("Master process is running...\n")

    # Receive results from all workers
    for i in range(1, size):
        message = comm.recv(source=i)
        print(f"Received from Process {message['rank']}")
        print(f"Assigned Task: {message['task']}")
        print(f"Computed Sum: {message['result']}\n")

    print("All worker processes completed.")

# Worker Processes
else:
    # Assign a data chunk based on rank
    task_number = rank
    data_chunk = list(range(rank * 10, rank * 10 + 5))

    # Simple computation
    computed_sum = sum(data_chunk)

    # Prepare message
    message = {
        "rank": rank,
        "task": f"Data chunk {task_number}: {data_chunk}",
        "result": computed_sum
    }

    # Send result to master
    comm.send(message, dest=0)
