"""Generated from Smithy shape ``com.amazonaws.databrew#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.arn
    import capo_databrew.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_databrew.types.arn.Arn"
    """<p>The DataBrew resource to which tags should be added. The value for this parameter is an Amazon Resource Name (ARN). For DataBrew, you can tag a dataset, a job, a project, or a recipe.</p>"""
    tags: "capo_databrew.types.tag_map.TagMap"
    """<p>One or more tags to be assigned to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_databrew.types.tag_map

    out["Tags"] = capo_databrew.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_databrew.types.tag_map

        out["tags"] = capo_databrew.types.tag_map.deserialize_json(data["Tags"])
    else:
        out["tags"] = {}
    return out
