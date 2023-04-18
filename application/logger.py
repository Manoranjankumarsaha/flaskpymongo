import os
from logging.config import dictConfig

from application import app
from flask import request 

# if app.debug:
    # app.logger.propagate = False
        
log_file = os.path.join(os.getcwd(), 'myapp.log')
LOGGING_CONFIG={
        "version": 1,
        'disable_existing_loggers': False,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] [%(levelname)s | %(module)s] %(message)s",
                "datefmt":"%Y-%m-%d, %H:%M:%S %Z",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": "app.log",
                "formatter": "default",
            },
        },
        "root": {
                "level": "DEBUG", 
                "handlers": ["console", "file"]
                },
    }
dictConfig(LOGGING_CONFIG)


# Define a before request function to log incoming requests
@app.before_request
def log_request_info():
    app.logger.info('Request Method: %s', request.method)
    app.logger.info('Request URL: %s', request.url)
    headers = '\n'.join(f'{key}: {value}' for key, value in request.headers.items())
    app.logger.info('Request Headers:\n%s', headers)

    if request.method == 'POST' and request.headers.get('Content-Type') == 'application/json':
        request_data = request.get_data().decode('utf-8')
        app.logger.info('Request Body: %s', request_data)
    if request.method == 'PUT' and request.headers.get('Content-Type') == 'application/json':
        request_data = request.get_data().decode('utf-8')
        app.logger.info('Request Body: %s', request_data)
    
# Define an after request function to log outgoing responses
@app.after_request
def log_response_info(response):
    app.logger.info('Response: %s', response.status_code)
    # Check if the response is successful and not empty
    if response.status_code == 200:    
        response_data = response.get_data().decode('utf-8')
        app.logger.info('Response Body: %s', response_data)
    return response
    
# Define an error handler to log unhandled exceptions    
@app.errorhandler(Exception)
def internal_server_error(error):
    response = getattr(error, 'response', None)
    if response is not None:
        app.logger.info('Error %s: %s - Response: %s', response.status_code, str(error), response.get_data())
    else:
        app.logger.error('Unhandled exception: %s', str(error), exc_info=True)
        app.logger.exception('An error occurred: %s', (error))
        app.logger.error(f"{request.method} {request.url}: {error}")
    return 'An error occurred: ' + str(error), 500


# app.logger.debug('This is a debug message')
# app.logger.info('This is an info message')
# app.logger.warning('This is a warning message')
# app.logger.error('This is an error message')
# app.logger.critical('This is a critical message')