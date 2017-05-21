import random
import string
import uuid
from random import randint
import random
import time
import math

domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
letters = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l"]

def password_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def strTimeProp(start, end, format, prop):
    """Generating random date time in the given format between the given start and end date and time.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, 'datetime("%Y-%m-%dT%H:%M:%S")', prop)

def get_random_domain(domains):
    return random.choice(domains)

def get_random_name(letters, length):
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_emails(nb, length):
    return [get_random_name(letters, length) + '@' + get_random_domain(domains) for i in range(nb)]

def generate_random_automated_emails(nb, length):
    return [get_random_name(letters, length) + '@' + 'peterlist.org' for i in range(nb)]


def phn():
    n = '0000000000'
    while '9' in n[3:6] or n[3:6]=='000' or n[6]==n[7]==n[8]==n[9]:
        n = str(random.randint(10**9, 10**10-1))
    return n[:3] + '-' + n[3:6] + '-' + n[6:]

def ID():
    return str(uuid.uuid4())[2:8]

def amount1(a:int,b:int):
    return(randint(a,b))

def age():
    return(randint(20,60))

random_street = ["Berkeley","Columbia","Oxford","Exter","Amherst Aisle","Harvard","Campus","Jamboree","Palatine"]
random_buildingNumber = [271,279,226,228,446,15121,65]
city = ["Irvine","Newport Beach","Laguna Beach","Venice","Santa Monica"]

jobTitle = ["Intern","Software Engineer","Business Analyst","Consultant"]

item_type = ["Music","Books","Accessory","Bikes","Cars","Clothes","Phones"]
job_type = ["Accounting","Programming","Finance","Teaching","Research","Data Analyst","Consulting","Mechanical","Construction"]
event_type = ["Music Concert", "Community Service","Career Fair","Sports","TV and Cinema","Workshop"]
housing_type = ["Rent","Lease", "Buy"]
company_name = ["WellsFargo","Google","Chase","Yahoo","Facebook","Amazon","Verizon","Tesla"]
true_false = ["true","false"]
startDate = 'datetime("2017-05-20T00:00:00")'
endDate = 'datetime("2018-03-16T23:59:59")'

text_file = open("ownersampledata.adm","w")
text_file2 = open("sampledata.adm","w")

for i in range(1,101):

    userID = ID();
    userPhone = phn();
    useremailID = generate_random_emails(10,7)[1];
    userPassword = password_generator()

    randomemailID = generate_random_automated_emails(10,7);
    
    user_string = '{{"userID": "{0}","contactInfo":{{"phoneNumber": "{1}","email": "{2}"}},"userPassword": "{3}"}}'
    text_file.write(user_string.format(userID,userPhone,useremailID,userPassword))
    text_file.write("\n")

    job_string = '{{"postID": "{0}", "postInfo":{{"location":{{"streetName": "{1}","buildingNumber": {2}, "city": "{3}","state": "{4}","country": "United States of America"}},"dateTime": {5},\
"description": "{6}", "amount": {7}, "userID": "{8}", "automatedEmailID": "{9}"}}, "postingCategory": "Job",\
"fullTime": {10}, "jobCategory": {11}, "organizationName":"{12}", "jobTitle": "{13}", "jobRequirement": "{14}"}}'

    postID = ID()
    streetName = random.choice(random_street)
    buildingNumber = random.choice(random_buildingNumber)
    city = random.choice(city)
    state = "CA"
    randomDateTime = randomDate(startDate, endDate, random.random())
    description = "Looking for someone..."
    amount = amount1(30000,100000)
    userID = userID
    auto_email = random.choice(randomemailID)

    value = random.choice(true_false)
    jobCategory = randint(1,34)
    organizationName = random.choice(company_name)
    jobTitle = random.choice(jobTitle)
    jobRequirement = "Should have a Bachelor and Masters Degree with a 2 year work experience"

    text_file2.write(job_string.format(postID,streetName,buildingNumber,city,state,randomDateTime,description,amount,userID,auto_email,value,jobCategory,\
                                       organizationName,jobTitle,jobRequirement))
    text_file2.write("\n")
    

    event_string = '{{"postID": "{0}", "postInfo":{{"location":{{"streetName": "{1}","buildingNumber": {2}, "city": "{3}","state": "{4}","country": "United States of America"}},"dateTime": {5},\
"description": "{6}", "amount": {7}, "userID": "{8}", "automatedEmailID": "{9}"}}, "postingCategory": "Event",\
"startDate": {10},"endDate": {11},"eventCategory": {12}, "organizationName": "{13}", "eventTitle": "{14}"}}'

    postID = ID()
    streetName = random.choice(random_street)
    buildingNumber = random.choice(random_buildingNumber)
    city = random.choice(["Irvine","Newport Beach","Laguna Beach","Venice","Santa Monica"])
    state = "CA"
    randomDateTime = randomDate(startDate, endDate, random.random())
    description = "An Exciting Event in..."
    amount = amount1(30,100)
    userID = userID
    auto_email = random.choice(randomemailID)

    startDateEvent = 'datetime("2017-06-01T00:00:00")'
    endDateEvent = 'datetime("2017-06-29T23:59:59")'
    randomStartDate = randomDate(startDateEvent, endDateEvent, random.random())
    randomEndDate = randomDate(randomStartDate, endDateEvent, random.random())
    eventCategory = randint(1,18)
    organizationName = random.choice(["TD Music Group","ASUCI","STEM Inc.","ICS"])
    eventTitle = random.choice(["Fiesta","Workshop","Fair","Market"])

    text_file2.write(event_string.format(postID,streetName,buildingNumber,city,state,randomDateTime,description,amount,userID,auto_email,randomStartDate,\
                                       randomEndDate,eventCategory,organizationName,eventTitle))
    text_file2.write("\n")

    itemSale_string = '{{"postID": "{0}", "postInfo":{{"location":{{"streetName": "{1}","buildingNumber": {2}, "city": "{3}","state": "{4}","country": "United States of America"}},"dateTime": {5},\
"description": "{6}", "amount": {7}, "userID": "{8}", "automatedEmailID": "{9}"}}, "postingCategory": "Item Sale",\
"itemName": "{10}","itemCategory": {11}, "condition": "{12}"}}'

    
    postID = ID()
    streetName = random.choice(random_street)
    buildingNumber = random.choice(random_buildingNumber)
    city = random.choice(["Irvine","Newport Beach","Laguna Beach","Venice","Santa Monica"])
    state = "CA"
    randomDateTime = randomDate(startDate, endDate, random.random())
    description = "Item on sale..."
    amount = amount1(30,1000)
    userID = userID
    auto_email = random.choice(randomemailID)

    itemName = "Item Title"
    itemCategory = randint(1,19)
    condition = random.choice(["Fairly New","Old","Average","Good"])

    text_file2.write(itemSale_string.format(postID,streetName,buildingNumber,city,state,randomDateTime,description,amount,userID,auto_email,itemName,\
                                       itemCategory,condition))
    text_file2.write("\n")


    lostFound_string = '{{"postID": "{0}", "postInfo":{{"location":{{"streetName": "{1}","buildingNumber": {2}, "city": "{3}","state": "{4}","country": "United States of America"}},"dateTime": {5},\
"description": "{6}", "amount": {7}, "userID": "{8}", "automatedEmailID": "{9}"}}, "postingCategory": "LostFound",\
"itemFoundDate": {10}, "itemName": "{11}", "lostOrFound" : {12}}}'

    postID = ID()
    streetName = random.choice(random_street)
    buildingNumber = random.choice(random_buildingNumber)
    city = random.choice(["Irvine","Newport Beach","Laguna Beach","Venice","Santa Monica"])
    state = "CA"
    randomDateTime = randomDate(startDate, endDate, random.random())
    description = "Item on sale..."
    amount = 0
    userID = userID
    auto_email = random.choice(randomemailID)

    itemFoundDate = randomDate(startDate, randomDateTime, random.random())
    itemName = "Found Item Title"
    lostFound = random.choice(true_false)

    text_file2.write(lostFound_string.format(postID,streetName,buildingNumber,city,state,randomDateTime,description,amount,userID,auto_email,itemFoundDate,\
                                            itemName,lostFound))
    text_file2.write("\n")


    housing_string = '{{"postID": "{0}", "postInfo":{{"location":{{"streetName": "{1}","buildingNumber": {2}, "city": "{3}","state": "{4}","country": "United States of America"}},"dateTime": {5},\
"description": "{6}", "amount": {7}, "userID": "{8}", "automatedEmailID": "{9}"}}, "postingCategory": "Housing",\
"bedroomNumber":{10}, "petAllowed":{11},"housingCategory": {12},"size": {13}, "startDate": {14},"endDate": {15}, "occupants": {16},\
"bathroomType": {17}, "roomates": {18}, "hasParking": {19}, "localityName" : "{20}"}}'

    postID = ID()
    streetName = random.choice(random_street)
    buildingNumber = random.choice(random_buildingNumber)
    city = random.choice(["Irvine","Newport Beach","Laguna Beach","Venice","Santa Monica"])
    state = "CA"
    randomDateTime = randomDate(startDate, endDate, random.random())
    description = "Looking for someone..."
    amount = amount1(30000,100000)
    userID = userID
    auto_email = random.choice(randomemailID)

    bedroom = randint(1,5)
    pet = random.choice(true_false)
    housingCategory = randint(1,3)
    size = randint(900,1200)
    startDateEvent = 'datetime("2017-06-01T00:00:00")'
    endDateEvent = 'datetime("2017-06-29T23:59:59")'
    randomStartDate = randomDate(startDateEvent, endDateEvent, random.random())
    randomEndDate = randomDate(randomStartDate, endDateEvent, random.random())
    occupants = randint(2,7)
    bathroom = random.choice(true_false)
    roomates = randint(1,3)
    hasParking = random.choice(true_false)
    locality = random.choice(["Harvard","Oxford","Columbia","Berkeley","Mesa"])
    

    text_file2.write(housing_string.format(postID,streetName,buildingNumber,city,state,randomDateTime,description,amount,userID,auto_email,bedroom,pet,\
                                       housingCategory,size,randomStartDate,randomEndDate,occupants,bathroom,roomates,hasParking,locality))
    text_file2.write("\n")







    

    
    
    




