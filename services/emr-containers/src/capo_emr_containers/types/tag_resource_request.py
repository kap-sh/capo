"""Generated from Smithy shape ``com.amazonaws.emrcontainers#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.rsi_arn
    import capo_emr_containers.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_emr_containers.types.rsi_arn.RsiArn"
    """<p>The ARN of resources.</p>"""
    tags: "capo_emr_containers.types.tag_map.TagMap"
    """<p>The tags assigned to resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_emr_containers.types.tag_map

    out["tags"] = capo_emr_containers.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_emr_containers.types.tag_map

        out["tags"] = capo_emr_containers.types.tag_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
