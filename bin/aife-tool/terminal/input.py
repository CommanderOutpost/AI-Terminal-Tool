# Import necessary modules
import sys
from ai.ai_reply_storage import RedisDatabase


# Define a cleanup function to handle interruptions (e.g., Ctrl+C)
def cleanup(signum, frame):
    # Create an instance of the RedisDatabase class
    redis_db = RedisDatabase()

    # Retrieve all data stored in the Redis database
    all_data = redis_db.get_all_data()

    # Print a message indicating an interruption and the deletion of AI memory
    print("\nInterruption detected. Deleting AI memory...")

    # Delete all data from the Redis database
    redis_db.delete_all_data()

    # Exit the program with status code 1
    sys.exit(1)
