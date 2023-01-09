def write_link(link):
    try:
        has_link = False
        with open("links.txt","r") as file:
            lines = file.readlines()
            for l in lines:
                if link == l[:len(l)-1]:
                    has_link = True
        if has_link == False:
            with open("links.txt","a") as file:
                file.write(link+"\n")  
            return True 
        return False
    except:
        return False



