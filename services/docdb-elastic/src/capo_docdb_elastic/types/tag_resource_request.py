"""Generated from Smithy shape ``com.amazonaws.docdbelastic#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_docdb_elastic.types.arn
    import capo_docdb_elastic.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_docdb_elastic.types.arn.Arn"
    """<p>The ARN identifier of the elastic cluster resource.</p>"""
    tags: "capo_docdb_elastic.types.tag_map.TagMap"
    """<p>The tags that are assigned to the elastic cluster resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_docdb_elastic.types.tag_map

    out["tags"] = capo_docdb_elastic.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_docdb_elastic.types.tag_map

        out["tags"] = capo_docdb_elastic.types.tag_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
