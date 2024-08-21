from bs4 import BeautifulSoup
import requests


def get_detailed_answer(id: int):
    """ Question details endpoint """

    detail_url = f'https://savollar.islom.uz/s/{id}'
    response = requests.get(detail_url)  
    soup = BeautifulSoup(response.content, 'html.parser')

    #checking the status, if it is OK, it will get the information about the Question
    if response.status_code == 200:

        title = soup.find('h1')
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
