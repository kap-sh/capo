"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#CreateAppInstanceBotRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_identity.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.chime_arn
    import capo_chime_sdk_identity.types.client_request_token
    import capo_chime_sdk_identity.types.configuration
    import capo_chime_sdk_identity.types.metadata
    import capo_chime_sdk_identity.types.resource_name
    import capo_chime_sdk_identity.types.tag_list


class CreateAppInstanceBotRequest(TypedDict, closed=True):
    app_instance_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstance</code> request.</p>"""
    name: NotRequired["capo_chime_sdk_identity.types.resource_name.ResourceName"]
    """<p>The user's name.</p>"""
    metadata: NotRequired["capo_chime_sdk_identity.types.metadata.Metadata"]
    """<p>The request metadata. Limited to a 1KB string in UTF-8.</p>"""
    client_request_token: (
        "capo_chime_sdk_identity.types.client_request_token.ClientRequestToken"
    )
    """<p>The unique ID for the client making the request. Use different tokens for different <code>AppInstanceBots</code>.</p>"""
    tags: NotRequired["capo_chime_sdk_identity.types.tag_list.TagList"]
    """<p>The tags assigned to the <code>AppInstanceBot</code>.</p>"""
    configuration: "capo_chime_sdk_identity.types.configuration.Configuration"
    """<p>Configuration information about the Amazon Lex V2 V2 bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAppInstanceBotRequest) -> dict:
    out: dict = {}
    out["AppInstanceArn"] = value["app_instance_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_chime_sdk_identity.types.tag_list

        out["Tags"] = capo_chime_sdk_identity.types.tag_list.serialize_json(
            value["tags"]
        )
    import capo_chime_sdk_identity.types.configuration

    out["Configuration"] = capo_chime_sdk_identity.types.configuration.serialize_json(
        value["configuration"]
    )
    return out


def deserialize_json(data: dict) -> CreateAppInstanceBotRequest:
    out: CreateAppInstanceBotRequest = {}  # type: ignore[typeddict-item]
    if data.get("AppInstanceArn") is not None:
        out["app_instance_arn"] = data["AppInstanceArn"]
    else:
        out["app_instance_arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Metadata") is not None:
        out["metadata"] = data["Metadata"]
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    else:
        out["client_request_token"] = ""
    if data.get("Tags") is not None:
        import capo_chime_sdk_identity.types.tag_list

        out["tags"] = capo_chime_sdk_identity.types.tag_list.deserialize_json(
            data["Tags"]
        )
    if data.get("Configuration") is not None:
        import capo_chime_sdk_identity.types.configuration

        out["configuration"] = (
            capo_chime_sdk_identity.types.configuration.deserialize_json(
                data["Configuration"]
            )
        )
    else:
        raise DeserializationError("CreateAppInstanceBotRequest.configuration required")
    return out


def redact_sensitive(value: CreateAppInstanceBotRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "metadata" in value:
        out["metadata"] = "*** Sensitive Data Redacted ***"
    if "tags" in value:
        import capo_chime_sdk_identity.types.tag_list

        out["tags"] = capo_chime_sdk_identity.types.tag_list.redact_sensitive(
            value["tags"]
        )
    return out
