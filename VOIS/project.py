import spacy
import pytesseract as tess
import re
import cv2 as cv
spacy.__version__

img = cv.imread("test_bill.jpg")  # create matrixx of image
text = tess.image_to_string(img)  # extraction of data from image
nlp = spacy.load("en_core_web_sm")

doc = nlp(text)
names = []
prices = []
cities = []
dates = []

for ent in doc.ents:
    if ent.label_ == "PERSON":
        names.append(ent.text)

    elif ent.label_ == "MONEY":
        prices.append(ent.text) 

    elif ent.label_ == "GPE":
        cities.append(ent.text)

    elif ent.label_ == "DATE":
        dates.append(ent.text)

def extract_phone_numbers(string):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', number) for number in phone_numbers]

def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)

phone = extract_phone_numbers(text)
emails = extract_email_addresses(text)

# print(phone,emails,sep="\n")

import json
data = {
    "names" : names,
    "prices": prices,
    "cities":cities,
    "dates" : dates,
    "phones" : phone,
    "emails" : emails
}
data_json = json.dumps(data)

output = {}

for ent in doc.ents :
    if ent.label_ in output.keys():
        output[ent.label_].append(ent.text)
    else :
        output[ent.label_] = []
        output[ent.label_].append(ent.text)

output["phone"] = phone
output["emails"] = emails

output_2 = json.dumps(output)

with open("sample.json","w") as output_file :
  json.dump(output,output_file)

data = json.load(open("sample.json"))

final_output_data = {
    "names" : data['MONEY'],
    "prices": data["MONEY"],
    "cities": data["ORG"],
    "dates" : data["DATE"],
    "phones" : phone,
    "emails" : emails
}

print("varad")