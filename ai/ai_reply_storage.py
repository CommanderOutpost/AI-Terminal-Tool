import redis


class RedisDatabase:
    def __init__(self, host="localhost", port=6379, db=0):
        # Connect to the Redis server
        self.redis_db = redis.StrictRedis(
            host=host, port=port, db=db, decode_responses=True
        )

    def add_item(self, key, value):
        # Add an item to the Redis database
        self.redis_db.set(key, value)
        print(f"Added {key}: {value} to the database.")

    def remove_item(self, key):
        # Remove an item from the Redis database
        if self.redis_db.exists(key):
            self.redis_db.delete(key)
            print(f"Removed {key} from the database.")
        else:
            print(f"{key} not found in the database.")


if __name__ == "__main__":
    main()
