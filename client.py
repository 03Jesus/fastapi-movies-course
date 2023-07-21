import requests

REVIEW_ID = 3
URL = f'http://localhost:8000/api/v1/reviews/{REVIEW_ID}'
# HEADERS = {'accpet': 'application/json'}
# QUERYSET = {'page': 1, 'limit': 1}

# response = requests.get(URL, headers=HEADERS, params=QUERYSET)
# print(response)

# if response.status_code == 200:
#     print('Petición realizada de forma exitosa')

#     if response.headers.get('content-type') == 'application/json':

#         reviews = response.json()
#         for review in reviews:

#             print(f"score: {review['score']} - {review['review']} ")


# REVIEW = {
#     'user_id': 1,
#     'movie_id': 1,
#     'review': 'Review creada con requests.',
#     'score': 5
# }

# response = requests.post(URL, json=REVIEW)

# if response.status_code == 200:
#     print('Reseña creada de forma exitosa')

# else:
#     print(response.content)

REVIEW = {
    'review': 'Review actualizada con requests.',
    'score': 4
}

response = requests.put(URL, json=REVIEW)

if response.status_code == 200:
    print('Reseña actualizada de forma exitosa')
    print(response.json())

else:
    print(response.content)
