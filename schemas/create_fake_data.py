import csv
import random

from faker import Faker

from schemas.models import DataSchemas


def create_fake_data(rows, pk, data_set):
    dataschema = DataSchemas.objects.get(id=pk)

    head = []
    if dataschema.full_name:
        head.append(dataschema.full_name)
    if dataschema.age:
        head.append(dataschema.age)
    if dataschema.phone_number:
        head.append(dataschema.phone_number)
    if dataschema.company:
        head.append(dataschema.company)
    if dataschema.email:
        head.append(dataschema.email)

    fake = Faker("en_US")
    fake_data = []
    for _ in range(rows):
        person = []
        if dataschema.full_name:
            person.append(fake.name())
        if dataschema.full_name:
            person.append(fake.random_int(min=18, max=60, step=1))
        if dataschema.phone_number:
            person.append(fake.phone_number())
        if dataschema.company:
            person.append(fake.company())
        if dataschema.email:
            person.append(fake.email())

        fake_data.append(person)

    random_number = random.randrange(0, 100, 1)
    name = f"result_csv/people_fake_data_{dataschema.title}_{random_number}.csv"

    with open(name, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(head)
        writer.writerows(fake_data)

    data_set.status = "Success"
    data_set.create_dataschemas = True
    data_set.rows = rows
    data_set.url = name
    data_set.save()
