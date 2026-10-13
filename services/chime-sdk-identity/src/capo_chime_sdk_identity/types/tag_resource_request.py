"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#TagResourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_chime_sdk_identity.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.chime_arn
    import capo_chime_sdk_identity.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The resource ARN.</p>"""
    tags: "capo_chime_sdk_identity.types.tag_list.TagList"
    """<p>The tag key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_chime_sdk_identity.types.tag_list

    out["Tags"] = capo_chime_sdk_identity.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if data.get("Tags") is not None:
        import capo_chime_sdk_identity.types.tag_list

        out["tags"] = capo_chime_sdk_identity.types.tag_list.deserialize_json(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out


def redact_sensitive(value: TagResourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        import capo_chime_sdk_identity.types.tag_list

        out["tags"] = capo_chime_sdk_identity.types.tag_list.redact_sensitive(
            value["tags"]
        )
    return out
