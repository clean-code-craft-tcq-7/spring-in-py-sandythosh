def calculateStats(numbers):
  # implement the computation of statistics here and return the results
  avg = sum(numbers) / len(numbers) if numbers else float('nan')
  min_val = min(numbers) if numbers else float('nan')
  max_val = max(numbers) if numbers else float('nan')
  return {
      "avg": avg,
      "min": min_val,
      "max": max_val
  }
