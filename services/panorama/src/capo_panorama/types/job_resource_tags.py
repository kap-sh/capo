"""Generated from Smithy shape ``com.amazonaws.panorama#JobResourceTags``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.job_resource_type
    import capo_panorama.types.tag_map


class JobResourceTags(TypedDict, closed=True):
    resource_type: "capo_panorama.types.job_resource_type.JobResourceType"
    """<p>The job's type.</p>"""
    tags: "capo_panorama.types.tag_map.TagMap"
    """<p>The job's tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobResourceTags) -> dict:
    out: dict = {}
    out["ResourceType"] = value["resource_type"]
    import capo_panorama.types.tag_map

    out["Tags"] = capo_panorama.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> JobResourceTags:
    out: JobResourceTags = {}  # type: ignore[typeddict-item]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    else:
        out["resource_type"] = ""
    if data.get("Tags") is not None:
        import capo_panorama.types.tag_map

        out["tags"] = capo_panorama.types.tag_map.deserialize_json(data["Tags"])
    else:
        out["tags"] = {}
    return out
