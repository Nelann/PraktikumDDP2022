employees = [
  {
    "id": 1,
    "name": "John",
  },
  {
    "id": 2,
    "name": "Budi",
  },
  {
    "id": 3,
    "name": "Joko",
  },
]

for employee in employees:
  if (employee['id'] == 3):
    print(f"Hello my name is {employee['name']}")