# access_control.py

def audit_log(func):
    def wrapper(*args, **kwargs):
        print("\n" + "="*25)
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        print("="*25)
        return result
    return wrapper

def compute_access_level(control, artist_len):
    # Formula: (CONTROL_NUM * 3) + len(FAVORITE_ARTIST)
    return (control * 3) + artist_len

@audit_log
def validate_access(level, threshold):
    if level >= threshold:
        return "ACCESS GRANTED"
    return "ACCESS DENIED"