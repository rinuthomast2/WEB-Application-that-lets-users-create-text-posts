from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_restful import Api
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from flask import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'your-email'
app.config['MAIL_PASSWORD'] = 'your-password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=30)

db = SQLAlchemy(app)
jwt = JWTManager(app)
mail = Mail(app)
bcrypt = Bcrypt(app)
CORS(app)
api = Api(app)
migrate = Migrate(app, db)

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'My API'
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/api/posts', methods=['GET'])
@jwt_required()
def get_posts():
    search_query = request.args.get('q', '')
    posts = Post.search(search_query)
    return jsonify([p.serialize() for p in posts])

@app.route('/api/posts', methods=['POST'])
@jwt_required()
def create_post():
    data = request.json
    user = User.query.filter_by(email=get_jwt_identity()).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404
    post = Post(
        title=data['title'],
        content=data['content'],
        user_id=user.id
    )
    db.session.add(post)
    db.session.commit()
    return jsonify({'message': 'Post created successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
