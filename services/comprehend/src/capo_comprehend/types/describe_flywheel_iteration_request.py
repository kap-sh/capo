"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeFlywheelIterationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.comprehend_flywheel_arn
    import capo_comprehend.types.flywheel_iteration_id


class DescribeFlywheelIterationRequest(TypedDict, closed=True):
    flywheel_arn: "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    """<p></p>"""
    flywheel_iteration_id: (
        "capo_comprehend.types.flywheel_iteration_id.FlywheelIterationId"
    )
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFlywheelIterationRequest) -> dict:
    out: dict = {}
    out["FlywheelArn"] = value["flywheel_arn"]
    out["FlywheelIterationId"] = value["flywheel_iteration_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFlywheelIterationRequest:
    out: DescribeFlywheelIterationRequest = {}  # type: ignore[typeddict-item]
    if data.get("FlywheelArn") is not None:
        out["flywheel_arn"] = data["FlywheelArn"]
    else:
        out["flywheel_arn"] = ""
    if data.get("FlywheelIterationId") is not None:
        out["flywheel_iteration_id"] = data["FlywheelIterationId"]
    else:
        out["flywheel_iteration_id"] = ""
    return out
