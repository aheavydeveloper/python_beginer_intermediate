print(" a decorator factory—a function that accepts the argument and returns the actual decorator function.")
print("check the explainnation of this implementation in the txt file in the package")
# This is the "decorator factory." It takes the argument (count).
def repeat_message(count):
    # This is the actual decorator function, which takes the function to be decorated (func)
    def decorator(func):
        # This is the wrapper function that replaces the original function
        def wrapper(*args, **kwargs):
            # The decorator logic uses the 'count' argument from the factory
            result = func(*args, **kwargs)

            # Use a simple loop to repeat the result based on the 'count' argument
            for _ in range(count):
                print(f"Repeated Output: {result}")

            return result

        # Return the wrapper function
        return wrapper

    # Return the decorator function
    return decorator


# ----------------------------------------------------------------

# 2. Applying the Decorator
# The @ symbol calls repeat_message(3), which returns the actual decorator function.
# The decorator function then wraps the greet function.
@repeat_message(count=3)
def greet(name):
    """The original function that takes a string argument."""
    message = f"Hello, {name}!"
    print(f"Original Output: {message}")
    return message


# 3. Calling the Decorated Function
greet("Alex")