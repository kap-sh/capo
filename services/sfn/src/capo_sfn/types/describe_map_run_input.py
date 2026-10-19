"""Generated from Smithy shape ``com.amazonaws.sfn#DescribeMapRunInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.long_arn


class DescribeMapRunInput(TypedDict, closed=True):
    map_run_arn: "capo_sfn.types.long_arn.LongArn"
    """<p>The Amazon Resource Name (ARN) that identifies a Map Run.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeMapRunInput) -> dict:
    out: dict = {}
    out["mapRunArn"] = value["map_run_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeMapRunInput:
    out: DescribeMapRunInput = {}  # type: ignore[typeddict-item]
    if data.get("mapRunArn") is not None:
        out["map_run_arn"] = data["mapRunArn"]
    else:
        out["map_run_arn"] = ""
    return out
