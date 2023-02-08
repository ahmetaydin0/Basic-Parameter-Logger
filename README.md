## GET Request with Incrementing Parameter
#### This script sends GET requests to a URL with an incrementing parameter. The response of each request is written to a text file.

### Requirements
- Python 3
- requests library

### How to Run
- Clone the repository or download the main.py file.
- Install the required library.
```sh
pip install requests
```
- Replace `http://example.com` in the code with the actual URL to send the GET requests to.
- Replace `param1` with the actual parameter to be incremented in the GET request.
- Replace 1 and 10 with the start and end values of the parameter, respectively.
- Run the script
```sh
python main.py
```
- The responses of the GET requests will be written to an output.txt file in the same directory as the script.

> Note: The output.txt file will be overwritten each time the script is run. If you want to save multiple sets of responses, rename the file before running the script again or change the file name in the code.
