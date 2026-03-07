def min_time_to_resolve_bugs(timeTaken, bugs):
    min_time = min(timeTaken)
    low = 1
    high = bugs * min_time
    answer = high
    
    while low <= high:
        mid = low + (high - low)// 2
        total_bugs_resolved = 0
        for time_per_bug in timeTaken:
            total_bugs_resolved += mid // time_per_bug

            if total_bugs_resolved >= bugs:
                break
        if total_bugs_resolved >= bugs:
            answer = mid
            high = mid -1
        else:
            low = mid + 1
    return answer

if __name__ == "__main__":
    timeTaken = [1,2,3]
    bugs = 5
    print(min_time_to_resolve_bugs(timeTaken, bugs))