"""class PrintJob:
    def __init__(self, name, arrival_time, pages):
        self.name = name
        self.arrival_time = arrival_time
        self.pages = pages


def simulate_fcfs(jobs):
    # sort by arrival time
    jobs.sort(key=lambda job: job.arrival_time)

    current_time = 0
    completion_time = []

    for job in jobs:
        if current_time < job.arrival_time:
            current_time = job.arrival_time
        start_time = current_time
        end_time = current_time + job.pages
        completion_time.append((job.name, start_time, end_time))
         current_time = end_time
    return completion_time


def main():
    jobs = [PrintJob("A", 0, 10), PrintJob("B", 10, 15), PrintJob("C", 3, 3)]
    completion_time = simulate_fcfs(jobs)

    print("job completion Time")
    for job_name, start_time, end_time in completion_time:
        print(f"Job{job_name}:start time={start_time}s, end time={end_time}s")
    total_time = completion_time[-1][2]
    print(f"total time to complete all jobs:{total_time} minutes")


if __name__ == "__main__":
    main()"""

# --------------------------------------------------------------------------------------------------------------------------------------------

# program 2
"""class Task:
    def __init__(self, name, execution_time):
        self.name = name
        self.execution_time = execution_time

 
def simulate_sjf(tasks):
    # Sort tasks by their execution time (Shortest Job First)
    tasks.sort(key=lambda task: task.execution_time)

    current_time = 0
    completion_times = []
    for task in tasks:
        start_time = current_time
        end_time = start_time + task.execution_time
        completion_times.append((task.name, start_time, end_time))

        # Update current time to the end time of the current task
        current_time = end_time
    return completion_times


def main():
    # Define the tasks
    tasks = [
        Task("A", 3),
        Task("B", 5),
        Task("C", 7),
        Task("D", 4)
    ]

    completion_times = simulate_sjf(tasks)

    print("Task Completion Time:")
    for task_name, start_time, end_time in completion_times:
        print(f"Task {task_name}: Start Time = {start_time}h, End Time = {end_time}h")

    total_time = completion_times[-1][2]
    print(f"Total time to complete all tasks: {total_time} hours")


if __name__ == "__main__":
    main()
"""

# -----------------------------------------------------------------------------------------------------------------------------------------
# program 3
"""from collections import deque


def round_robin_scheduling(order_times, time_quantum):
    
    queue = deque((i, time) for i, time in enumerate(order_times))

    current_time = 0
    while queue:
        
        order_index, remaining_time = queue.popleft()
        processing_time = min(time_quantum, remaining_time)
        remaining_time -= processing_time
        current_time += processing_time

       
        if remaining_time > 0:
            queue.append((order_index, remaining_time))

    return current_time


# Input: Processing times for each order
order_times = [5, 3, 8, 6]
time_quantum = 5

# Calculate total time required using Round Robin scheduling
total_time = round_robin_scheduling(order_times, time_quantum)
print(f"Total time required to complete all orders: {total_time} minutes")"""

# -----------------------------------------------------------------------------------------------------------------------------------------------
# program 4
import heapq

patients = [
    ('Patient A', 1, 10),  # (Patient Name, Priority Level, Treatment Time)
    ('Patient B', 2, 8),
    ('Patient C', 3, 15),
    ('Patient D', 4, 5)
]


def priority_scheduling(patients):

    priority_queue = []
    for patient in patients:
        name, priority, treatment_time = patient
        heapq.heappush(priority_queue, (priority, name, treatment_time))

    current_time = 0
    order_of_treatment = []

    while priority_queue:
        _, name, treatment_time = heapq.heappop(priority_queue)
        current_time += treatment_time
        order_of_treatment.append((name, treatment_time, current_time))

    return order_of_treatment, current_time


# Run the Priority Scheduling algorithm
treatment_order, total_time = priority_scheduling(patients)

# Print the results
print("Order of treatment and completion time:")
for patient in treatment_order:
    name, treatment_time, completion_time = patient
    print(f"{name}: Treatment Time = {treatment_time} minutes, Completion Time = {completion_time} minutes")

