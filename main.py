import requests
from bs4 import BeautifulSoup
import csv23



link = []
links=[]


url='https://books.toscrape.com/catalogue/category/books/default_15/index.html'  

r = requests.get(url)
# print('product_page_url :' + url)

soup = BeautifulSoup(r.text)


# def Visite_d_une_page(url):

	
# 	r = requests.get(url)
# 	soup = BeautifulSoup(r.text)

# 	title = soup.find('title')

# 	tds = soup.findAll('td')

# # print(tds[0].text)
# # [print (td.text + '\n\n') for td in tds]

# 	image = soup.find('img')
# 	images =image['src']
# # print(image.attrs['src'])
# 	# print(images)


# 	description = soup.find("div", {'id': 'product_description'}).find_next("p").text

# 	# print(description)

# 	review_rating = soup.find('p', {'class': "star-rating Three"}).attrs['class'][1]
	


# 	# books = 'https://books.toscrape.com/catalogue/category/books_1/index.html'
# 	# print(requests.get(books))

# 	cat = soup.find('ul',{'class':'breadcrumb'})
# 	a = cat.find('li',{'class':'active'}).find_previous()



# 	infos_extraites ={
# 		"product_page_url": url, 

# 		"universal_product_code": soup.find('td').string,
# 		"title" : soup.find('title').text,
# 		"price_excluding_tax": soup.findAll('td')[2].string,
# 		"price_including_tax": soup.findAll('td')[3].string,
# 		"number_available" : soup.findAll('td')[5].string,
# 		"product_description" : description,
# 		"category" : soup.find('ul',{'class':'breadcrumb'}).find('li',{'class':'active'}).find_previous().text,
# 		"review_rating" : review_rating,
# 		"image_url" : images
# 	}	
# 	return infos_extraites

# informations = Visite_d_une_page('https://books.toscrape.com/catalogue/the-coming-woman-a-novel-based-on-the-life-of-the-infamous-feminist-victoria-woodhull_993/index.html')


# print(informations)

# with open('main.csv','w', newline='')as index:
# 	writer=csv.writer(index, delimiter=';')
# 	writer.writerow(informations)





# header = informations.keys()
# print(getList(header))

# with open('countries.csv', 'w', encoding='UTF8') as f:
#     writer = csv.writer(f)

#     # write the header
#     writer.writerow(header)

#     # write the data
#     writer.writerow(informations)




# recupere_les_liens_des_catégories(url):


# for category in soup.find('div',{'class':'side_categories'}).findAll('a', href=True):
# 	link=category['href'].replace('../','')
# 	links.append('https://books.toscrape.com/catalogue/category/books/' + link)
# print(links)





# données pour toute une catégorie

entete = soup.find('div', {'class':"col-sm-8 h1"})
print(entete.text)
for a in soup.find('ul',{'class':'nav nav-list'}).findAll('a', href=True):
	print(a.text)
results = soup.find('form', {'class':'form-horizontal'})

print(results.text)

warning = soup.find('div', {'class': 'alert alert-warning'})
print(warning.text)

#warning = soup.find('div', {'class': 'alert alert-warning'}).find('strong')
#print(warning.text)




# parcourir les differentes pages d'une catégorie

#results = soup.find('form', {'class':'form-horizontal'}).find('strong')

#nbre=int(results.text)
#nbre_page=(int(nbre/20))
# (nbre%20 !=0):
#	nbre_page+=1

#for i in range(nbre_page):
#	print('https://books.toscrape.com/catalogue/category/books/default_15/page-' +str(i) + '.html')




# lien des livres des pages d'une caegory


#for a in soup.find('section').find_all('a',href=True):
	#link = a['href'].replace('../','')

	#links.append('https://books.toscrape.com/catalogue/' + link  )
	#print(links)


# données de tous les livres de la catégorie choisie

	# for image in soup.find_all('img'):
	# 	print(image['alt'])
	# 	img= image['src'].replace('../../../../','')
	# 	links.append('https://books.toscrape.com/' + img)

	# 	print (links)


	# review_rating = soup.findAll('p', {'class':'star-rating'})
	# for review in review_rating:
	# 	print('nombres d\'étoiles : '+ review.attrs['class'][1])




	# ti=[]
	# for b in soup.find('article', {'class':'product_pod'}).find_all('a'):
	# 	ti=b['href'].replace('../../../', 'https://books.toscrape.com/catalogue/')
	# 	print(ti)	


	# for prix in soup.findAll('p',{'class':'price_color'}):
	# 	print(prix.text)



	# 	for available in soup.findAll('p',{'class':'instock availability'}):
	# 			print(available.text)


	# 	for basket in soup.findAll('button',{'type': 'submit'}):

	# 		print(basket.text)





# page2= soup.find('li', {'class' : 'next'}).find('a')
# print(page2)

# r = requests.get('https://books.toscrape.com/catalogue/category/books/default_15/page-2.html')


# soup = BeautifulSoup(r.text)
# for b in soup.find('section').find_all('a',href=True):
# 	link = b['href'].replace('../','')

# 	links.append('https://books.toscrape.com/catalogue/' + link  )


# 	print(links)




# 	r = requests.get('https://books.toscrape.com/catalogue/category/books/default_15/page-3.html')


# soup = BeautifulSoup(r.text)
# for b in soup.find('section').find_all('a',href=True):
# 	link = b['href'].replace('../','')

# 	links.append('https://books.toscrape.com/catalogue/' + link  )


# 	print(links)


# r = requests.get('https://books.toscrape.com/catalogue/category/books/default_15/page-4.html')


# soup = BeautifulSoup(r.text)
# for b in soup.find('section').find_all('a',href=True):
# 	link = b['href'].replace('../','')

# 	links.append('https://books.toscrape.com/catalogue/' + link  )


# 	print(links)


# r = requests.get('https://books.toscrape.com/catalogue/category/books/default_15/page-5.html')


# soup = BeautifulSoup(r.text)
# for b in soup.find('section').find_all('a',href=True):
# 	link = b['href'].replace('../','')

# 	links.append('https://books.toscrape.com/catalogue/' + link  )


# 	print(links)



# 	r = requests.get('https://books.toscrape.com/catalogue/category/books/default_15/page-6.html')


# soup = BeautifulSoup(r.text)
# for b in soup.find('section').find_all('a',href=True):
# 	link = b['href'].replace('../','')

# 	links.append('https://books.toscrape.com/catalogue/' + link  )


# 	print(links)


# # 	r = requests.get('https://books.toscrape.com/catalogue/category/books/default_15/page-7.html')


# soup = BeautifulSoup(r.text)
# for b in soup.find('section').find_all('a',href=True):
# 	link = b['href'].replace('../','')

# 	links.append('https://books.toscrape.com/catalogue/' + link  )


# 	print(links)







