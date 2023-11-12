from db import db
import filetype
import re
class ValidarHincha:
    def __init__(self):
        self.errores =  []
    def validar(self, region, comuna, deportes,  transporte, nombre, email, telefono, comentario, conn):
        self.errores  = []
        pass
    def validarRegion(self, region):
        if int(region) < 1 or int(region) > 16:
            return True
        self.errores.append("region")
        return False
        
