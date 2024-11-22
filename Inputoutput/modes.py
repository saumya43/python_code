# Example of seek() and tell() methods in file handling
File = "load_balancer_log.log"
with open(File, 'w') as file:
    file.write("Hello World!\nPython Programming\nFile Handling Example")

# Reading and using seek() and tell()
with open(File, 'r') as file:
    # Initial position
    print(f"Initial position: {file.tell()}")  # Output: 0
    
    # Read first line
    print(f"First line: {file.readline().strip()}")
    print(f"After first line position: {file.tell()}")
    
    # Seek to beginning
    file.seek(0)
    print(f"After seek(0) position: {file.tell()}")
    
    # Read entire file
    content = file.read()
    print(f"After reading entire file position: {file.tell()}")
    
    # Seek from beginning (absolute position)
    file.seek(6)  # Go to 6th character
    print(f"Content after seek(6): {file.read(5)}")  # Should read "World"
    
    # Seek from current position (relative to current)
    file.seek(0)  # Go back to start
    file.read(6)  # Read "Hello "
    file.seek(5, 1)  # Move 5 positions forward from current
    print(f"Content after relative seek: {file.read(5)}")
    
    # Seek from end
    file.seek(0, 2)  # Go to end
    print(f"Position at end of file: {file.tell()}")
    
    # Seek backwards from end
    file.seek(-7, 2)  # Go 7 characters back from end
    print(f"Last word: {file.read()}")  # Should print "Example"

# Example with binary mode
with open(File, 'rb') as file:
    # In binary mode, seek can move to any position
    file.seek(-10, 2)  # Go 10 bytes back from end
    print(f"Last 10 bytes: {file.read().decode()}")
