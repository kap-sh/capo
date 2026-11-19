"""Generated from Smithy shape ``com.amazonaws.comprehend#ListFlywheelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.flywheel_summary_list
    import capo_comprehend.types.string


class ListFlywheelsResponse(TypedDict, closed=True):
    flywheel_summary_list: NotRequired[
        "capo_comprehend.types.flywheel_summary_list.FlywheelSummaryList"
    ]
    """<p>A list of flywheel properties retrieved by the service in response to the request. </p>"""
    next_token: NotRequired["capo_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFlywheelsResponse) -> dict:
    out: dict = {}
    if "flywheel_summary_list" in value:
        import capo_comprehend.types.flywheel_summary_list

        out["FlywheelSummaryList"] = (
            capo_comprehend.types.flywheel_summary_list.serialize_aws_json_1_1(
                value["flywheel_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFlywheelsResponse:
    out: ListFlywheelsResponse = {}  # type: ignore[typeddict-item]
    if data.get("FlywheelSummaryList") is not None:
        import capo_comprehend.types.flywheel_summary_list

        out["flywheel_summary_list"] = (
            capo_comprehend.types.flywheel_summary_list.deserialize_aws_json_1_1(
                data["FlywheelSummaryList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListFlywheelsResponse) -> dict:
    out: dict = {}
    if "flywheel_summary_list" in value:
        import capo_comprehend.types.flywheel_summary_list

        out["FlywheelSummaryList"] = (
            capo_comprehend.types.flywheel_summary_list.serialize_cbor(
                value["flywheel_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListFlywheelsResponse:
    out: ListFlywheelsResponse = {}  # type: ignore[typeddict-item]
    if data.get("FlywheelSummaryList") is not None:
        import capo_comprehend.types.flywheel_summary_list

        out["flywheel_summary_list"] = (
            capo_comprehend.types.flywheel_summary_list.deserialize_cbor(
                data["FlywheelSummaryList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
