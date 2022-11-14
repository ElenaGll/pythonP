def sum_of_intervals(intervals):
    intervals.sort()
    result = 0
    for i in intervals:
        result += i[1] - i[0]
        break
    for i, interval in enumerate(intervals[:-1]):
        if interval[1] < intervals[i + 1][0]:
            result += intervals[i + 1][1] - intervals[i + 1][0]
        elif interval[1] > intervals[i + 1][0]:
            if interval[1] > intervals[i + 1][1]:
                continue
            elif interval[1] < intervals[i + 1][1]:
                result += intervals[i + 1][1] - interval[1]
    return result
