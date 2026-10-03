"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ConfluenceSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.confluence_auth_type
    import capo_bedrock_agent.types.confluence_host_type
    import capo_bedrock_agent.types.https_url
    import capo_bedrock_agent.types.secret_arn


class ConfluenceSourceConfiguration(TypedDict, closed=True):
    host_url: "capo_bedrock_agent.types.https_url.HttpsUrl"
    """<p>The Confluence host URL or instance URL.</p>"""
    host_type: "capo_bedrock_agent.types.confluence_host_type.ConfluenceHostType"
    """<p>The supported host type, whether online/cloud or server/on-premises.</p>"""
    auth_type: "capo_bedrock_agent.types.confluence_auth_type.ConfluenceAuthType"
    """<p>The supported authentication type to authenticate and connect to your Confluence instance.</p>"""
    credentials_secret_arn: "capo_bedrock_agent.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name of an Secrets Manager secret that stores your authentication credentials for your Confluence instance URL. For more information on the key-value pairs that must be included in your secret, depending on your authentication type, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/confluence-data-source-connector.html#configuration-confluence-connector">Confluence connection configuration</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfluenceSourceConfiguration) -> dict:
    out: dict = {}
    out["hostUrl"] = value["host_url"]
    import capo_bedrock_agent.types.confluence_host_type

    out["hostType"] = capo_bedrock_agent.types.confluence_host_type.serialize_json(
        value["host_type"]
    )
    import capo_bedrock_agent.types.confluence_auth_type

    out["authType"] = capo_bedrock_agent.types.confluence_auth_type.serialize_json(
        value["auth_type"]
    )
    out["credentialsSecretArn"] = value["credentials_secret_arn"]
    return out


def deserialize_json(data: dict) -> ConfluenceSourceConfiguration:
    out: ConfluenceSourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("hostUrl") is not None:
        out["host_url"] = data["hostUrl"]
    else:
        raise DeserializationError("ConfluenceSourceConfiguration.host_url required")
    if data.get("hostType") is not None:
        import capo_bedrock_agent.types.confluence_host_type

        out["host_type"] = (
            capo_bedrock_agent.types.confluence_host_type.deserialize_json(
                data["hostType"]
            )
        )
    else:
        raise DeserializationError("ConfluenceSourceConfiguration.host_type required")
    if data.get("authType") is not None:
        import capo_bedrock_agent.types.confluence_auth_type

        out["auth_type"] = (
            capo_bedrock_agent.types.confluence_auth_type.deserialize_json(
                data["authType"]
            )
        )
    else:
        raise DeserializationError("ConfluenceSourceConfiguration.auth_type required")
    if data.get("credentialsSecretArn") is not None:
        out["credentials_secret_arn"] = data["credentialsSecretArn"]
    else:
        raise DeserializationError(
            "ConfluenceSourceConfiguration.credentials_secret_arn required"
        )
    return out
