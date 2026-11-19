"""Generated from Smithy shape ``com.amazonaws.comprehend#UpdateFlywheelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.flywheel_properties


class UpdateFlywheelResponse(TypedDict, closed=True):
    flywheel_properties: NotRequired[
        "capo_comprehend.types.flywheel_properties.FlywheelProperties"
    ]
    """<p>The flywheel properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFlywheelResponse) -> dict:
    out: dict = {}
    if "flywheel_properties" in value:
        import capo_comprehend.types.flywheel_properties

        out["FlywheelProperties"] = (
            capo_comprehend.types.flywheel_properties.serialize_aws_json_1_1(
                value["flywheel_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFlywheelResponse:
    out: UpdateFlywheelResponse = {}  # type: ignore[typeddict-item]
    if data.get("FlywheelProperties") is not None:
        import capo_comprehend.types.flywheel_properties

        out["flywheel_properties"] = (
            capo_comprehend.types.flywheel_properties.deserialize_aws_json_1_1(
                data["FlywheelProperties"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateFlywheelResponse) -> dict:
    out: dict = {}
    if "flywheel_properties" in value:
        import capo_comprehend.types.flywheel_properties

        out["FlywheelProperties"] = (
            capo_comprehend.types.flywheel_properties.serialize_cbor(
                value["flywheel_properties"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> UpdateFlywheelResponse:
    out: UpdateFlywheelResponse = {}  # type: ignore[typeddict-item]
    if data.get("FlywheelProperties") is not None:
        import capo_comprehend.types.flywheel_properties

        out["flywheel_properties"] = (
            capo_comprehend.types.flywheel_properties.deserialize_cbor(
                data["FlywheelProperties"]
            )
        )
    return out
