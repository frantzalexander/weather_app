# Weather App Project Overview
The Weather SMS notification app sends a report of the morning weather. 

The program gathers data utilizing from the Openweather API. 

Then sends a text message to the user utilizing the Twilio Client API. 

# Objectives
- Gather Weather data from API
- Process JSON data
- Send SMS Message with weather report.

# Results
The program collects the data from the API. 

Then, checks the weather code of the first 11 hours of the day. 

Finally, it then sends a text message with the weather report. 

# Process
```mermaid
flowchart TD
start(((START)))
request[Request Data]
process[Process Data]
check[Checks Weather Code]
send[Sends SMS Report]
finish(((END)))
start --> request
request --> process
process --> check
check -->|Rain| send
check -->|Sunny| send
send --> finish
