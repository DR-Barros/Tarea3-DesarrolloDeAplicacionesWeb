from flask import Flask, render_template, request, redirect, url_for
from db import db
from utils.validations import *
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os

UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

conn = db.getConection()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agregar-hincha')
def agregarHincha():
    return render_template('agregar-hincha.html')

@app.route('/agregar-artesano')
def agregarArtesano():
    tiposArtesania = db.getTipoArtesania(conn)
    region = db.getRegion(conn)
    comuna = db.getComuna(conn)
    return render_template('agregar-artesano.html', tipos = tiposArtesania, regiones = region, comunas = comuna)

@app.route('/informacion-hincha')
def informacionHincha():
    return render_template('informacion-hincha.html')

@app.route('/informacion-artesano-<num>')
def informacionArtesano(num):
    try: 
        n = int(num)
    except:
        return redirect("ver-artesanos")
    informacion = db.getArtesanoById(conn, n)
    if informacion == None:
        return redirect("ver-artesanos")
    foto = db.getArtesanoFotoById(conn, n)
    tipo = db.getArtesanoTipoById(conn, n)
    return render_template('informacion-artesano.html', artesano = informacion, fotos=foto, tipos = tipo)

@app.route('/ver-hinchas')
def verHinchas():
    return render_template('ver-hinchas.html')

@app.route('/ver-artesanos')
def verArtesanos():
    artesano = db.getArtesanos(conn, 0)
    foto = db.getArtesanoFoto(conn, 0)
    tipo = db.getArtesanoTipo(conn, 0)
    cant = db.getCantArtesanos(conn)
    show = 5 < cant
    return render_template('ver-artesanos.html', artesanos = artesano, fotos=foto, tipos = tipo, n=0, ant= 0, sig=1, mostrar = show)

@app.route('/ver-artesanos<num>')
def verArtesanos_param(num):
    numero = 5*int(num)
    num = int(num)
    artesano = db.getArtesanos(conn, numero)
    foto = db.getArtesanoFoto(conn, numero)
    tipo = db.getArtesanoTipo(conn, numero)
    cant = db.getCantArtesanos(conn)
    print(cant)
    show = numero+5 < cant
    return render_template('ver-artesanos.html', artesanos = artesano, fotos=foto, tipos = tipo, n =num, ant=num-1, sig=num+1, mostrar = show)


@app.route('/post-artesanos', methods=['POST'])
def post_artesano():
     if request.method == 'POST':
        region = request.form.get("region")
        comuna = request.form.get("comuna")
        artesania = request.form.getlist("artesania")
        descripcion = request.form.get("descripcion")
        photo = request.files.get("photo")
        photo2 = request.files.get("photo2")
        photo3 = request.files.get("photo3")
        nombre = request.form.get("name")
        email = request.form.get("mail")
        telefono = request.form.get("phone")
        if validarArtesano(region, comuna, artesania, photo, photo2, photo3, nombre, email, telefono, conn):
            #agregar artesano a la base de datos
            db.addArtesano(conn, comuna, descripcion, nombre, email, telefono)
            artesano = db.getLastId(conn)[0][0]
            #agreagar el tipo del artesano
            for t in artesania:
                db.addArtesanoTipo(conn, t, artesano)

            #agregar las fotos si corresponde
            if photo != None and photo.filename != "" :
                _filename = hashlib.sha256(
                    secure_filename(photo.filename) # nombre del archivo
                    .encode("utf-8") # encodear a bytes
                    ).hexdigest()
                _extension = filetype.guess(photo).extension
                img_filename = f"{_filename}.{_extension}"

                # 2. save img as a file
                photo.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))
                # subir link a la base dato
                db.addArtesanoFoto(conn, app.config["UPLOAD_FOLDER"], img_filename, artesano)
            if photo2 != None and photo2.filename != "" :
                _filename = hashlib.sha256(
                    secure_filename(photo2.filename) # nombre del archivo
                    .encode("utf-8") # encodear a bytes
                    ).hexdigest()
                _extension = filetype.guess(photo2).extension
                img2_filename = f"{_filename}.{_extension}"

                # 2. save img as a file
                photo2.save(os.path.join(app.config["UPLOAD_FOLDER"], img2_filename))
                # subir link a la base dato
                db.addArtesanoFoto(conn, app.config["UPLOAD_FOLDER"], img2_filename, artesano)
            if photo3 != None and photo3.filename != "" :
                _filename = hashlib.sha256(
                    secure_filename(photo3.filename) # nombre del archivo
                    .encode("utf-8") # encodear a bytes
                    ).hexdigest()
                _extension = filetype.guess(photo3).extension
                img3_filename = f"{_filename}.{_extension}"

                # 2. save img as a file
                photo3.save(os.path.join(app.config["UPLOAD_FOLDER"], img3_filename))
                # subir link a la base dato
                db.addArtesanoFoto(conn, app.config["UPLOAD_FOLDER"], img3_filename, artesano)
            
            return redirect(url_for("index"))
        else:
            tiposArtesania = db.getTipoArtesania(conn)
            return redirect(url_for("agregarArtesano"))

if __name__ == '__main__':
    app.run(debug=True)