"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CreateVoiceProfileDomainRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.client_request_id
    import capo_chime_sdk_voice.types.server_side_encryption_configuration
    import capo_chime_sdk_voice.types.tag_list
    import capo_chime_sdk_voice.types.voice_profile_domain_description
    import capo_chime_sdk_voice.types.voice_profile_domain_name


class CreateVoiceProfileDomainRequest(TypedDict, closed=True):
    name: "capo_chime_sdk_voice.types.voice_profile_domain_name.VoiceProfileDomainName"
    """<p>The name of the voice profile domain.</p>"""
    description: NotRequired[
        "capo_chime_sdk_voice.types.voice_profile_domain_description.VoiceProfileDomainDescription"
    ]
    """<p>A description of the voice profile domain.</p>"""
    server_side_encryption_configuration: "capo_chime_sdk_voice.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    """<p>The server-side encryption configuration for the request.</p>"""
    client_request_token: NotRequired[
        "capo_chime_sdk_voice.types.client_request_id.ClientRequestId"
    ]
    """<p>The unique identifier for the client request. Use a different token for different domain creation requests.</p>"""
    tags: NotRequired["capo_chime_sdk_voice.types.tag_list.TagList"]
    """<p>The tags assigned to the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVoiceProfileDomainRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_chime_sdk_voice.types.server_side_encryption_configuration

    out["ServerSideEncryptionConfiguration"] = (
        capo_chime_sdk_voice.types.server_side_encryption_configuration.serialize_json(
            value["server_side_encryption_configuration"]
        )
    )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_chime_sdk_voice.types.tag_list

        out["Tags"] = capo_chime_sdk_voice.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateVoiceProfileDomainRequest:
    out: CreateVoiceProfileDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateVoiceProfileDomainRequest.name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ServerSideEncryptionConfiguration") is not None:
        import capo_chime_sdk_voice.types.server_side_encryption_configuration

        out["server_side_encryption_configuration"] = (
            capo_chime_sdk_voice.types.server_side_encryption_configuration.deserialize_json(
                data["ServerSideEncryptionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateVoiceProfileDomainRequest.server_side_encryption_configuration required"
        )
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("Tags") is not None:
        import capo_chime_sdk_voice.types.tag_list

        out["tags"] = capo_chime_sdk_voice.types.tag_list.deserialize_json(data["Tags"])
    return out


def redact_sensitive(value: CreateVoiceProfileDomainRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "server_side_encryption_configuration" in value:
        import capo_chime_sdk_voice.types.server_side_encryption_configuration

        out["server_side_encryption_configuration"] = (
            capo_chime_sdk_voice.types.server_side_encryption_configuration.redact_sensitive(
                value["server_side_encryption_configuration"]
            )
        )
    if "tags" in value:
        import capo_chime_sdk_voice.types.tag_list

        out["tags"] = capo_chime_sdk_voice.types.tag_list.redact_sensitive(
            value["tags"]
        )
    return out
