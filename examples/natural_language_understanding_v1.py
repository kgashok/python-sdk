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
url_list = [url1, url2, url3]

for nlu_url in url_list: 
    response = service.analyze(
        url=nlu_url,
        features=Features(categories=CategoriesOptions(), \
                        #entities=EntitiesOptions(),
                        #keywords=KeywordsOptions())
                        )
    ).get_result()

    #print(json.dumps(response, indent=2))
    print(response['retrieved_url'])
    for c in response['categories']:
        print(c['score'], c['label'])


