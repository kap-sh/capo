"""Generated from Smithy shape ``com.amazonaws.kendra#BasicAuthenticationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.host
    import capo_kendra.types.port
    import capo_kendra.types.secret_arn


class BasicAuthenticationConfiguration(TypedDict, closed=True):
    host: "capo_kendra.types.host.Host"
    """<p>The name of the website host you want to connect to using authentication credentials.</p> <p>For example, the host name of https://a.example.com/page1.html is "a.example.com".</p>"""
    port: "capo_kendra.types.port.Port"
    """<p>The port number of the website host you want to connect to using authentication credentials.</p> <p>For example, the port for https://a.example.com/page1.html is 443, the standard port for HTTPS.</p>"""
    credentials: "capo_kendra.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of an Secrets Manager secret. You create a secret to store your credentials in <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html">Secrets Manager</a> </p> <p>You use a secret if basic authentication credentials are required to connect to a website. The secret stores your credentials of user name and password.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BasicAuthenticationConfiguration) -> dict:
    out: dict = {}
    out["Host"] = value["host"]
    out["Port"] = value["port"]
    out["Credentials"] = value["credentials"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BasicAuthenticationConfiguration:
    out: BasicAuthenticationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Host") is not None:
        out["host"] = data["Host"]
    else:
        raise DeserializationError("BasicAuthenticationConfiguration.host required")
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    else:
        raise DeserializationError("BasicAuthenticationConfiguration.port required")
    if data.get("Credentials") is not None:
        out["credentials"] = data["Credentials"]
    else:
        raise DeserializationError(
            "BasicAuthenticationConfiguration.credentials required"
        )
    return out
