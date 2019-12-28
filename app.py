"""
Example Chalice application exploring integrating variour tooling
"""

# pylint: disable=unused-argument

from typing import Any, Dict

from aws_lambda_context import LambdaContext
from chalice import Chalice  # type: ignore

from chalicelib.config import ParameterStoreConfig
from chalicelib.logging import configure_logging

app = Chalice(app_name="snyker", debug=False)  # pylint: disable=invalid-name
configure_logging(app)
config = ParameterStoreConfig("snyker")  # pylint: disable=invalid-name


@app.route("/")
def index() -> Dict[str, str]:
    """Automatically creates an API Gateway"""
    app.log.info("This is an info statement")
    app.log.debug("This is a debug statement")
    return {"hello": config["VALUE"]}


@app.lambda_function()
def function(event: Any, context: LambdaContext) -> Dict[str, str]:
    """Raw lambda function"""
    return {"hello": "function"}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
