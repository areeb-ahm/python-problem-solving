# Write function safe_read_config(filepath):

# Try opening file, read all lines.
# Return list of lines (stripped of \n), skip empty lines.
# If file doesn't exist, catch the exception, print "Config file not found: <filepath>", return empty list [].
# Use with statement.

def safe_read_config(filepath):
    try:
        with open(filepath, "r") as f:
            data = f.read().split("\n")
            return [line for line in data if line != ""]
    except FileNotFoundError:
        print(f"Config file not found: {filepath}")
        return []
    
print(safe_read_config("nonexistent.txt"))
print(safe_read_config("pr08_f1.txt"))