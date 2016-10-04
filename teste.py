from flask import Flask
from flask import request
from ldap3 import Server, Connection, ALL

app = Flask(__name__)
app.secret_key = 'dsajifjwq98f9qw8f98qw9fqwfkjqwofjw9qf89qw'

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if not try_login(username, password):
        return "Invalid credentials!"
    return "Login successfullly"

def try_login(username, password):
    try:
        server = Server('ldap://ipa.demo1.freeipa.org:389', get_info=ALL)
        Connection(server, 'uid={0}, cn=users, cn=accounts, dc=demo1, dc=freeipa, dc=org'.format(username), password, auto_bind=True)
        return True
    except:
        return False

if __name__=='__main__':
  app.run()