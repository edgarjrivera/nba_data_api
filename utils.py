import time
from flask import current_app, Response

def get_response_metrics(response: Response, start_time: float):
    """
    Logs the size of the response and the time taken to process the request.

    Args:
        response (Response): The Flask response object.
        start_time (float): The start time of the request.
    """
    try:
        # ✅ Measure response size
        response_size_kb = len(response.get_data()) / 1024  # Convert bytes to KB

        # ✅ Calculate execution time
        execution_time = time.time() - start_time  # Time in seconds

        # ✅ Log response size and execution time
        current_app.logger.info(
            f"Response Size: {response_size_kb:.2f} KB | Execution Time: {execution_time:.4f} seconds"
        )

    except Exception as e:
        current_app.logger.error(f"Error calculating response metrics: {e}")
