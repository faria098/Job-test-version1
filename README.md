
# Alert API

This is a simple REST API built using Flask for managing alerts. It allows users to create alerts with custom IDs and retrieve alerts by ID. This README provides an overview of the project, its structure, and how to use it.

## Table of Contents

- [Database](#database)
- [Endpoints](#endpoints)
- [Examples](#examples)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Database

This API uses SQLite as the database system for storing alert data. SQLite is a lightweight, serverless, and file-based database that is well-suited for small to medium-sized applications. It's chosen for its simplicity and portability.

The `alerts` table in the database has the following schema:

- `id` (INTEGER): An identifier for the alert.
- `message` (TEXT): The content of the alert message.
- `timestamp` (DATETIME): The timestamp when the alert was created.

## Endpoints

### Create or Update Alert

- **Endpoint:** `POST /alerts`
- **Description:** This endpoint allows users to create or update an alert. Users can specify a custom `id` in the request body. If the `id` exists, the alert with that ID will be updated with the new message. If the `id` does not exist, a new alert will be created.
- **Request Body (JSON):**
```json
{
  "id": 1, // Custom alert ID (optional)
  "message": "This is an alert message"
}



## Get Alert by ID

- **Endpoint:** `GET /alerts/{alert_id}`
- **Description:** This endpoint allows users to retrieve a specific alert by its ID.
- **Response (Success - HTTP 200 OK):**
```json
{
  "id": 1,
  "message": "This is an alert message",
  "timestamp": "2023-11-10 12:34:56"
}
```

## Get All Alerts

- **Endpoint:** `GET /alerts`
- **Description:** This endpoint allows users to retrieve all alerts.
- **Response (Success - HTTP 200 OK):**
```json
[
  {
    "id": 1,
    "message": "Alert 1",
    "timestamp": "2023-11-10 12:34:56"
  },
  {
    "id": 2,
    "message": "Alert 2",
    "timestamp": "2023-11-10 12:35:01"
  }
]
```

## Examples

### Create a New Alert

To create a new alert with a custom ID, you can make a POST request to `/alerts` with the following JSON body:

```json
{
  "id": 1,
  "message": "This is a new alert"
}
```
The response will be:

```json
{
  "message": "Alert with ID 1 created successfully"
}
```



## Get Alert by ID

- **Endpoint:** `GET /alerts/{alert_id}`
- **Description:** This endpoint allows users to retrieve a specific alert by its ID.
- **Response (Success - HTTP 200 OK):**
```json
{
  "id": 1,
  "message": "This is an alert message",
  "timestamp": "2023-11-10 12:34:56"
}
```

## Get All Alerts

- **Endpoint:** `GET /alerts`
- **Description:** This endpoint allows users to retrieve all alerts.
- **Response (Success - HTTP 200 OK):**
```json
[
  {
    "id": 1,
    "message": "Alert 1",
    "timestamp": "2023-11-10 12:34:56"
  },
  {
    "id": 2,
    "message": "Alert 2",
    "timestamp": "2023-11-10 12:35:01"
  }
]
```

## Examples

### Create a New Alert

To create a new alert with a custom ID, you can make a POST request to `/alerts` with the following JSON body:

```json
{
  "id": 1,
  "message": "This is a new alert"
}
```
The response will be:

```json
{
  "message": "Alert with ID 1 created successfully"
}
```

### Update an Existing Alert

To update an existing alert with a custom ID, make a POST request to `/alerts` with the following JSON body:

```json
{
  "id": 1,
  "message": "This is an updated alert"
}
```
The response will be:

```json
{
  "message": "Alert with ID 1 updated successfully"
}
```

### Retrieve an Alert by ID

To retrieve an alert by its ID, make a GET request to `/alerts/{alert_id}` (e.g., `/alerts/1`). The response will contain the alert details.

### Retrieve All Alerts

To retrieve all alerts, make a GET request to `/alerts`. The response will contain a list of all alerts in the database.

## Usage

1. Clone this repository to your local machine.
2. Install Flask if not already installed: `pip install Flask`.
3. Initialize the SQLite database by running `python app.py` from the project root directory.
4. Run the Flask app: `python app.py`.
5. Use Postman or any HTTP client to interact with the API as described in the examples above.

## Contributing

Contributions are welcome! Please read the CONTRIBUTING.md file for details on how to contribute to this project.


