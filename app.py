from bs4 import BeautifulSoup
import detail
import requests


url = "https://savollar.islom.uz/"

search_question = input("Enter your question: ")

def research_question(keywords: str):
    params = {'words': keywords, 'page': 1}  # Add 'page' parameter to start from the first page

    response = requests.get(url + 'search', params=params)  # Corrected to hit the search endpoint

    # Checking the status of the request
    if response.status_code == 200:
        # Parse the response content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all elements with the class 'question'
        results = soup.find_all('div', class_='question')
        
        # Print the search results
        if results:
            for result in results:
                title_span = result.find('span', class_='word_search')
                a_href = result.find('a').get('href')
                question_id = a_href.split('/')[-1]
                answer = detail.get_detailed_answer(question_id)

                print(answer)
            
                if title_span:
                    print(title_span.get_text().strip(), a_href) 
        else:
            print("No results found.")
    else:
        print(f"Request failed with status code {response.status_code}")

# Call the function with the user's input
research_question(search_question)

