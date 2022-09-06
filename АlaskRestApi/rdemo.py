import requests

r =  requests.get('https://xkcd.com/353/')

print("content:")
print("-----")
print(r.content)
print("-----")
print("text:")
print("-----")
print(r.text)
