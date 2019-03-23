def ConvertToUnix(date):
    down = date.split("-")
    uma = []
    for i in down:
        uma.append(int(i))
    return 31556926*(uma[0]-1970)+uma[1]*2629743+uma[2]*86400