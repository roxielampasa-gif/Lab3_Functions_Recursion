import grades
import access_control  # New Import

# 1. Setup Inputs
LAST_NAME = "Nacional"
STUDENT_ID = "TUPM-25-0363"
FAVORITE_ARTIST = "TAYLOR SWIFT" # Example

SEED_NUM = int(STUDENT_ID[-1])
CONTROL_NUM = max(1, SEED_NUM)
ARTIST_LEN = len(FAVORITE_ARTIST)

# 2. Execute Mission 1
level = access_control.compute_access_level(CONTROL_NUM, ARTIST_LEN)
threshold = CONTROL_NUM * 5
decision = access_control.validate_access(level, threshold)

# 3. Print Results
print(f"Computed Access Level: {level}")
print(f"Threshold: {threshold}")
print(f"Decision: {decision}")