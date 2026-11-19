"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeFlywheelIterationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.flywheel_iteration_properties


class DescribeFlywheelIterationResponse(TypedDict, closed=True):
    flywheel_iteration_properties: NotRequired[
        "capo_comprehend.types.flywheel_iteration_properties.FlywheelIterationProperties"
    ]
    """<p>The configuration properties of a flywheel iteration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFlywheelIterationResponse) -> dict:
    out: dict = {}
    if "flywheel_iteration_properties" in value:
        import capo_comprehend.types.flywheel_iteration_properties

        out["FlywheelIterationProperties"] = (
            capo_comprehend.types.flywheel_iteration_properties.serialize_aws_json_1_1(
                value["flywheel_iteration_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFlywheelIterationResponse:
    out: DescribeFlywheelIterationResponse = {}  # type: ignore[typeddict-item]
    if data.get("FlywheelIterationProperties") is not None:
        import capo_comprehend.types.flywheel_iteration_properties

        out["flywheel_iteration_properties"] = (
            capo_comprehend.types.flywheel_iteration_properties.deserialize_aws_json_1_1(
                data["FlywheelIterationProperties"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeFlywheelIterationResponse) -> dict:
    out: dict = {}
    if "flywheel_iteration_properties" in value:
        import capo_comprehend.types.flywheel_iteration_properties

        out["FlywheelIterationProperties"] = (
            capo_comprehend.types.flywheel_iteration_properties.serialize_cbor(
                value["flywheel_iteration_properties"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeFlywheelIterationResponse:
    out: DescribeFlywheelIterationResponse = {}  # type: ignore[typeddict-item]
    if data.get("FlywheelIterationProperties") is not None:
        import capo_comprehend.types.flywheel_iteration_properties

        out["flywheel_iteration_properties"] = (
            capo_comprehend.types.flywheel_iteration_properties.deserialize_cbor(
                data["FlywheelIterationProperties"]
            )
        )
    return out
