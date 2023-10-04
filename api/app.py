from flask import Flask, redirect, url_for, request
from alchemical.flask import Alchemical
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_mail import Mail
from apifairy import APIFairy
from config import Config, ProductionConfig
from elasticsearch import Elasticsearch

db = Alchemical()
migrate = Migrate()
ma = Marshmallow()
cors = CORS()
mail = Mail()
apifairy = APIFairy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(ProductionConfig)

    # extensions
    from api import models
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    if app.config['USE_CORS']:  # pragma: no branch
        cors.init_app(app)
    mail.init_app(app)
    apifairy.init_app(app)

    # blueprints
    from api.errors import bp_errors
    app.register_blueprint(bp_errors)

    from api.tokens import bp_tokens
    app.register_blueprint(bp_tokens, url_prefix='/api')

    from api.users import bp_users
    app.register_blueprint(bp_users, url_prefix='/api')

    from api.posts import bp_posts
    app.register_blueprint(bp_posts, url_prefix='/api')
    
    from api.fake import bp_fake
    app.register_blueprint(bp_fake)


    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
        if app.config['ELASTICSEARCH_URL'] else None

    # define the shell context
    @app.shell_context_processor
    def shell_context():  # pragma: no cover
        ctx = {'db': db}
        for attr in dir(models):
            model = getattr(models, attr)
            if hasattr(model, '__bases__') and \
                    db.Model in getattr(model, '__bases__'):
                ctx[attr] = model
        return ctx

    @app.route('/')
    def index():  # pragma: no cover
        return redirect(url_for('apifairy.docs'))

    @app.after_request
    def after_request(response):
        # Werkzeu sometimes does not flush the request body so we do it here
        request.get_data()
        return response

    return app
