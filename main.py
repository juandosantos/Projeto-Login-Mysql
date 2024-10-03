from flask import Flask
from routes.home_route import home_page
from routes.cliente_route import cliente_page
from routes.create_route import create_page

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_sessao'
app.register_blueprint(home_page)
app.register_blueprint(cliente_page, url_prefix="/client")
app.register_blueprint(create_page, url_prefix="/criar")


app.run(debug=True)