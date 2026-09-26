"""Generated from Smithy shape ``com.amazonaws.accountaccess#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_account_access.errors import DeserializationError

if TYPE_CHECKING:
    import capo_account_access.types.application_arn
    import capo_account_access.types.tags_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_account_access.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the resource to add tags to.</p>"""
    tags: "capo_account_access.types.tags_map.TagsMap"
    """<p>Specifies the tags to add to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_account_access.types.tags_map

    out["tags"] = capo_account_access.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_account_access.types.tags_map

        out["tags"] = capo_account_access.types.tags_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
