from app import app
 
@app.route('/auth')
def auths():
    return 'auth'