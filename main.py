import requests

def main():
    # URL to send GET request to
    url = "http://example.com"

    # Parameter to be incremented in the GET request
    param = "param1"

    # Start value of the parameter
    start_value = 1

    # End value of the parameter
    end_value = 10

    # Loop through values of the parameter
    for i in range(start_value, end_value + 1):
        # Construct the full URL with the parameter and its value
        request_url = url + "?" + param + "=" + str(i)

        # Send the GET request
        response = requests.get(request_url)

        # Write the response to a text file
        with open("output.txt", "a") as f:
            f.write(response.text + "\n")

if __name__ == "__main__":
    main()
