'''
calculate the sizes given the short side of a 
single piece of paper
'''
import const
import math

intro = '''
um, you need some data somehow
'''

corners = {
    "orig": 0.4040610178,
    "beast": 0.3181818182,
    "beast_long":0.3374827819,
    "Sentinelle_dell_Energia":0.4242640687,
    "kids long":0.3636363636,
    "kids":	0.3181818182
}

def definput(prompt, given):
    val=input(prompt)
    if len(val) == 0:
        return float(given)
    else:
        return float(val)


def convertall(base=None,width=None,from_center=None,sqwidth=None,
               corner_ratio=None):


    if width and corner_ratio:
        print("width, corner_ratio: {} {}".format(width, corner_ratio))
        sqwidth = width / 2
        from_center = sqwidth * corner_ratio
        base=math.sqrt(math.pow(from_center,2) * 2 )
        
    elif width and base:
        print("width, base: {} {}".format(width, base))
        sqwidth = width/2
        from_center = math.sqrt(math.pow(from_center,2) / 2 )
        corner_ratio = from_center / sqwidth
        

    elif sqwidth and corner_ratio:
        width= 2 * sqwidth
        base = width * corner_ratio
    elif corner_ratio and base:
        from_center= math.sqrt(math.pow(base,2)/2)
        sqwidth= from_center / corner_ratio
        width= sqwidth*2
        
    else:
        print("you need two specify at least two values")
        return
    # from_center = math.sqrt(math.pow(base, 2)/2)
    print("total width: {}".format(width))

    print("square width: {}".format(sqwidth))
    print("base size: {}".format(base))
    print("corner_ratio: {}".format(corner_ratio))
    from_center = math.sqrt(math.pow(base, 2)/2)
    print("measure {} from center".format(from_center))



if __name__ == "__main__":
    # width = float(input("enter sheet width: "))
    # convertall(width=width, corner_ratio=.404)
    base = definput("enter base (3 5/16)", 3 + 5/16.0)
    for x in ["orig", "beast", "kids long"]:
        print('============{}==============='.format(x))
        convertall(base,corner_ratio=corners[x])
    width= definput('enter width(8.5)', 8.5)
    for x in ["orig", "beast", "kids long"]:
        print('============{}==============='.format(x))
        convertall(width=width,corner_ratio=corners[x])