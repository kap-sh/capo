"""Generated from Smithy shape ``com.amazonaws.kendra#ProxyConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.host
    import capo_kendra.types.port
    import capo_kendra.types.secret_arn


class ProxyConfiguration(TypedDict, closed=True):
    host: "capo_kendra.types.host.Host"
    """<p>The name of the website host you want to connect to via a web proxy server.</p> <p>For example, the host name of https://a.example.com/page1.html is "a.example.com".</p>"""
    port: "capo_kendra.types.port.Port"
    """<p>The port number of the website host you want to connect to via a web proxy server. </p> <p>For example, the port for https://a.example.com/page1.html is 443, the standard port for HTTPS.</p>"""
    credentials: NotRequired["capo_kendra.types.secret_arn.SecretArn"]
    """<p>The Amazon Resource Name (ARN) of an Secrets Manager secret. You create a secret to store your credentials in <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html">Secrets Manager</a> </p> <p>The credentials are optional. You use a secret if web proxy credentials are required to connect to a website host. Amazon Kendra currently support basic authentication to connect to a web proxy server. The secret stores your credentials.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProxyConfiguration) -> dict:
    out: dict = {}
    out["Host"] = value["host"]
    out["Port"] = value["port"]
    if "credentials" in value:
        out["Credentials"] = value["credentials"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProxyConfiguration:
    out: ProxyConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Host") is not None:
        out["host"] = data["Host"]
    else:
        raise DeserializationError("ProxyConfiguration.host required")
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    else:
        raise DeserializationError("ProxyConfiguration.port required")
    if data.get("Credentials") is not None:
        out["credentials"] = data["Credentials"]
    return out
