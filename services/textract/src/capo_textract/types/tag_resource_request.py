"""Generated from Smithy shape ``com.amazonaws.textract#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_textract.types.amazon_resource_name
    import capo_textract.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_textract.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) that specifies the resource to be tagged.</p>"""
    tags: "capo_textract.types.tag_map.TagMap"
    """<p>A set of tags (key-value pairs) that you want to assign to the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_textract.types.tag_map

    out["Tags"] = capo_textract.types.tag_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_textract.types.tag_map

        out["tags"] = capo_textract.types.tag_map.deserialize_aws_json_1_1(data["Tags"])
    else:
        out["tags"] = {}
    return out
