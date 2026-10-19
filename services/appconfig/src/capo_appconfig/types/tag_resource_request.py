"""Generated from Smithy shape ``com.amazonaws.appconfig#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.arn
    import capo_appconfig.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_appconfig.types.arn.Arn"
    """<p>The ARN of the resource for which to retrieve tags.</p>"""
    tags: "capo_appconfig.types.tag_map.TagMap"
    """<p>The key-value string map. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with <code>aws:</code>. The tag value can be up to 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_appconfig.types.tag_map

    out["Tags"] = capo_appconfig.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_appconfig.types.tag_map

        out["tags"] = capo_appconfig.types.tag_map.deserialize_json(data["Tags"])
    else:
        out["tags"] = {}
    return out
