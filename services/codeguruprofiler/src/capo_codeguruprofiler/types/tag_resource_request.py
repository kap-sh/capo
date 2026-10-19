"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.profiling_group_arn
    import capo_codeguruprofiler.types.tags_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_codeguruprofiler.types.profiling_group_arn.ProfilingGroupArn"
    """<p> The Amazon Resource Name (ARN) of the resource that the tags are added to. </p>"""
    tags: "capo_codeguruprofiler.types.tags_map.TagsMap"
    """<p> The list of tags that are added to the specified resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_codeguruprofiler.types.tags_map

    out["tags"] = capo_codeguruprofiler.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_codeguruprofiler.types.tags_map

        out["tags"] = capo_codeguruprofiler.types.tags_map.deserialize_json(
            data["tags"]
        )
    else:
        out["tags"] = {}
    return out
