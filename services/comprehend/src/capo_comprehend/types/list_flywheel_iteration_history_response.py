"""Generated from Smithy shape ``com.amazonaws.comprehend#ListFlywheelIterationHistoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.flywheel_iteration_properties_list
    import capo_comprehend.types.string


class ListFlywheelIterationHistoryResponse(TypedDict, closed=True):
    flywheel_iteration_properties_list: NotRequired[
        "capo_comprehend.types.flywheel_iteration_properties_list.FlywheelIterationPropertiesList"
    ]
    """<p>List of flywheel iteration properties</p>"""
    next_token: NotRequired["capo_comprehend.types.string.String"]
    """<p>Next token</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFlywheelIterationHistoryResponse) -> dict:
    out: dict = {}
    if "flywheel_iteration_properties_list" in value:
        import capo_comprehend.types.flywheel_iteration_properties_list

        out["FlywheelIterationPropertiesList"] = (
            capo_comprehend.types.flywheel_iteration_properties_list.serialize_aws_json_1_1(
                value["flywheel_iteration_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFlywheelIterationHistoryResponse:
    out: ListFlywheelIterationHistoryResponse = {}  # type: ignore[typeddict-item]
    if data.get("FlywheelIterationPropertiesList") is not None:
        import capo_comprehend.types.flywheel_iteration_properties_list

        out["flywheel_iteration_properties_list"] = (
            capo_comprehend.types.flywheel_iteration_properties_list.deserialize_aws_json_1_1(
                data["FlywheelIterationPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListFlywheelIterationHistoryResponse) -> dict:
    out: dict = {}
    if "flywheel_iteration_properties_list" in value:
        import capo_comprehend.types.flywheel_iteration_properties_list

        out["FlywheelIterationPropertiesList"] = (
            capo_comprehend.types.flywheel_iteration_properties_list.serialize_cbor(
                value["flywheel_iteration_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListFlywheelIterationHistoryResponse:
    out: ListFlywheelIterationHistoryResponse = {}  # type: ignore[typeddict-item]
    if data.get("FlywheelIterationPropertiesList") is not None:
        import capo_comprehend.types.flywheel_iteration_properties_list

        out["flywheel_iteration_properties_list"] = (
            capo_comprehend.types.flywheel_iteration_properties_list.deserialize_cbor(
                data["FlywheelIterationPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
