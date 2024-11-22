import re

def parse_log_message_regex(message_string):
    # Use regex to find all key-value pairs
    pattern = r'(\w+)="([^"]*)"'
    pairs = re.findall(pattern, message_string)
    print(pairs)
    
    # Convert to dictionary
    return dict(pairs)

# Test the function
message = 'message="Payment failed" transaction_id="TX789" amount="500.00" error_code="ERR_001" user_id="ABC123"'
parsed_dict = parse_log_message_regex(message)

# Print the resulting dictionary
print("\nParsed Dictionary (using regex):")
for key, value in parsed_dict.items():
    print(f"{key}: {value}")