import microdata
import urllib
import sys

#url = "file:////Users/wb/projects/s2/something.to/templates/person/person.html"
url = sys.argv[1]
output_file = url.replace('.html', '.json')
output_file = output_file.replace('file:////Users/wb/projects/s2/something.to/', '')
print(output_file)
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
  the_page = response.read()

items = microdata.get_items(the_page)
len(items)
item = items[0]

original_stdout = sys.stdout # Save a reference to the original standard output

with open(output_file, 'w+') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print(item.json())
    sys.stdout = original_stdout # Reset the standard output to its original value
#f= open(output_file,"w+")
#f.write(print(item.json))
#f.close
