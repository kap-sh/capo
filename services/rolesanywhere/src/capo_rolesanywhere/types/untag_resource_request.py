"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#UntagResourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_rolesanywhere.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rolesanywhere.types.amazon_resource_name
    import capo_rolesanywhere.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_rolesanywhere.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the resource.</p>"""
    tag_keys: "capo_rolesanywhere.types.tag_key_list.TagKeyList"
    """<p>A list of keys. Tag keys are the unique identifiers of tags. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_rolesanywhere.types.tag_key_list

    out["tagKeys"] = capo_rolesanywhere.types.tag_key_list.serialize_json(
        value["tag_keys"]
    )
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if data.get("tagKeys") is not None:
        import capo_rolesanywhere.types.tag_key_list

        out["tag_keys"] = capo_rolesanywhere.types.tag_key_list.deserialize_json(
            data["tagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out


def redact_sensitive(value: UntagResourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tag_keys" in value:
        import capo_rolesanywhere.types.tag_key_list

        out["tag_keys"] = capo_rolesanywhere.types.tag_key_list.redact_sensitive(
            value["tag_keys"]
        )
    return out
