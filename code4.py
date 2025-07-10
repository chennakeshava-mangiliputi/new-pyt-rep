with open('data.txt',"w") as f:
    f.write("Hey I'm practicing python ")
with open('data.txt',"a") as f:
    f.write("Wanna join with me?")
with open('data.txt',"r") as f:
    file_text=f.read()
cnt=file_text.split()
print(len(cnt))