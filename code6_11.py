names = list()
print("変更前のlistのidentity{}".format(id(names)))
names.append("松田")
print("変更後のlistのidentity{}".format(id(names)))

name = "松田"
print("変更前のlistのidentity{}".format(id(name)))
name = "スーパー" + name
print("変更後のlistのidentity{}".format(id(name)))