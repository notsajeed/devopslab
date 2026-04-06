import os

# 1. SECURITY ISSUE: Hardcoded secret (Codacy flags this as a critical security risk)
# Source: https://docs.codacy.com/repositories/issues/
API_KEY = "sk-12345-not-a-real-key-but-flags-as-secret"

def calculate_average(numbers):
    """
    Function to show common issues:
    - Error prone: Division by zero risk
    - Style: Inconsistent naming
    """
    total = 0
    for n in numbers:
        total = total + n
    
    # 2. ERROR PRONE: Potential division by zero if 'numbers' is empty
    # Codacy often flags this as a "Bug Risk"
    average = total / len(numbers)
    return average

def main():
    # 3. UNUSED CODE: Variable defined but never used
    # Source: https://docs.codacy.com/v2.0/repositories/issues-view/
    unused_variable = 100
    
    # 4. STYLE ISSUE: Print statement without parentheses (if using older linters)
    # or mixing types in print (Error prone)
    nums = [10, 20, 30]
    print("The average is: " + calculate_average(nums))

    # 5. COMPLEXITY/DUPLICATION: Writing the same logic again instead of calling the function
    # Codacy tracks "Code Duplication" metrics
    vals = [5, 15, 25]
    t = 0
    for v in vals:
        t += v
    avg = t / len(vals)
    print(avg)

if __name__ == "__main__":
    main()
