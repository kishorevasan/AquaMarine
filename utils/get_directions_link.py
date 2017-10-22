#ORIGIN AND DEST IS A SET OF (LAT,LANG)
def getdirectionslink(origin,dest):
    return("https://www.google.de/maps/dir/"+str(origin[0])+","+str(origin[1])+"/"+str(dest[0])+","+str(dest[1])+"/")