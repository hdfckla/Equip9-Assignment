from bisect import bisect_left, bisect_right

def preprocess_maintenance_logs(maintenance_logs):
    # Sort logs by date
    maintenance_logs.sort(key=lambda x: x[1])
    
    # Extract dates and cumulative sums
    dates = [log[1] for log in maintenance_logs]
    cumulative_sums = [0] * len(maintenance_logs)
    cumulative_sums[0] = maintenance_logs[0][2]
    
    for i in range(1, len(maintenance_logs)):
        cumulative_sums[i] = cumulative_sums[i - 1] + maintenance_logs[i][2]
    
    return dates, cumulative_sums

def query_total_cost(dates, cumulative_sums, start_date, end_date):
    left_idx = bisect_left(dates, start_date)
    right_idx = bisect_right(dates, end_date) - 1
    
    if left_idx > right_idx:
        return 0  # No records in the range
    
    return cumulative_sums[right_idx] - (cumulative_sums[left_idx - 1] if left_idx > 0 else 0)

def maintenance_log_analysis(maintenance_logs, queries):
    dates, cumulative_sums = preprocess_maintenance_logs(maintenance_logs)
    
    return [query_total_cost(dates, cumulative_sums, start, end) for start, end in queries]

# Example usage
maintenance_logs = [(101, "2024-01-01", 500), (102, "2024-01-10", 300), (101, "2024-01-15", 700)]
queries = [("2024-01-01", "2024-01-10"), ("2024-01-01", "2024-01-15")]

print(maintenance_log_analysis(maintenance_logs, queries))
