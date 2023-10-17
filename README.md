# Transaction Tracker

Transaction Tracker is a Django-based web application that allows users to manage and track financial transactions with filtering and pagination capabilities.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python: This project is built with Python. You'll need Python 3.x installed on your system.
- PIP: PIP is a package manager for Python. It should come with Python, but ensure it's up to date.
- Virtual Environment (optional): It's recommended to create a virtual environment for this project to isolate its dependencies from other projects. You can install it using the following command:

    ```bash
    pip install virtualenv
    ```

## Installation

To install and run the Transaction Tracker app, follow these steps:

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/transaction-tracker.git
    ```

2. Navigate to the project directory:

    ```bash
    cd transaction-tracker
    ```

3. Create and activate a virtual environment (optional):

    ```bash
    virtualenv venv
    source venv/bin/activate
    ```

4. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

6. Load initial transactions from a JSON file (if available):

    ```bash
    python manage.py load_transactions transactions.json
    ```

    Replace `transactions.json` with the path to your JSON file.

7. Start the development server:

    ```bash
    python manage.py runserver
    ```

8. Access the Transaction Tracker web application in your web browser at `http://localhost:8000`.

## Usage

- The Transaction Tracker app allows you to manage financial transactions. You can:
  - View a list of transactions.
  - Create new transactions.
  - Update existing transactions.
  - Delete transactions.
  - Filter transactions by date and description.
  - Paginate through the transaction list.

- Access the app's API to interact with transactions programmatically using the `/api/transactions/` endpoint.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Create a pull request describing your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, feel free to contact the project maintainers:

- Your Name - [ahmedmabdirashid@gmail.com]
- Project Link: [GitHub Repository](https://github.com/AhmedARMohamed/transaction-tracker)
