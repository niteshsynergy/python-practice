import time

file_path = r"C:\Users\Rahul Kumar\Desktop\serviceProvider.txt"

try:
    with open(file_path, 'r+', encoding='utf-8') as statusFile:
        # Step 1: Read original content
        original_content = statusFile.read()

        # Step 2: Replace file content with "TQ."
        statusFile.seek(0)  # Move cursor to the beginning
        statusFile.write("TQ.")  # Overwrite with new content
        statusFile.truncate()  # Remove extra characters if any

    # Step 3: Read new content & print
    with open(file_path, 'r', encoding='utf-8') as statusFile:
        updated_content = statusFile.read()
        print("\n📌 Updated File Content:\n", updated_content)

    # Simulating rollback delay
    time.sleep(3)  # Wait for 3 seconds before rolling back

    # Step 4: Restore original content (Rollback)
    with open(file_path, 'w', encoding='utf-8') as statusFile:
        statusFile.write(original_content)

    print("\n✅ Rollback Successful! File content restored.")

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
