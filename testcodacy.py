import os
import sqlite3
import hashlib
import base64

# --- 1. SECURITY RISK: SQL INJECTION ---
# Codacy's Bandit tool flags string formatting in SQL queries as a high risk.
def get_user_data(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # RISK: Using f-strings or % for SQL is a major vulnerability.
    query = f"SELECT * FROM users WHERE id = '{user_id}'" 
    cursor.execute(query)
    return cursor.fetchone()

# --- 2. SECURITY RISK: COMMAND INJECTION ---
# Using os.system with unsanitized input is a critical risk.
def ping_host(host_address):
    # RISK: An attacker could pass "8.8.8.8; rm -rf /"
    os.system("ping -c 1 " + host_address)

# --- 3. SECURITY RISK: WEAK CRYPTOGRAPHY ---
# Using MD5 is flagged as an insecure hashing algorithm.
def insecure_hash(data):
    # RISK: MD5 is cryptographically broken and considered a risk.
    return hashlib.md5(data.encode()).hexdigest()

# --- 4. CODE COMPLEXITY: HIGH CYCLOMATIC COMPLEXITY ---
# Functions with too many nested decisions trigger "Complexity" warnings.
def overly_complex_logic(a, b, c, d, e):
    # RISK: Deep nesting (more than 4-5 levels) is a maintainability risk.
    if a > 0:
        if b > 0:
            for i in range(c):
                if d:
                    while e > 0:
                        if i % 2 == 0:
                            print("Too many branches!")
                        e -= 1
                else:
                    return "Deeply nested"
    return "Done"

# --- 5. ERROR PRONE: MUTABLE DEFAULT ARGUMENTS ---
# A classic Python pitfall often flagged by Pylint/Ruff on Codacy.
def add_to_list(val, my_list=[]):
    # RISK: The same list object is reused across all function calls.
    my_list.append(val)
    return my_list
