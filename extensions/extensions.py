filename = input("File name: ").strip().lower()
try:
    [name, ext] = filename.rsplit(".", 1)
    if ext == "gif":
        print("image/gif")
    elif ext == "jpg" or ext == "jpeg":
        print("image/jpeg")
    elif ext == "png":
        print("image/png")
    elif ext == "pdf":
        print("application/pdf")
    elif ext == "txt":
        print("text/plain")
    elif ext == "zip":
        print("application/zip")
    else:
        print("application/octet-stream")
except:
    print("application/octet-stream")
