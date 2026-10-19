"""Generated from Smithy shape ``com.amazonaws.interconnect#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_interconnect.types.amazon_resource_name
    import capo_interconnect.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    arn: "capo_interconnect.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the resource that should receive the new tags.</p>"""
    tags: "capo_interconnect.types.tag_map.TagMap"
    """<p>A map of tags to apply to the specified resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import capo_interconnect.types.tag_map

    out["tags"] = capo_interconnect.types.tag_map.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("tags") is not None:
        import capo_interconnect.types.tag_map

        out["tags"] = capo_interconnect.types.tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    else:
        out["tags"] = {}
    return out
