Inventory Management System is a backend API built using Django Rest Framework for managing an inventory system. It provides endpoints to create, retrieve, update, and delete inventory items. The application uses PostgreSQL for the database and Redis for caching.

Content : 

1) Setup Instructions
2) API Documentation
3) Usage Examples
4) Testing
5) Contributing
6) License

Installation

1) Clone the repository:
    git clone https://github.com/KANISHK251/Inventory_Management.git
   cd Inventory_Management

 3) Install dependencies from requirements.txt:
    pip install -r requirements.txt

4) Set up the PostgreSQL database and Redis:
	•	Ensure PostgreSQL and Redis are installed and running.
	•	Create a PostgreSQL database and update the DATABASES settings in settings.py.

5) Apply database migrations:
   python manage.py migrate

6) Create a superuser (admin):
   python manage.py createsuperuser

7) Run the development server:
   python manage.py runserver
   

API Documentation

Endpoints:

1. Create Item
    Method: POST
    URL: /items/
    Body:
   {
   "name": "HeadPhone",
   "description": "Electronics",
   "quantity": 3,
   "price": "2999.99"
   }

   •	Response:
   {
  "id": 1,
  "name": "HeadPhone",
  "description": "Electronics",
  "quantity": 3,
  "price": "2999.99"
   }

2) Retrieve Item
    Method: GET
    URL: /items/{id}/
    Response:
   {
  "id": 1,
  "name": "HeadPhone",
  "description": "Electronics",
  "quantity": 3,
  "price": "2999.99"
   }

3) Update Item
   Method: PUT / PATCH
   URL: /items/{id}/
   Body: (for PUT)

   {
  "name": "SmartPhone",
  "description": "Electronics",
  "quantity": 4,
  "price": "34999.99"
   }

4) Delete Item
   Method: DELETE
   URL: /items/{id}/

Usage Examples

1. Creating an Item
   Use the following curl command or Postman to create a new inventory item.
   curl -X POST http://127.0.0.1:8000/items/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Laptop", "description": "Electronics", "quantity": 5, "price": "50000.00"}'

2. Retrieving an Item:
   curl -X GET http://127.0.0.1:8000/items/1/


Testing :

We can run the unit tests for this project using pytest. 

1.	Install pytest:
   pip install pytest

2. Run the tests :
   pytest

Contributing

If you’d like to contribute to this project:
  1.  Fork the repository.
	2.	Create a feature branch (git checkout -b feature-branch-name).
	3.	Commit your changes (git commit -m 'Add some feature').
	4.	Push to the branch (git push origin feature-branch-name).
	5.	Create a new Pull Request.

License

This project is licensed under the MIT License - see the LICENSE file for details.
