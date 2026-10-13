"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#TagResourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.arn
    import capo_chime_sdk_voice.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_chime_sdk_voice.types.arn.Arn"
    """<p>The ARN of the resource being tagged. </p>"""
    tags: "capo_chime_sdk_voice.types.tag_list.TagList"
    """<p>A list of the tags being added to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_chime_sdk_voice.types.tag_list

    out["Tags"] = capo_chime_sdk_voice.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if data.get("Tags") is not None:
        import capo_chime_sdk_voice.types.tag_list

        out["tags"] = capo_chime_sdk_voice.types.tag_list.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out


def redact_sensitive(value: TagResourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "resource_arn" in value:
        out["resource_arn"] = "*** Sensitive Data Redacted ***"
    if "tags" in value:
        import capo_chime_sdk_voice.types.tag_list

        out["tags"] = capo_chime_sdk_voice.types.tag_list.redact_sensitive(
            value["tags"]
        )
    return out
