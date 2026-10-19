"""Generated from Smithy shape ``com.amazonaws.kinesis#GetResourcePolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.resource_arn
    import capo_kinesis.types.stream_id


class GetResourcePolicyInput(TypedDict, closed=True):
    resource_arn: "capo_kinesis.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the data stream or consumer.</p>"""
    stream_id: NotRequired["capo_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourcePolicyInput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourcePolicyInput:
    out: GetResourcePolicyInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("StreamId") is not None:
        out["stream_id"] = data["StreamId"]
    return out
