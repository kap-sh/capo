"""Generated from Smithy shape ``com.amazonaws.comprehend#StartFlywheelIterationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.comprehend_flywheel_arn
    import capo_comprehend.types.flywheel_iteration_id


class StartFlywheelIterationResponse(TypedDict, closed=True):
    flywheel_arn: NotRequired[
        "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    ]
    """<p></p>"""
    flywheel_iteration_id: NotRequired[
        "capo_comprehend.types.flywheel_iteration_id.FlywheelIterationId"
    ]
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartFlywheelIterationResponse) -> dict:
    out: dict = {}
    if "flywheel_arn" in value:
        out["FlywheelArn"] = value["flywheel_arn"]
    if "flywheel_iteration_id" in value:
        out["FlywheelIterationId"] = value["flywheel_iteration_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartFlywheelIterationResponse:
    out: StartFlywheelIterationResponse = {}  # type: ignore[typeddict-item]
    if data.get("FlywheelArn") is not None:
        out["flywheel_arn"] = data["FlywheelArn"]
    if data.get("FlywheelIterationId") is not None:
        out["flywheel_iteration_id"] = data["FlywheelIterationId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartFlywheelIterationResponse) -> dict:
    out: dict = {}
    if "flywheel_arn" in value:
        out["FlywheelArn"] = value["flywheel_arn"]
    if "flywheel_iteration_id" in value:
        out["FlywheelIterationId"] = value["flywheel_iteration_id"]
    return out


def deserialize_cbor(data: dict) -> StartFlywheelIterationResponse:
    out: StartFlywheelIterationResponse = {}  # type: ignore[typeddict-item]
    if data.get("FlywheelArn") is not None:
        out["flywheel_arn"] = data["FlywheelArn"]
    if data.get("FlywheelIterationId") is not None:
        out["flywheel_iteration_id"] = data["FlywheelIterationId"]
    return out
