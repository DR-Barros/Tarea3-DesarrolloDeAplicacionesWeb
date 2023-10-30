from db import db
import filetype
import re

#devuelve true si es valido y los errores si no lo es
def validarArtesano(region, comuna, artesanias, photo, photo2, photo3, nombre, email, telefono, conn):
    if int(region) < 1 or int(region) > 16:
        print("region invalido")
        return False
    #validar Comuna
    com = validarComuna(comuna, conn)
    print(com)
    if com == -1 or int(region) != com:
        print("comuna invalido")
        return False
    #validar tipos
    for t in artesanias:
        if int(t) < 1 or int(t) > 9:
            print("tipo invalido")
            return False

    #validar fotos
    if not (validarImg(photo) and  photo != None and photo.filename != ""):
        print("foto1 invalido")
        return False
    
    if  photo2 != None and photo2.filename != "":
        if not validarImg(photo2):
            print("foto2 invalido")
            return False
    
    if  photo3 != None and photo3.filename != "":
        if not validarImg(photo3):
            print("foto3 invalido")
            return False


    #nombre
    if len(nombre) < 3 or len(nombre) >80:
        print("Nombre invalido")
        return False
     
    #mail
    exprReg = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(exprReg, email):
        print("mail invalido")
        return False

    #celular
    exprReg = r'^(\+569|9)\d{8}$'
    if not re.match(exprReg, telefono):
        print("celu invalido")
        return False

    #si paso todo devolver True
    return True

def validarHincha(region, comuna, deportes, nombre, email, telefono, conn):
    pass

#devuelve el id de la region, devuelve -1 si no la encuentra
def validarComuna(comuna, conn):
    possibleComuna = db.getComuna(conn)
    for com in possibleComuna:
        if com[0] == int(comuna):
            return com[2]
    return -1 

def validarImg(conf_img):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}
    
    # check file extension
    ftype_guess = filetype.guess(conf_img)
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    # check mimetype
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    return True