"""
Example Chalice application exploring integrating variour tooling
"""
# pylint: disable=W0613,C0103
from typing import Any, Dict

from aws_lambda_context import LambdaContext
from chalice import Chalice  # type: ignore

from chalicelib import RESPONSE
from chalicelib.config import conf

app = Chalice(app_name="snyker")


@app.route("/")
def index() -> Dict[str, str]:
    """Automatically creates an API Gateway"""
    return {"hello": conf["VALUE"]}
    #return RESPONSE


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
