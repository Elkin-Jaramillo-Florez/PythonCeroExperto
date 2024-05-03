set_countries = {"col", "mex", "arg"}

size = len(set_countries)
print(size)

print("col" in set_countries)
print("pe" in set_countries)

set_countries.add("pe")
print(set_countries)
set_countries.add("pe")
print(set_countries)


# update
set_countries.update({"bol", "ecu", "pe"})
print(set_countries)

# remove
set_countries.remove("bol")
print(set_countries)
set_countries.discard("bol")
print(set_countries)

set_countries.clear()
print(set_countries)
print(len(set_countries))
