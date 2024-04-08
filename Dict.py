thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
thisdict.update({"color": "red"})
y= thisdict.get("color")
del thisdict["model"]
print(thisdict)
print(x)
print(y)
