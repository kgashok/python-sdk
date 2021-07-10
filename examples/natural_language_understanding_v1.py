import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, CategoriesOptions
#from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Authentication via IAM
# authenticator = IAMAuthenticator('your_api_key')
# service = NaturalLanguageUnderstandingV1(
#     version='2018-03-16',
#     authenticator=authenticator)
# service.set_service_url('https://gateway.watsonplatform.net/natural-language-understanding/api')

# Authentication via external config like VCAP_SERVICES
service = NaturalLanguageUnderstandingV1(
    version='2018-03-16')
#service.set_service_url('https://gateway.watsonplatform.net/natural-language-understanding/api')

#response = service.analyze(
#    text='Bruce Banner is the Hulk and Bruce Wayne is BATMAN! '
#    'Superman fears not Banner, but Wayne.',
#    features=Features(entities=EntitiesOptions(),
#                      keywords=KeywordsOptions())).get_result()

#print(json.dumps(response, indent=2))

url1 = "http://newsroom.ibm.com/Guerbet-and-IBM-Watson-Health-Announce-Strategic-Partnership-for-Artificial-Intelligence-in-Medical-Imaging-Liver"
url2 = "https://medium.com/swlh/how-to-study-for-data-structures-and-algorithms-interviews-at-faang-65043e00b5df" 
url3 = "https://developer.ibm.com/tutorials/smart-bookmark-plugin-using-watson-nlu/"
url4 = "https://www.msn.com/en-in/money/technology/alien-life-on-saturn-moon-nasa-cassini-found-potential-proof-says-study/ar-AALXLVN?ocid=winp1taskbar"
url5 = "https://kgisl.github.io/makesite/blog/cokreating-geniuses/"
url6 = "https://j.mp/bookThis"
url7 = "https://stackoverflow.blog/2021/07/07/the-unexpected-benefits-of-mentoring-others/?cb=1&_ga=2.73568470.599507052.1625770473-478896514.1585758695"
url8 = "https://www.businesstoday.in/industry/it/story/tcs-to-hire-40000-freshers-from-campuses-in-current-fiscal-300932-2021-07-09"
url9 = "https://www.deccanherald.com/business/business-news/elon-musk-trial-asks-the-2-billion-question-who-controls-tesla-1006673.html"
url10 = "https://www.tennisworldusa.org/tennis/news/Roger_Federer/99764/novak-djokovic-i-hope-that-roger-federer-rafael-nadal-and-me-can-/"
url_list = [url1, url2, url3, url4, url5, url6, url7, url8, url9, url10]

filename = "urls.txt"
with open(filename, 'r') as fp:
    urls = fp.readlines()

import time

for nlu_url in reversed(urls):
    nlu_url = nlu_url.strip()
    try:
        response = service.analyze(
            url=nlu_url,
            features=Features(categories=CategoriesOptions(), \
                            #entities=EntitiesOptions(),
                            #keywords=KeywordsOptions())
                            )
        ).get_result()
    except: 
        print("*** Server busy...")
        time.sleep(2)

    #print(json.dumps(response, indent=2))
    print(response['retrieved_url'])
    for c in response['categories']:
        print("-", c['score'], c['label'])

