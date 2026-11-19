"""Generated from Smithy shape ``com.amazonaws.comprehend#CreateFlywheelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.comprehend_flywheel_arn
    import capo_comprehend.types.comprehend_model_arn


class CreateFlywheelResponse(TypedDict, closed=True):
    flywheel_arn: NotRequired[
        "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the flywheel.</p>"""
    active_model_arn: NotRequired[
        "capo_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the active model version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFlywheelResponse) -> dict:
    out: dict = {}
    if "flywheel_arn" in value:
        out["FlywheelArn"] = value["flywheel_arn"]
    if "active_model_arn" in value:
        out["ActiveModelArn"] = value["active_model_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFlywheelResponse:
    out: CreateFlywheelResponse = {}  # type: ignore[typeddict-item]
    if data.get("FlywheelArn") is not None:
        out["flywheel_arn"] = data["FlywheelArn"]
    if data.get("ActiveModelArn") is not None:
        out["active_model_arn"] = data["ActiveModelArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateFlywheelResponse) -> dict:
    out: dict = {}
    if "flywheel_arn" in value:
        out["FlywheelArn"] = value["flywheel_arn"]
    if "active_model_arn" in value:
        out["ActiveModelArn"] = value["active_model_arn"]
    return out


def deserialize_cbor(data: dict) -> CreateFlywheelResponse:
    out: CreateFlywheelResponse = {}  # type: ignore[typeddict-item]
    if data.get("FlywheelArn") is not None:
        out["flywheel_arn"] = data["FlywheelArn"]
    if data.get("ActiveModelArn") is not None:
        out["active_model_arn"] = data["ActiveModelArn"]
    return out
