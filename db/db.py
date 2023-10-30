import pymysql

def getConection():
    conn = pymysql.connect(
        db='tarea2',
        user= 'cc5002',
        passwd= 'programacionweb',
        host= 'localhost',
        charset='utf8'
    )
    return conn

#devuelve un array con los tipos de las artesanias
def getTipoArtesania(conn):
    sql = "SELECT * FROM tipo_artesania"
    cursor = conn.cursor()
    cursor.execute(sql)
    tipos = cursor.fetchall()
    cursor.close()
    return tipos

#devuelve un array con (id, región)
def getRegion(conn):
    sql = "SELECT * FROM region"
    cursor = conn.cursor()
    cursor.execute(sql)
    region = cursor.fetchall()
    cursor.close()
    return region

#devuelve un array con (id, nombre, región_id)
def getComuna(conn):
    sql = "SELECT * FROM comuna"
    cursor = conn.cursor()
    cursor.execute(sql)
    comuna = cursor.fetchall()
    cursor.close()
    return comuna


def getCantArtesanos(conn):
    sql = "SELECT count(*) FROM artesano"
    cursor = conn.cursor()
    cursor.execute(sql)
    cant = cursor.fetchall()
    cursor.close()
    cursor.close()
    return cant[0][0]

def getArtesanos(conn, n):
    sql = "SELECT a.id, c.nombre, a.nombre, celular FROM artesano a, comuna c WHERE a.comuna_id = c.id ORDER BY id DESC LIMIT %s, 5"
    cursor = conn.cursor()
    cursor.execute(sql, (n))
    artesanos = cursor.fetchall()
    cursor.close()
    return artesanos

def getArtesanoFoto(conn, n):
    sql = "SELECT a.id, ruta_archivo, nombre_archivo FROM foto, (SELECT id FROM artesano ORDER BY id DESC LIMIT %s, 5) a WHERE artesano_id = a.id "
    cursor = conn.cursor()
    cursor.execute(sql, (n))
    fotos = cursor.fetchall()
    cursor.close()
    return fotos

def getArtesanoTipo(conn, n):
    sql = "SELECT ta.nombre, a.id FROM tipo_artesania ta, artesano_tipo at, (SELECT id FROM artesano ORDER BY id DESC LIMIT %s, 5) a WHERE at.artesano_id = a.id AND  at.tipo_artesania_id = ta.id"
    cursor = conn.cursor()
    cursor.execute(sql, (n))
    tipos = cursor.fetchall()
    cursor.close()
    return tipos

def getArtesanoById(conn, id):
    sql = "SELECT a.nombre, r.nombre, c.nombre, email, celular, descripcion_artesania FROM artesano a, comuna c, region r WHERE a.id = %s AND a.comuna_id = c.id AND c.region_id = r.id"
    cursor = conn.cursor()
    cursor.execute(sql, (id))
    artesano = cursor.fetchall()
    cursor.close()
    if len(artesano) == 0:
        return None
    return artesano[0]

def getArtesanoTipoById(conn, id):
    sql = "SELECT ta.nombre FROM tipo_artesania ta, artesano_tipo at WHERE at.artesano_id = %s AND  at.tipo_artesania_id = ta.id"
    cursor = conn.cursor()
    cursor.execute(sql, (id))
    tipos = cursor.fetchall()
    cursor.close()
    return tipos

def getArtesanoFotoById(conn, id):
    sql = "SELECT ruta_archivo, nombre_archivo FROM foto WHERE artesano_id = %s"
    cursor = conn.cursor()
    cursor.execute(sql, (id))
    fotos = cursor.fetchall()
    cursor.close()
    return fotos

def getLastId(conn):
    sql ="SELECT LAST_INSERT_ID()"
    cursor = conn.cursor()
    cursor.execute(sql)
    id = cursor.fetchall()
    cursor.close()
    return id

def getDeportes(conn):
    sql ="SELECT * FROM deporte"
    cursor = conn.cursor()
    cursor.execute(sql)
    d = cursor.fetchall()
    cursor.close()
    return d

def addArtesano(conn, comuna, descripcion, nombre, email, celular):
    sql = "INSERT INTO artesano (comuna_id, descripcion_artesania, nombre, email, celular) VALUES (%s,%s,%s,%s,%s)"
    cursor = conn.cursor()
    cursor.execute(sql, (comuna, descripcion, nombre, email, celular))
    conn.commit()
    cursor.close()

def addArtesanoTipo(conn, tipo, artesano):
    cursor = conn.cursor()
    sql = "INSERT INTO artesano_tipo (artesano_id, tipo_artesania_id) VALUES (%s,%s)"
    cursor.execute(sql, (artesano, tipo))
    conn.commit()
    cursor.close()

def addArtesanoFoto(conn, ruta, foto, artesano):
    cursor = conn.cursor()
    sql = "INSERT INTO foto (ruta_archivo, nombre_archivo, artesano_id) VALUES (%s,%s,%s)"
    cursor.execute(sql, (ruta, foto, artesano))
    conn.commit()
    cursor.close()
