from collections import Counter

def least_interval(tasks, n):
    task_counts = Counter(tasks)
    max_frequency = max(task_counts.values())
    count_max_frequency = sum(
        1 for task in task_counts
        if task_counts[task] == max_frequency
    )
    frame_length = (max_frequency - 1) * ( n + 1) + count_max_frequency
    total_tasks = len(tasks)
    return max(total_tasks, frame_length)

if __name__ == "__main__":
    tasks = ["A","A","A", "B","B","B"]
    n = 3
    print(least_interval(tasks, n))