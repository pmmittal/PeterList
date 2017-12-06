import random
import string
import uuid
from random import randint
import random
import time
import math

jobIndustry_list = ['Accounting','Art', 'Automotive','Banking', \
 'Management','Consultant','Customer Service','Education','Engineering', \
 'Video','Finance', 'Government','Hospitality','Human Resources','Information Technology','Legal','Manufacturing','Marketing', \
 'Journalism','Medical', 'Sales','Science','Software Technology','Transportation']

eventCategory_list = ['Arts', 'Music','Camps Trip', 'Retreats','Career','Charity', 'Training', \
                      'Workshops','Concerts','Festivals', 'Fairs','Food', \
                      'Religion', 'Science', 'Technology','Sports', 'Fitness','Travel', \
                      'Outdoor']

itemCategory_list = ['Bicycles','Books','Cars', \
                     'Clothing', 'Electronics','Furniture','Health', \
                     'Beauty','Household', 'Musical Instruments','Other', \
                     'Toys']

lostFoundCategory_list = ['Item Lost','Item Found']

housing_images = ["https://images.unsplash.com/photo-1486304873000-235643847519?dpr=2&auto=format&fit=crop&w=1500&h=844&q=80&cs=tinysrgb&crop=&bg=",
"https://images.unsplash.com/photo-1488805990569-3c9e1d76d51c?dpr=2&auto=format&fit=crop&w=1500&h=1001&q=80&cs=tinysrgb&crop=&bg=",
"https://images.unsplash.com/photo-1463620910506-d0458143143e?dpr=2&auto=format&fit=crop&w=1500&h=1000&q=80&cs=tinysrgb&crop=&bg=",
"https://images.unsplash.com/photo-1473447216727-44efba8cf0e0?dpr=1&auto=format&fit=crop&w=1500&h=1001&q=80&cs=tinysrgb&crop=&bg=",
"https://images.unsplash.com/photo-1444201983204-c43cbd584d93?dpr=1&auto=format&fit=crop&w=1500&h=1000&q=80&cs=tinysrgb&crop=&bg=",
"https://images.unsplash.com/photo-1424847262089-18a6858bd7e2?dpr=1&auto=format&fit=crop&w=1500&h=1000&q=80&cs=tinysrgb&crop=&bg="]

event_images = ["http://tricostar.com/wp-content/uploads/Event-management.png",
                "http://technext.github.io/Evento/images/demo/bg-slide-01.jpg",
                "https://www.uwrf.edu/CareerFair/images/Career-Fair-Large-Page-Banner-JPG_3.jpg",
                "https://d3n8a8pro7vhmx.cloudfront.net/greekladders/pages/187/attachments/original/1411750417/careerfair-image.jpg?1411750417"]

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
    return strTimeProp(start, end, "%Y-%m-%dT%H:%M:%S", prop)

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

jobTitle = ["Data Scientist","Software Engineer","Business Analyst","Consultant"]

company_name = ["Wells Fargo","Google","Chase","Yahoo","Facebook","Amazon","Verizon","Tesla","Apple"]
true_false = ["true","false"]


startDate = "2016-05-20T00:00:00"
endDate = "2017-11-28T23:59:59"

text_file = open("ownersampledata.adm","w")
text_file2 = open("sampledata.adm","w")

for i in range(1,101):

    userID_postID_list = []

    userID = ID();
    
    
    randomemailID = generate_random_automated_emails(10,7);


