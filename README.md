Hi, This is one of my projects. The name of a project is the Weather Order System. 
Main aim of this project is manage order delivery status based on weather conditions in multiple cities, which customers have ordered. 

Initially I created an virtual environment for this project so that installed libraries can only accessible within this project, instead of making it global.

Then I created following files:

  1. .env file -->  To store API Key in a secure way.
  3. main.py   -->  To write actual python script to develop this project.
  4. orders.json --> To store orders data in json format

I imported the needed packages for this project:
  --> json = to work with json data, to convert json data to python data like dictionary or list.
  --> asyncio = used for asynchronus programming or doing parallel tasks.
  --> aiohttp = used to make API requests asynchronusly.
  --> requests = To make one by one API call. 
  --> os = Used to interact with system environment.
  --> load_dotenv = Used to load .env file into our program.

I tried this project in two ways:
  1. Using requests.get(), to make one by one API call, slow and blocking problem
  2. Using asyncio.gather(), to make multiple API calls, fast, no blocking

I wrote function for each and every operation, where each function has it's own functionality, improves code readability so that 
other developers can easily understand, and it reduces time complexity during runtime.

First, I wrote code to make one by one API call, using requests.get() inside weather_order_json() function. 
Then, I wrote code to make multiple API calls, using asynchronus programming. 

For both, update_order_data() is common to update order delivery status and generate AI type apology message to the customer by specifying exact reason for delay.

I handled runtime excptions using try and except block, so that program flow goes smoothly. Even if requested city is not found.

I created order_updated.json file using file handling inside the function to show the updated status.

I attached project related files below:



