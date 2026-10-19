"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ApiKeyCredentialProviderItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore_control.types.api_key_credential_provider_arn_type
    import capo_bedrock_agentcore_control.types.credential_provider_name


class ApiKeyCredentialProviderItem(TypedDict, closed=True):
    name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName"
    """<p>The name of the API key credential provider.</p>"""
    credential_provider_arn: "capo_bedrock_agentcore_control.types.api_key_credential_provider_arn_type.ApiKeyCredentialProviderArnType"
    """<p>The Amazon Resource Name (ARN) of the API key credential provider.</p>"""
    created_time: "datetime.datetime"
    """<p>The timestamp when the API key credential provider was created.</p>"""
    last_updated_time: "datetime.datetime"
    """<p>The timestamp when the API key credential provider was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiKeyCredentialProviderItem) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["credentialProviderArn"] = value["credential_provider_arn"]
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["createdTime"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["created_time"]
        )
    )
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["lastUpdatedTime"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["last_updated_time"]
        )
    )
    return out


def deserialize_json(data: dict) -> ApiKeyCredentialProviderItem:
    out: ApiKeyCredentialProviderItem = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("credentialProviderArn") is not None:
        out["credential_provider_arn"] = data["credentialProviderArn"]
    else:
        out["credential_provider_arn"] = ""
    if data.get("createdTime") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["created_time"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["createdTime"]
            )
        )
    else:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("lastUpdatedTime") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["last_updated_time"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedTime"]
            )
        )
    else:
        import datetime

        out["last_updated_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
