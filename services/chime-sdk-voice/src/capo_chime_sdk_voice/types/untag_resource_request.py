"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#UntagResourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.arn
    import capo_chime_sdk_voice.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_chime_sdk_voice.types.arn.Arn"
    """<p>The ARN of the resource having its tags removed.</p>"""
    tag_keys: "capo_chime_sdk_voice.types.tag_key_list.TagKeyList"
    """<p>The keys of the tags being removed from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_chime_sdk_voice.types.tag_key_list

    out["TagKeys"] = capo_chime_sdk_voice.types.tag_key_list.serialize_json(
        value["tag_keys"]
    )
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if data.get("TagKeys") is not None:
        import capo_chime_sdk_voice.types.tag_key_list

        out["tag_keys"] = capo_chime_sdk_voice.types.tag_key_list.deserialize_json(
            data["TagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out


def redact_sensitive(value: UntagResourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "resource_arn" in value:
        out["resource_arn"] = "*** Sensitive Data Redacted ***"
    if "tag_keys" in value:
        import capo_chime_sdk_voice.types.tag_key_list

        out["tag_keys"] = capo_chime_sdk_voice.types.tag_key_list.redact_sensitive(
            value["tag_keys"]
        )
    return out
