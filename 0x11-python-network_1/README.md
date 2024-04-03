0x11. Python - Network #1

Resources
Read or watch:

HOWTO Fetch Internet Resources Using urllib Package
Quickstart with Requests package
Requests package

General
How to fetch internet resources with the Python package urllib
How to decode urllib body response
How to use the Python package requests #requestsiswaysimplerthanurllib
How to make HTTP GET request
How to make HTTP POST/PUT/etc. request
How to fetch JSON resources
How to manipulate data from an external service

Both forms of passing parameters to a GET request in requests are quite similar in terms of functionality, but the one you provided with params is more explicit and clearer. Here's why it might be more recommended for a total beginner:

Clarity: Using the params parameter explicitly indicates that you're passing parameters in the URL query string. This makes it clear what the purpose of the payload dictionary is.

Consistency: The params parameter is specifically designed for passing parameters in GET requests. Beginners might find it easier to remember this syntax, leading to more consistent code.

Readability: The use of params makes the code more readable, especially for someone who might not be familiar with the requests library. It clearly communicates the intention of passing parameters to the URL.

Convenience: params automatically handles URL encoding of the parameters, ensuring that special characters are properly encoded. This convenience can be helpful for beginners who might not be familiar with URL encoding.

Given these reasons, using the params parameter is generally recommended for beginners as it provides a clear, consistent, and readable way to pass parameters in a GET request.



User
Requests package


The requests package in Python is a widely used library for making HTTP requests. It provides a simple and elegant way to interact with web services and APIs. Below is a brief overview of its key features and functionalities:

Simplicity: requests offers a straightforward API that abstracts away the complexities of HTTP requests, making it easy to use even for beginners.

HTTP Methods: It supports various HTTP methods such as GET, POST, PUT, DELETE, PATCH, etc., allowing you to interact with web resources in different ways.

Easy Installation: You can install requests easily using pip, the Python package manager:
