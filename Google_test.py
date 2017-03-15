from google import google
num_page = 3
search_results = google.search("November 10 2016 atvi", num_page)
for result in search_results:
    print(result.description)