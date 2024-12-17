import requests

username='student1'
password='funtik123'

base_url = 'http://127.0.0.1:8000/api/'
url = f'{base_url}courses/'
available_courses = []
while url is not None:
    print(f'Loading courses from {url}')
    r = requests.get(url)
    # print(r)
    response = r.json()
    url = response['next']
    courses = response['results']
    available_courses += [course['title'] for course in courses]
print(f'Available courses: {", ".join(available_courses)}')

for course in courses:
    course_id = course['id']
    course_title = course['title']
    url=f'{base_url}courses/{course_id}/enroll/'
    print(url)
    r = requests.post(
        url,
        auth=(username, password)
    )
    print(r)
    if r.status_code == 200:
        print(f'Successfully enrolled in {course_title}')