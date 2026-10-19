"""Generated from Smithy shape ``com.amazonaws.rekognition#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.resource_arn
    import capo_rekognition.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_rekognition.types.resource_arn.ResourceArn"
    """<p> Amazon Resource Name (ARN) of the model, collection, or stream processor that you want to assign the tags to. </p>"""
    tags: "capo_rekognition.types.tag_map.TagMap"
    """<p> The key-value tags to assign to the resource. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_rekognition.types.tag_map

    out["Tags"] = capo_rekognition.types.tag_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_rekognition.types.tag_map

        out["tags"] = capo_rekognition.types.tag_map.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        out["tags"] = {}
    return out
