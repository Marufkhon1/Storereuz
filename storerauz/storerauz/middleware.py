import time

class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Start timing the request processing
        start_time = time.time()

        # Log request information
        self.log_request_info(request)

        # Process the request
        response = self.get_response(request)

        # Log response information
        self.log_response_info(request, response, start_time)

        return response

    def log_request_info(self, request):
        print(f"\nRequest Method: {request.method}")
        print(f"Path: {request.path}")
        if request.user.is_authenticated:
            print(f"User: {request.user}")
        else:
            print("User: Anonymous User")

    def log_response_info(self, request, response, start_time):
        end_time = time.time()
        execution_time = end_time - start_time

        print(f"\nResponse Status Code: {response.status_code}")
        print(f"Execution Time: {execution_time:.6f} seconds")

        if 'Content-Length' in response:
            print(f"Response Content Length: {response['Content-Length']} bytes")

        print("\n" + "=" * 40)