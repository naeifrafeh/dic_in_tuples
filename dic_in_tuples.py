
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def mydic(my_dict):
    list = []
    for val in my_dict.items():
       list.append(val)
    return list



print mydic(my_dict)
    