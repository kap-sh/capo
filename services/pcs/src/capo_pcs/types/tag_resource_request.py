"""Generated from Smithy shape ``com.amazonaws.pcs#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pcs.types.arn
    import capo_pcs.types.request_tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_pcs.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tags: "capo_pcs.types.request_tag_map.RequestTagMap"
    """<p>1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_pcs.types.request_tag_map

    out["tags"] = capo_pcs.types.request_tag_map.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tags") is not None:
        import capo_pcs.types.request_tag_map

        out["tags"] = capo_pcs.types.request_tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    else:
        out["tags"] = {}
    return out
