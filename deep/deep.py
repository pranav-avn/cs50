ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
if(ans.strip() == "42"):
    print("Yes")
elif(ans.strip().lower() == "forty-two" or ans.strip().lower() == "forty two"):
    print("Yes")
else:
    print("No")