#Job string done#
    job_string = '{{"postID": "{0}", "postInfo":{{"location":{{"streetName": "{1}","buildingNumber": {2}, "city": "{3}","state": "{4}","country": "United States of America","zip": 92612}},"createdOn": "{5}",\
"description": "{6}", "amount": {7}, "userID": "{8}", "automatedEmailID": "{9}"}}, "postingCategory": "Job",\
"jobType": "{10}", "jobIndustry": "{11}", "jobOrganizationName":"{12}", "jobTitle": "{13}", "jobRequirement": "{14}"}}'

    postID = ID()
    userID_postID_list.append(postID)
    streetName = random.choice(random_street)
    buildingNumber = random.choice(random_buildingNumber)
    city = random.choice(city)
    state = "CA"
    randomDateTime = randomDate(startDate, endDate, random.random())
    description = "Looking for someone..."
    amount = amount1(30000,100000)
    userID = userID
    auto_email = random.choice(randomemailID)

    jobType = random.choice(["Full Time","Part Time","Internship"])
    #value = random.choice(true_false)
    jobIndustry = random.choice(jobIndustry_list)
    organizationName = random.choice(company_name)
    jobTitle = random.choice(jobTitle)
    jobRequirement = "Should have a Bachelor and Masters Degree with a 2 years work experience"

    text_file2.write(job_string.format(postID,streetName,buildingNumber,city,state,randomDateTime,description,amount,userID,auto_email,jobType,jobIndustry,\
                                       organizationName,jobTitle,jobRequirement))
    text_file2.write("\n")


    
    #event string done**
    event_string = '{{"postID": "{0}", "postInfo":{{"location":{{"streetName": "{1}","buildingNumber": {2}, "city": "{3}","state": "{4}","country": "United States of America","zip": 92612}},"createdOn": "{5}",\
"description": "{6}", "amount": {7}, "userID": "{8}", "automatedEmailID": "{9}", "photos": ["{15}"]}}, "postingCategory": "Event",\
"eventStartOn": "{10}","eventEndOn": "{11}","eventCategory": "{12}", "eventOrganizationName": "{13}", "eventTitle": "{14}"}}'

    postID = ID()
    userID_postID_list.append(postID)
    streetName = random.choice(random_street)
    buildingNumber = random.choice(random_buildingNumber)
    city = random.choice(["Irvine","Newport Beach","Laguna Beach","Venice","Santa Monica"])
    state = "CA"
    randomDateTime = randomDate(startDate, endDate, random.random())
    description = "An Exciting Event in..."
    amount = amount1(30,100)
    userID = userID
    auto_email = random.choice(randomemailID)

    startDateEvent = "2017-06-01T00:00:00"
    endDateEvent = "2017-06-29T23:59:59"
    randomStartDate = randomDate(startDateEvent, endDateEvent, random.random())
    randomEndDate = randomDate(randomStartDate, endDateEvent, random.random())
    eventCategory = random.choice(eventCategory_list)
    organizationName = random.choice(["TD Music Group","ASUCI","STEM Inc.","ICS"])
    eventTitle = random.choice(["Fiesta","Workshop","Fair","Market"])
    eventPhoto = random.choice(event_images)

    text_file2.write(event_string.format(postID,streetName,buildingNumber,city,state,randomDateTime,description,amount,userID,auto_email,randomStartDate,\
                                       randomEndDate,eventCategory,organizationName,eventTitle,eventPhoto))
    text_file2.write("\n")

    #Item_sale string done

    itemSale_string = '{{"postID": "{0}", "postInfo":{{"location":{{"streetName": "{1}","buildingNumber": {2}, "city": "{3}","state": "{4}","country": "United States of America","zip": 92612}},"createdOn": "{5}",\
"description": "{6}", "amount": {7}, "userID": "{8}", "automatedEmailID": "{9}"}}, "postingCategory": "Item Sale",\
"itemName": "{10}","itemCategory": "{11}", "condition": "{12}"}}'

    
    postID = ID()
    userID_postID_list.append(postID)
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
    itemCategory = random.choice(itemCategory_list)
    condition = random.choice(["Fairly New","Old","Average","Good"])

    text_file2.write(itemSale_string.format(postID,streetName,buildingNumber,city,state,randomDateTime,description,amount,userID,auto_email,itemName,\
                                       itemCategory,condition))
    text_file2.write("\n")


#     lostFound_string = '{{"postID": "{0}", "postInfo":{{"location":{{"streetName": "{1}","buildingNumber": {2}, "city": "{3}","state": "{4}","country": "United States of America","zip": 92612}},"dateTime": {5},\
# "description": "{6}", "amount": {7}, "userID": "{8}", "automatedEmailID": "{9}"}}, "postingCategory": "LostFound",\
# "itemFoundDate": {10}, "itemName": "{11}", "lostOrFound" : "{12}"}}'

#     postID = ID()
#     streetName = random.choice(random_street)
#     buildingNumber = random.choice(random_buildingNumber)
#     city = random.choice(["Irvine","Newport Beach","Laguna Beach","Venice","Santa Monica"])
#     state = "CA"
#     randomDateTime = randomDate(startDate, endDate, random.random())
#     description = "Item on sale..."
#     amount = 0
#     userID = userID
#     auto_email = random.choice(randomemailID)

#     itemFoundDate = randomDate(startDate, randomDateTime, random.random())
#     itemName = "Found Item Title"
#     lostFound = random.choice(lostFoundCategory_list)

