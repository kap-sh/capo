"""Generated from Smithy shape ``com.amazonaws.kinesis#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.resource_arn
    import capo_kinesis.types.stream_id
    import capo_kinesis.types.tag_map


class TagResourceInput(TypedDict, closed=True):
    tags: "capo_kinesis.types.tag_map.TagMap"
    """<p>An array of tags to be added to the Kinesis resource. A tag consists of a required key and an optional value. You can add up to 50 tags per resource.</p> <p>Tags may only contain Unicode letters, digits, white space, or these symbols: _ . : / = + - @.</p>"""
    resource_arn: "capo_kinesis.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the Kinesis resource to which to add tags.</p>"""
    stream_id: NotRequired["capo_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceInput) -> dict:
    out: dict = {}
    import capo_kinesis.types.tag_map

    out["Tags"] = capo_kinesis.types.tag_map.serialize_aws_json_1_1(value["tags"])
    out["ResourceARN"] = value["resource_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_kinesis.types.tag_map

        out["tags"] = capo_kinesis.types.tag_map.deserialize_aws_json_1_1(data["Tags"])
    else:
        out["tags"] = {}
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("StreamId") is not None:
        out["stream_id"] = data["StreamId"]
    return out
