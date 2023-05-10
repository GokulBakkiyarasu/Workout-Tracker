# Exercise Tracker

This program is a simple exercise tracker that allows users to input their exercises and related data, and stores that information in a Google Sheet using the Sheety API. The program also makes use of the Nutritionix API to get additional nutritional information for the exercises entered by the user.

![Screenshot (20)](https://github.com/GokulBakkiyarasu/Workout-Tracker/assets/87391223/5749715b-7e10-4db2-86e1-c90b0d859f3a)


## Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/your_username/Workout-Tracker.git
   ```
2. Install dependencies:
   ```
   pip install requests
   ```
3. Set up your environment variables:
   - `APP_ID`: Your Nutritionix App ID
   - `API_KEY`: Your Nutritionix API Key
   - `TOKEN`: Your Sheety API Token
4. Run the program:
   ```
   main.py
   ```

## Usage

1. Enter your exercises:
   - Enter your exercise details in the prompt when prompted to do so.
   - Enter your gender, weight, height, and age.
2. View your exercise data:
   - Your exercise data will be displayed in the console.
3. View your exercise data in the Google Sheet:
   - The exercise data will also be stored in a Google Sheet that you can view.

## File structure

```
├── main.py        	      # Main program file
└── README.md                 # README file
```

## Functions

### Posting Exercise Data to Sheety

```python
for exercise in results["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response1 = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=header1)
    print(response1.json())
```

This function takes the exercise data obtained from the Nutritionix API and posts it to a Google Sheet using the Sheety API. It creates a dictionary `sheet_inputs` containing the exercise data, and then makes a `POST` request to the Sheety endpoint.

### Getting Exercise Data from the Nutritionix API

```python
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=API_ENDPOINT, json=parameters, headers=header)
results = response.json()
print(results)
```

This function sends a `POST` request to the Nutritionix API to get the exercise data. It creates a dictionary `parameters` containing the user's input and API credentials, and then sends a request to the API endpoint. The response is then parsed into a JSON object and printed to the console.

## API References

- [Nutritionix API](https://developer.nutritionix.com/docs/v2)
- [Sheety API](https://sheety.co/docs/requests)
## Contributing
Contributions to this project are welcome. To contribute, follow these steps:
1. Fork this repository
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Make and commit your changes (`git commit -am "Add new feature"`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a new Pull Request
## Find me on
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-Profile-informational?style=flat&logo=linkedin&logoColor=white&color=0D76A8)](https://www.linkedin.com/in/gokul-bakkiyarasu-531535251)
