from db import db
import re
class ValidarHincha:
    def __init__(self):
        self.errores =  []

    def validar(self, region, comuna, deportes,  transporte, nombre, email, telefono, comentario, conn):
        self.errores  = []
        return (self.validarRegion(region) and self.validarComuna(region, comuna, conn) and self.validarDeportes(deportes) 
                and self.validarTransporte(transporte) and self.validarNombre(nombre) and self.validarMail(email) 
                and self.validarCelular(telefono) and self.validarComentario(comentario), self.errores)

    def validarRegion(self, region):
        if int(region) < 1 or int(region) > 16:
            self.errores.append("region")
            return False
        return True
    
    def validarComuna(self, region, comuna, conn):
        possibleComuna = db.getComuna(conn)
        for com in possibleComuna:
            if com[0] == int(comuna):
                if int(region) != com[2]:
                    self.errores.append("region")
                    return False
                else:
                    return True
        self.errores.append("region")
        return False
    
    def validarDeportes(self, deportes):
        for t in deportes:
            if int(t) < 1 or int(t) > 60:
                self.errores.append("deporte")
                return False
        return True
            
    def validarTransporte(self, transporte):
        if transporte != "particular" and transporte != "locomoción pública":
            self.errores.append("deporte")
            return False
        return True
    
    def validarNombre(self, nombre):
        if len(nombre) < 3 or len(nombre) >80:
            self.errores.append("nombre")
            return False
        return True
    
    def validarMail(self, email):
        exprReg = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(exprReg, email):
            self.errores.append("mail")
            return False
        return True
    
    def validarCelular(self, telefono):
        exprReg = r'^(\+569|9)\d{8}$'
        if not re.match(exprReg, telefono):
            self.errores.append("celular")
            return False
        return True
    
    def validarComentario(self, comentario):
        if  len(comentario) > 80:
            self.errores.append("comentario")
            return False
        return True