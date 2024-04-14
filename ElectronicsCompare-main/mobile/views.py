from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from mobile.models import Mobile

def get_text_content(element):
    text_content = ""

    # Check if the div element is found
    if element:
        # Iterate through all the elements within the div
        for element in element.descendants:
            # Check if the element is a string (text)
            if isinstance(element, str):
                text_content += element 
    
    return text_content

def get_latest_price(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.select_one('[class="specs-phone-name-title"]').contents[0]
            price_element  = soup.select_one('[data-spec="price"]')            
            image_element = soup.select_one('[class="specs-photo-main"]')
            desc_element = soup.select_one('[class="specs-spotlight-features"]')
            image_src="https://clipground.com/images/photo-icon-png-7.png"
            if image_element:
            # Select the img tag within the div
                img_tag = image_element.select_one('img')

            # Check if the img tag is found
                if img_tag:
            # Get the src attribute of the img tag
                    image_src = img_tag['src']
            
        
            # print(
            #    title,
            #    get_text_content(desc_element),
            #    get_text_content(price_element),
            #    image_src 
            # )
            created,mov = Mobile.objects.create(
                title=title,
                description=get_text_content(desc_element),
                price=get_text_content(price_element),
                image_url=image_src,
            )
            # print(created,mov)
            return True
        else:
            return f"Failed to retrieve the webpage. Status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage

# Create your views here.
def hello(request):
    data = {'mobiles':Mobile.objects.all()}
    if request.method == 'POST':
        if 'delete' in request.POST:
            mobile_id = request.POST['delete']
            mobile = Mobile.objects.get(pk=mobile_id)
            mobile.delete()
            return render(request,'index.html',data)
        
        url = request.POST.get('url')
        get_latest_price(url)
        data =  {'add':True,'mobiles':Mobile.objects.all()}
        return render(request,'index.html',data)
    return render(request,'index.html',data)
