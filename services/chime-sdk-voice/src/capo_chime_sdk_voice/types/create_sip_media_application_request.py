"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CreateSipMediaApplicationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.sip_media_application_endpoint_list
    import capo_chime_sdk_voice.types.sip_media_application_name
    import capo_chime_sdk_voice.types.string
    import capo_chime_sdk_voice.types.tag_list


class CreateSipMediaApplicationRequest(TypedDict, closed=True):
    aws_region: "capo_chime_sdk_voice.types.string.String"
    """<p>The AWS Region assigned to the SIP media application.</p>"""
    name: (
        "capo_chime_sdk_voice.types.sip_media_application_name.SipMediaApplicationName"
    )
    """<p>The SIP media application's name.</p>"""
    endpoints: "capo_chime_sdk_voice.types.sip_media_application_endpoint_list.SipMediaApplicationEndpointList"
    """<p>List of endpoints (Lambda ARNs) specified for the SIP media application.</p>"""
    tags: NotRequired["capo_chime_sdk_voice.types.tag_list.TagList"]
    """<p>The tags assigned to the SIP media application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSipMediaApplicationRequest) -> dict:
    out: dict = {}
    out["AwsRegion"] = value["aws_region"]
    out["Name"] = value["name"]
    import capo_chime_sdk_voice.types.sip_media_application_endpoint_list

    out["Endpoints"] = (
        capo_chime_sdk_voice.types.sip_media_application_endpoint_list.serialize_json(
            value["endpoints"]
        )
    )
    if "tags" in value:
        import capo_chime_sdk_voice.types.tag_list

        out["Tags"] = capo_chime_sdk_voice.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSipMediaApplicationRequest:
    out: CreateSipMediaApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("AwsRegion") is not None:
        out["aws_region"] = data["AwsRegion"]
    else:
        raise DeserializationError(
            "CreateSipMediaApplicationRequest.aws_region required"
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateSipMediaApplicationRequest.name required")
    if data.get("Endpoints") is not None:
        import capo_chime_sdk_voice.types.sip_media_application_endpoint_list

        out["endpoints"] = (
            capo_chime_sdk_voice.types.sip_media_application_endpoint_list.deserialize_json(
                data["Endpoints"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSipMediaApplicationRequest.endpoints required"
        )
    if data.get("Tags") is not None:
        import capo_chime_sdk_voice.types.tag_list

        out["tags"] = capo_chime_sdk_voice.types.tag_list.deserialize_json(data["Tags"])
    return out


def redact_sensitive(value: CreateSipMediaApplicationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "endpoints" in value:
        import capo_chime_sdk_voice.types.sip_media_application_endpoint_list

        out["endpoints"] = (
            capo_chime_sdk_voice.types.sip_media_application_endpoint_list.redact_sensitive(
                value["endpoints"]
            )
        )
    if "tags" in value:
        import capo_chime_sdk_voice.types.tag_list

        out["tags"] = capo_chime_sdk_voice.types.tag_list.redact_sensitive(
            value["tags"]
        )
    return out
