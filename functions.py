import subprocess


def fetch(url: str):
    result = subprocess.run(["wget", "-qO-", url], capture_output=True, text=True)

    response = result.stdout
    return response, 200


def fetch_cities():
    return fetch("https://sisusimulator.com.br/api/searchcity/")


def fetch_colleges(uf: str, city: str):
    return fetch(f"https://sisusimulator.com.br/api/cidade/{uf}/{city}")


def fetch_courses(college: str, campus: str):
    return fetch(f"https://sisusimulator.com.br/api/universidade/{college}/{campus}")


def fetch_course(course_id: str):
    return fetch(f"https://sisusimulator.com.br/api/curso/{course_id}")
