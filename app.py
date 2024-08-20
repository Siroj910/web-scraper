from bs4 import BeautifulSoup
import requests

# Url => 
url = "https://savollar.islom.uz/"

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')


search_question = input("Enter your question: ")


def research_question(keywords: str):
    params = {'words': keywords} # search parametres

    response = requests.get(url, params=params)  

    # Checking the status of the request
    if response.status_code == 200:
        # Parse the response content
        soup = BeautifulSoup(response.content, 'html.parser')

        
        results = soup.find_all(class_='question')  
        print(results)
        for result in results:
            print(result.get_text())  

    else:
        print(f"Request failed with status code {response.status_code}")


research_question(search_question)

def get_detailed_answer(id: int):
    """ Question details endpoint """

    detail_url = f'https://savollar.islom.uz/s/{id}'
    response = requests.get(detail_url)  
    soup = BeautifulSoup(response.content, 'html.parser')

    #checking the status, if it is OK, it will get the information about the Question
    if response.status_code == 200:

        title = soup.find('h1', class_='title')
        title_text = title.get_text(strip=True) if title else "Title not found"
        
        info = soup.find('div', class_='info_question')
        info_text = info.get_text(strip=True) if info else "Info not found"
        
        paragraphs = soup.find_all('div', class_='text_in_question')
        paragraphs_text = "\n\n".join([p.get_text(strip=True) for p in paragraphs]) if paragraphs else "Paragraphs not found"


        answer_in_question = soup.find_all('div', class_='answer_in_question')
        info_text = "\n\n".join([p.get_text(strip=True) for p in answer_in_question]) if paragraphs else "Paragraphs not found"
        
        # Returning the extracted information
        return {
            "title": title_text,
            "info": info_text,
            "paragraphs": paragraphs_text,
            "answer_in_question":info_text
        }
    else:
        return {"error": "Failed to retrieve the question details"}

data = get_detailed_answer(251816)
print(data)
