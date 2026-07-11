import random
import secrets
import uuid

random_integer = random.randint(1, 20)
print(random_integer)

list_numbers = []
for i in range(20):
    random_integer = random.randint(1, 20)
    list_numbers.append(random_integer)

print(list_numbers)

random_float = random.random()
print(random_float)
list_float = [random.random() for i in range(1, 11)]
print(list_float)

random_secure = secrets.token_bytes(3)
print(random_secure)

random_uuid = uuid.uuid4()
print(random_uuid)
