from django.utils.text import slugify

a_file = open("titles.txt", "r")

urllist = []
for line in a_file:
  stripped_line = line.strip()
  urllist.append(stripped_line)
bb = input("Enter The Your Web Site: " )
for url in urllist:
    
    b = (slugify(url))
    
    mahin = bb + b
    print(mahin)