#     text_file2.write(lostFound_string.format(postID,streetName,buildingNumber,city,state,randomDateTime,description,amount,userID,auto_email,itemFoundDate,\
#                                             itemName,lostFound))
#     text_file2.write("\n")



    housing_sale_string = '{{"postID": "{0}", "postInfo":{{"location":{{"streetName": "{1}","buildingNumber": {2}, "city": "{3}","state": "{4}","country": "United States of America","zip": 92612}},"createdOn": "{5}",\
"description": "{6}", "amount": {7}, "userID": "{8}", "automatedEmailID": "{9}", "photos":["{18}"]}}, "postingCategory": "Housing Sale",\
"bedroomNumber":{10}, "bathroomNumber": {11},"homeType": "{12}","size": {13}, "dateAvailable": "{14}","furnished": {15}, "parkingNumber": {16},\
"localityName" : "{17}"}}' 
    
    
    postID = ID()
    userID_postID_list.append(postID)
    streetName = random.choice(random_street)
    buildingNumber = random.choice(random_buildingNumber)
    city = random.choice(["Irvine","Newport Beach","Laguna Beach","Venice","Santa Monica"])
    state = "CA"
    randomDateTime = randomDate(startDate, endDate, random.random())
    description = "Looking for someone..."
    amount = amount1(400,1400)
    userID = userID
    auto_email = random.choice(randomemailID)

    bedroom = randint(1,7)
    bathroom = randint(1,7)
    homeType = random.choice(['Condo','House','Penthouse'])
    #pet = random.choice(true_false)
    #housingCategory = "Rent/Lease"
    size = randint(900,1200)
    startDateEvent = "2017-06-01T00:00:00"
    endDateEvent = "2017-06-29T23:59:59"
    dateAvailable = randomDate(startDateEvent, endDateEvent, random.random())
    furnished = random.choice(true_false)
    parkingNumber = random.choice([1,2])
    locality = random.choice(["Harvard","Oxford","Columbia","Berkeley","Mesa"])
    housingPhoto = random.choice(housing_images)



    

    text_file2.write(housing_sale_string.format(postID,streetName,buildingNumber,city,state,randomDateTime,description,amount,userID,auto_email,bedroom,bathroom,\
                                       homeType,size,dateAvailable,furnished,parkingNumber,locality,housingPhoto))
    text_file2.write("\n")




    housing_lease_string = '{{"postID": "{0}", "postInfo":{{"location":{{"streetName": "{1}","buildingNumber": {2}, "city": "{3}","state": "{4}","country": "United States of America","zip": 92612}},"createdOn": "{5}",\
"description": "{6}", "amount": {7}, "userID": "{8}", "automatedEmailID": "{9}", "photos":["{22}"]}}, "postingCategory": "Housing Lease",\
"bedroomNumber": {10}, "bathroomNumber": {11},"homeType": "{12}","size": {13}, "dateAvailable": "{14}","furnished": {15}, "hasParking": {16},\
"localityName" : "{17}", "petAllowed": {18}, "endDate": "{19}", "occupants": {20}, "roommates": {21}}}'


    postID = ID()
    userID_postID_list.append(postID)
    streetName = random.choice(random_street)
    buildingNumber = random.choice(random_buildingNumber)
    city = random.choice(["Irvine","Newport Beach","Laguna Beach","Venice","Santa Monica"])
    state = "CA"
    randomDateTime = randomDate(startDate, endDate, random.random())
    description = "Looking for someone..."
    amount = amount1(400,1400)
    userID = userID
    auto_email = random.choice(randomemailID)

    bedroom = randint(1,7)
    bathroom = randint(1,7)
    homeType = random.choice(['Condo','House','Penthouse'])
    #pet = random.choice(true_false)
    #housingCategory = "Rent/Lease"
    size = randint(900,1200)
    startDateEvent = "2017-06-01T00:00:00"
    endDateEvent = "2017-06-29T23:59:59"
    dateAvailable = randomDate(startDateEvent, endDateEvent, random.random())
    furnished = random.choice(true_false)
    hasParking = random.choice(true_false)
    locality = random.choice(["Harvard","Oxford","Columbia","Berkeley","Mesa"])


    petAllowed = random.choice(true_false)
    randomEndDate = randomDate(randomStartDate, endDateEvent, random.random())
    occupants = randint(2,7)

    roommates = randint(1,3)
    
    
    housingPhoto = random.choice(housing_images)

    text_file2.write(housing_lease_string.format(postID,streetName,buildingNumber,city,state,randomDateTime,description,amount,userID,auto_email,bedroom,bathroom,\
                                       homeType,size,dateAvailable,furnished,hasParking,locality,petAllowed, randomEndDate,occupants, roommates,housingPhoto))
    text_file2.write("\n")


    user_string = '{{"userID": "{0}","firstName": "{1}", "lastName": "{2}", "phone": "{3}", "email": "{4}", "password": "{5}", "userPostings": {6}}}'

    userFirstName = random.choice(["Jack","Peter","Anteater","David","Ray","Emily","Sophia","Jasmine"])
    userLastName = random.choice(["Bill","Juan","Smith","Mata","Ronaldo","Muller","Messi","Suarez"])
    userPhone = phn();
    useremailID = generate_random_emails(10,7)[1];
    userPassword = password_generator()
    userPostings_list = userID_postID_list
    
    text_file.write(user_string.format(userID,userFirstName,userLastName,userPhone,useremailID,userPassword,userPostings_list))
    text_file.write("\n")

    
    
    




