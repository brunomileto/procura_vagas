import pprint
import requests
from bs4 import BeautifulSoup
from procura_vagas.getlinks import get_links

links_list = [
    'https://www.trabalhabrasil.com.br/vagas-empregos-em-aparecida-go',
    'https://www.trabalhabrasil.com.br/vagas-empregos-em-goiania-go',
    'https://www.trabalhabrasil.com.br/vagas-empregos-em-aparecida-de-goiania-go',
    'https://www.trabalhabrasil.com.br/vagas-empregos-em-anapolis-go',
    'https://www.trabalhabrasil.com.br/vagas-empregos-em-brasilia-df',
    'https://www.trabalhabrasil.com.br/vagas-empregos-em-sao-paulo-sp'
    'https://www.trabalhabrasil.com.br/vagas-empregos-em-florianopolis-sc',
    'https://www.trabalhabrasil.com.br/vagas-empregos-em-curitiba-pr',
    'https://www.trabalhabrasil.com.br/vagas-empregos-em-rio-de-janeiro-rj',
    'https://www.trabalhabrasil.com.br/vagas-empregos-em-belo-horizonte-mg'
]


def main(urls):
    """
    This function will get from our url list, the links of the pages, make the requests, create the soup object and
    select the values of the given html parameters. Then this function calls another function to actually get the
    values of the html parameters and, in the end this function will call another function to sort the result.
    :param urls:
    :return: hacker_news_list: A print with a list that contain all data, from the web pages, filtered and sorted.
    """
    return_list = []
    for link in urls:
        response = requests.get(link)
        soup_object = BeautifulSoup(response.text, 'html.parser')
        tag = soup_object.select('.job-plain-text')
        tag = str(tag)
        terms_list = ['t.i', ' ti ', 'sistemas', 'sistema', 'web', 'aplicativo', 'python', 'java',
                      'desenvolvimento', 'software', 'javascript']

        for i in terms_list:
            finder = tag.find(i)
            if finder >= 0:
                return_list.append(link)

    pprint.pprint(return_list)


for i in links_list:
    main(get_links(i))
