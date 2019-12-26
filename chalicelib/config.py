import boto3


def get_param(param_name):
    """
    This function reads a secure parameter from AWS' SSM service.
    The request must be passed a valid parameter name, as well as
    temporary credentials which can be used to access the parameter.
    The parameter's value is returned.
    """
    # Create the SSM Client
    ssm = boto3.client("ssm")

    # Get the requested parameter
    response = ssm.get_parameters(Names=[param_name], WithDecryption=True)

    # Store the credentials in a variable
    result = response["Parameters"][0]["Value"]

    return result

conf = {"VALUE": get_param("/snyker/VALUE")}
