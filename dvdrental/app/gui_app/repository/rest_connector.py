import requests

def getFilm(id):
    url = "http://localhost:8000/dvdrental/api/film/{id}/".format(id=id)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return "{}"
    # response.close() TODO

# TODO tworzenie jsona i zapis obiektu 
def putFilm(id, data, gui_model):
    res = json_builder(id, data, gui_model)
    url = "http://localhost:8000/dvdrental/api/action/film/"
    response = requests.put(url, data=res)

    if response.status_code != 200:
        print("put film error: ", response)
    return response.status_code == 200 

def json_builder(id: int, data: list, model):
    print(data)
    result = []
    for tl in data:
        name = tl[0]
        value = tl[1]
        if model[name].type == str:
            result.append('"' + name + '":"' + value + '"')
        elif model[name].type == int | model[name].type == float:
            result.append('"' + name + '":' + value + '')

    result.append('"id":' + str(id))
    
    return "{" + ",".join(result) + "}"