print(f"\nTotal time required to treat all patients: {total_time} minutes")
# -----------------------------------------------------------------------------------------------------------------------------------------
# week 2
# program 1
"""system_processes = [
    ("Process A", 5),
    ("Process B", 3),
    ("Process C", 7)
]

user_processes = [
    ("Process D", 4),
    ("Process E", 2),
    ("Process F", 6)
]


def simulate_scheduling(system_processes, user_processes):
    # Initialize the current time
    current_time = 0

    # Schedule system processes
    print("Scheduling System Processes:")
    for process, time in system_processes:
        print(f"{process} starts at time {current_time} and finishes at time {current_time + time}")
        current_time += time

    # Schedule user processes
    print("\nScheduling User Processes:")
    for process, time in user_processes:
        print(f"{process} starts at time {current_time} and finishes at time {current_time + time}")
        current_time += time

    return current_time


# Run the scheduling simulation
total_time = simulate_scheduling(system_processes, user_processes)

print(f"\nTotal time required to complete all processes: {total_time} units")
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# program 2
high_priority_jobs = [
    ("Job A", 8),
    ("Job B", 5),
    ("Job C", 10)
]

low_priority_jobs = [
    ("Job D", 6),
    ("Job E", 3),
    ("Job F", 7)
]


def simulate_scheduling(high_priority_jobs, low_priority_jobs):
    # Initialize the current time
    current_time = 0

    # Schedule high priority jobs
    print("Scheduling High Priority Jobs:")
    for job, time in high_priority_jobs:
        print(f"{job} starts at time {current_time} and finishes at time {current_time + time}")
        current_time += time

    # Schedule low priority jobs
    print("\nScheduling Low Priority Jobs:")
    for job, time in low_priority_jobs:
        print(f"{job} starts at time {current_time} and finishes at time {current_time + time}")
        current_time += time

    return current_time


# Run the scheduling simulation
total_time = simulate_scheduling(high_priority_jobs, low_priority_jobs)

print(f"\nTotal time required to complete all jobs: {total_time} units")
# -------------------------------------------------------------------------------------------------------------------------------------------
# program 3
high_priority_jobs = [
    ("Job A", 15),
    ("Job B", 10),
    ("Job C", 20)
]

low_priority_jobs = [
    ("Job D", 5),
    ("Job E", 8),
    ("Job F", 3)
]


def simulate_print_job_scheduling(high_priority_jobs, low_priority_jobs):
    # Initialize the current time
    current_time = 0

    # Schedule high priority jobs
    print("Scheduling High Priority Print Jobs:")
    for job, time in high_priority_jobs:
        print(f"{job} starts at time {current_time} and finishes at time {current_time + time}")
        current_time += time

    # Schedule low priority jobs
    print("\nScheduling Low Priority Print Jobs:")
    for job, time in low_priority_jobs:
        print(f"{job} starts at time {current_time} and finishes at time {current_time + time}")
        current_time += time

    return current_time


# Run the scheduling simulation
total_time = simulate_print_job_scheduling(high_priority_jobs, low_priority_jobs)

print(f"\nTotal time required to complete all print jobs: {total_time} units")
# ------------------------------------------------------------------------------------------------------------------------------------
# program 4
high_priority_tasks = [
    ("Task A", 12),
    ("Task B", 8),
    ("Task C", 15)
]

low_priority_tasks = [
    ("Task D", 6),
    ("Task E", 4),
    ("Task F", 10)
]


def simulate_task_scheduling(high_priority_tasks, low_priority_tasks):
    # Initialize the current time
    current_time = 0

    # Schedule high priority tasks
    print("Scheduling High Priority Tasks:")
    for task, time in high_priority_tasks:
        print(f"{task} starts at time {current_time} and finishes at time {current_time + time}")
        current_time += time

    # Schedule low priority tasks
    print("\nScheduling Low Priority Tasks:")
    for task, time in low_priority_tasks:
        print(f"{task} starts at time {current_time} and finishes at time {current_time + time}")
        current_time += time

    return current_time


# Run the scheduling simulation
total_time = simulate_task_scheduling(high_priority_tasks, low_priority_tasks)

print(f"\nTotal time required to complete all tasks: {total_time} units")
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# program 5
high_priority_jobs = [
    ("Job A", 20),
    ("Job B", 15),
    ("Job C", 25)
]

medium_priority_jobs = [
    ("Job D", 10),
    ("Job E", 12),
    ("Job F", 8)
]

low_priority_jobs = [
    ("Job G", 5),
    ("Job H", 4),
    ("Job I", 6)
]


def simulate_job_scheduling(high_priority_jobs, medium_priority_jobs, low_priority_jobs):
    # Initialize the current time
    current_time = 0

    # Schedule high priority jobs
    print("Scheduling High Priority Jobs:")
    for job, time in high_priority_jobs:
        print(f"{job} starts at time {current_time} and finishes at time {current_time + time}")
        current_time += time

    # Schedule medium priority jobs
    print("\nScheduling Medium Priority Jobs:")
    for job, time in medium_priority_jobs:
        print(f"{job} starts at time {current_time} and finishes at time {current_time + time}")
        current_time += time

    # Schedule low priority jobs
    print("\nScheduling Low Priority Jobs:")
    for job, time in low_priority_jobs:
        print(f"{job} starts at time {current_time} and finishes at time {current_time + time}")
        current_time += time

    return current_time


# Run the scheduling simulation
total_time = simulate_job_scheduling(high_priority_jobs, medium_priority_jobs, low_priority_jobs)

print(f"\nTotal time required to complete all jobs: {total_time} units")


# week 3--------------------------------------------------------------------------------------------------------------------------------------

class StudentRecord:
    def __init__(self, name, student_id, grade, address):
        self.name = name
        self.student_id = student_id
        self.grade = grade
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, ID: {self.student_id}, Grade: {self.grade}, Address: {self.address}"


class SequentialFileAllocation:
    def __init__(self, block_size):
        self.disk_blocks = []
        self.fat = {}  # File Allocation Table
        self.block_size = block_size
        self.next_free_block = 0

    def add_record(self, student_record):
        record_size = self.calculate_record_size(student_record)

        if self.next_free_block >= len(self.disk_blocks):
            self.disk_blocks.append([""] * self.block_size)

        block_index = self.next_free_block
        block = self.disk_blocks[block_index]
        block[0] = student_record
        self.fat[student_record.student_id] = block_index
        self.next_free_block += 1
        return True

    def get_record(self, student_id):
        block_index = self.fat.get(student_id)

        if block_index is None:
            return None

        block = self.disk_blocks[block_index]
        for record in block:
            if isinstance(record, StudentRecord) and record.student_id == student_id:
                return record
        return None

    def calculate_record_size(self, student_record):
        return 1

    def print_disk_status(self):
        print("Disk Status:")
        for index, block in enumerate(self.disk_blocks):
            print(f"Block {index}:")
            for record in block:
                if isinstance(record, StudentRecord):
                    print(f" {record}")
                else:
                    print(" Empty")
        print(f"Next free block: {self.next_free_block}")


# Example Usage
block_size = 1
file_system = SequentialFileAllocation(block_size)

student_records =   [
    StudentRecord("John Doe", 101, 10, "123 Main Street"),
    StudentRecord("Jane Smith", 102, 11, "456 Elm Street"),
    StudentRecord("Michael Brown", 103, 9, "789 Oak Avenue")
]

for record in student_records:
    file_system.add_record(record)

file_system.print_disk_status()

student_id = 101
retrieved_record = file_system.get_record(student_id)
if retrieved_record:
    print(f"\nRetrieved Record for ID {student_id}:")
    print(retrieved_record)
else:
    print(f"\nRecord with ID {student_id} not found.")"""


# ----------------------------------------------------------------------------------------------------------------------------
