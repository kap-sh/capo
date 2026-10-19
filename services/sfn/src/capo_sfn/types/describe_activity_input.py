"""Generated from Smithy shape ``com.amazonaws.sfn#DescribeActivityInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.arn


class DescribeActivityInput(TypedDict, closed=True):
    activity_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the activity to describe.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeActivityInput) -> dict:
    out: dict = {}
    out["activityArn"] = value["activity_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeActivityInput:
    out: DescribeActivityInput = {}  # type: ignore[typeddict-item]
    if data.get("activityArn") is not None:
        out["activity_arn"] = data["activityArn"]
    else:
        out["activity_arn"] = ""
    return out
