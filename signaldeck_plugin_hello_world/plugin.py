from flask import Blueprint

bp = Blueprint(
    "hello_world",                 # blueprint name
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/plugin/hello-world",   # optional: URLs für plugin views/static (views optional)
    static_url_path="/static",  # optional, verhindert static collisions
)

def register(app, ctx=None) -> None:
    """
    Called by signaldeck-core to register this plugin.
    ctx is optional here; blueprint registration doesn't need it.
    """
    app.register_blueprint(bp)
