
def run():
    from firebase_admin import credentials
    import firebase_admin, os

    path = './Clouix/Firebase'
    file = 'ideationology-4c639-firebase-adminsdk-5hfwu-5806b97f02.json'
    dir = os.path.join(path, file)

    # cred = credentials.Certificate(dir)
    cred = credentials.Certificate(file)

    url = 'https://ideationology-4c639-default-rtdb.asia-southeast1.firebasedatabase.app/'
    path = {'databaseURL' : url}

    if not firebase_admin._apps:
        # print('========> ', firebase_admin._apps)
        firebase_admin.initialize_app(cred, path)

    from firebase_admin import db
    refv = db.reference('counter/views')

    g = refv.get()
    g = g + 1
    refv.set(g)
    return g, url
