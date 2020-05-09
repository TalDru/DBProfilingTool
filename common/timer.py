# Timer decorator

import time


def time_execution_length(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        exec_length = (end_time - start_time) * 1000  # In MS

        if 'metadata' in kwargs:
            # Add execution length to the metadata
            metadata = kwargs.get('metadata')
            if metadata is not None:
                metadata['exec_times'].append(exec_length)

        return result

    return wrapper
