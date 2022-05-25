import requests
import os


# Сохранить на компьютере в папку(название родительская порода) по одной фотографии каждой подпороды
# у той породы у которых больше всего подпород


def get_folder_name(json):
    foldername = ''
    number_of_dogs = 0
    messages = json['message']
    subbreeds = []
    for message in messages:
        if len(messages[message]) > number_of_dogs:
            number_of_dogs = len(messages[message])
            foldername = message
            subbreeds = messages[message]
    return foldername, subbreeds


def get_random_request(foldername):
    url_random_request = 'https://dog.ceo/api/breed/' + foldername + '/images/random'
    return url_random_request


def make_dir(foldername):
    if not os.path.isdir(foldername):
        os.mkdir(foldername)


def get_file(foldername, subbreeds):
    for subbreed in subbreeds:
        url = 'https://dog.ceo/api/breed/terrier/' + subbreed + '/images/random'
        path = foldername + '/' + subbreed + '.jpg'
        with open(path, "wb") as file:
            data = requests.get(url).json()['message']
            data1 = requests.get(data)
            file.write(data1.content)
        #     while subbreed not in res_random:
        #         res_random = requests.get(url_random_request)
        #         continue
        #     else:
        #         file.write(res_random.content)


res_all = requests.get('https://dog.ceo/api/breeds/list/all')
json_all = res_all.json()
folder_name, sub_breeds = get_folder_name(json_all)
print(folder_name)
print(sub_breeds)
url_random_request = get_random_request(folder_name)
print(url_random_request)
make_dir(folder_name)
get_file(folder_name, sub_breeds)