from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from db import db
from utils.validations import *
import utils.validarHincha as vh
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os

UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'tu_clave_secreta'

@app.route('/')
def index():
    state = session.get('state')
    session['state'] = None
    return render_template('index.html', state=state)


@app.route('/agregar-hincha')
def agregarHincha():
    conn = db.getConection()
    deportes = db.getDeportes(conn)
    region = db.getRegion(conn)
    comuna = db.getComuna(conn)
    conn.close()
    return render_template('agregar-hincha.html', dep = deportes, regiones = region, comunas = comuna)

@app.route('/agregar-artesano')
def agregarArtesano():
    conn = db.getConection()
    tiposArtesania = db.getTipoArtesania(conn)
    region = db.getRegion(conn)
    comuna = db.getComuna(conn)
    conn.close()
    return render_template('agregar-artesano.html', tipos = tiposArtesania, regiones = region, comunas = comuna)

@app.route('/informacion-hincha-<num>')
def informacionHincha(num):
    try: 
        n = int(num)
    except:
        print("fallo cambiar numero")
        return redirect("ver-hinchas")
    conn = db.getConection()
    informacion = db.getHinchaById(conn, n)
    if informacion == None:
        conn.close()
        return redirect("ver-hinchas")
    deporte = db.getHinchaDeporById(conn, n)
    conn.close()
    return render_template('informacion-hincha.html', hincha = informacion, deportes = deporte)

@app.route('/informacion-artesano-<num>')
def informacionArtesano(num): 
    try: 
        n = int(num)
    except:
        return redirect("ver-artesanos")
    conn = db.getConection()
    informacion = db.getArtesanoById(conn, n)
    if informacion == None:
        conn.close()
        return redirect("ver-artesanos")
    foto = db.getArtesanoFotoById(conn, n)
    tipo = db.getArtesanoTipoById(conn, n)
    conn.close()
    return render_template('informacion-artesano.html', artesano = informacion, fotos=foto, tipos = tipo)

@app.route('/ver-hinchas')
def verHinchas():
    conn = db.getConection()
    hincha = db.getHinchas(conn, 0)
    deportes = db.getHinchaDeportes(conn, 0)
    cant = db.getCantHinchas(conn)
    conn.close()
    show = 5 < cant
    return render_template('ver-hinchas.html', hinchas=hincha, deportes=deportes, n=0, ant=0, sig=1, mostrar =show)

@app.route('/ver-hinchas<num>')
def verHinchas_param(num):
    conn = db.getConection()
    numero = 5*int(num)
    num = int(num)
    hincha = db.getHinchas(conn, numero)
    deportes = db.getHinchaDeportes(conn, numero)
    cant = db.getCantHinchas(conn)
    conn.close()
    show = numero+5 < cant
    return render_template('ver-hinchas.html', hinchas=hincha, deportes=deportes, n=num, ant=num-1, sig=num+1, mostrar =show)

@app.route('/ver-artesanos')
def verArtesanos():
    conn = db.getConection()
    artesano = db.getArtesanos(conn, 0)
    foto = db.getArtesanoFoto(conn, 0)
    tipo = db.getArtesanoTipo(conn, 0)
    cant = db.getCantArtesanos(conn)
    conn.close()
    show = 5 < cant
    return render_template('ver-artesanos.html', artesanos = artesano, fotos=foto, tipos = tipo, n=0, ant= 0, sig=1, mostrar = show)

@app.route('/ver-artesanos<num>')
def verArtesanos_param(num):
    conn = db.getConection()
    numero = 5*int(num)
    num = int(num)
    artesano = db.getArtesanos(conn, numero)
    foto = db.getArtesanoFoto(conn, numero)
    tipo = db.getArtesanoTipo(conn, numero)
    cant = db.getCantArtesanos(conn)
    conn.close()
    show = numero+5 < cant
    return render_template('ver-artesanos.html', artesanos = artesano, fotos=foto, tipos = tipo, n =num, ant=num-1, sig=num+1, mostrar = show)

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/post-artesanos', methods=['POST'])
def post_artesano():
    conn = db.getConection()
    region = request.form.get("region")
    comuna = request.form.get("comuna")
    artesania = request.form.getlist("artesania")
    descripcion = request.form.get("descripcion")
    photo = request.files.get("photo")
    photo2 = request.files.get("photo2")
    photo3 = request.files.get("photo3")
    nombre = request.form.get("name").strip()
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
        conn.close()
        session['state'] = "Se creo el artesano con exito"
        return redirect(url_for("index"))
    else:
        conn.close()
        return redirect(url_for("agregarArtesano"))

@app.route('/post-hinchas', methods=['POST'])
def post_hinchas():
    conn = db.getConection()
    region = request.form.get("region")
    comuna = request.form.get("comuna")
    deportes = request.form.getlist("deportes")
    transporte = request.form.get("transporte")
    nombre = request.form.get("name").strip()
    email = request.form.get("mail")
    telefono = request.form.get("phone")
    comentario = request.form.get("coment")
    validar = vh.ValidarHincha()
    valido, errores = validar.validar(region, comuna, deportes, transporte, nombre, email, telefono, comentario, conn)
    if valido:
        db.addHincha(conn, comuna, transporte, nombre, email, telefono, comentario)
        hincha = db.getLastId(conn)[0][0]
        for d in deportes:
            db.addHinchaDeporte(conn, d, hincha)
        conn.close()
        session['state'] = "Se creo el hincha  con exito"
        return jsonify("exito")
    else:
        print(errores)
        conn.close()
        return jsonify(errores)

@app.route('/artesano-data')
def artesanoData():
    conn = db.getConection()
    cursor = conn.cursor()
    sql = "SELECT t.nombre, COUNT(artesano_id) FROM artesano_tipo a, tipo_artesania t WHERE a.tipo_artesania_id = t.id GROUP BY t.nombre"
    cursor.execute(sql)
    tipos = cursor.fetchall()
    cursor.close
    conn.close
    return jsonify(tipos)

@app.route('/hincha-data')
def hinchaData():
    conn = db.getConection()
    cursor = conn.cursor()
    sql = "SELECT d.nombre, COUNT(h.hincha_id) FROM hincha_deporte h, deporte d WHERE d.id = h.deporte_id GROUP BY d.id"
    cursor.execute(sql)
    tipos = cursor.fetchall()
    cursor.close
    conn.close
    return jsonify(tipos)


if __name__ == '__main__':
    app.run(debug=True)