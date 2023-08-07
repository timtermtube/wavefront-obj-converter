import json

# ref: https://en.wikipedia.org/wiki/Wavefront_.obj_file

def check_texture() -> bool:
    w = input('Type "Y" if you want to import valid texture, .mtl: ')
    if w == "Y" or w == "y":
        print ("It goes with texture.")
        return True
    else:
        print ("It goes without texture.")
        return False
    
def o_file(path: str):
    structure = {
        "v": [],
        "vt": [],
        "vn": [],
        "f": []
    }
    f = open(file=path, encoding="utf-8", mode="r")
    for l in f.readlines():
        if len(l) > 0: pass

        # a line of the .obj file that is splitted
        p_l = l.split(" ")

        # switchting type of object; v, vt, vn, vp, f, l
        match p_l[0]:
            case "v": # geometric vertices
                coordinate = [float(p_l[1]), float(p_l[2]), float(p_l[3])]
                if len(l) == 5: coordinate.append(float(p_l[4]))
                print (tuple(coordinate))
                structure["v"].append(tuple(coordinate))

            case "f": # polygonal face
                face = gen_face()
                for i in p_l[1::]:
                    # number of vertex_indices, vertex_texture, vertex_normal
                    v, vt, vn = i.split("/")
                    face["vertices"].append(structure["v"][int(v)-1])
                structure["f"].append(face)

            case "l": # line
                pass
            #case "vt": # texture coordinates
            #case "vn": # vertex normals

    f.close()
    return structure

def gen_file(s):
    pass

def gen_face():
    return {
        "type": "face",
        "vertices": []
    }
    
# IF_TEXTURE = check_texture()
PATH = input("Write the path of valid .obj file you want to convert: ")
s = o_file(PATH)
gen_file(s)

print(s)
