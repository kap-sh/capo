"""Generated from Smithy shape ``com.amazonaws.comprehend#ListFlywheelsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.flywheel_filter
    import capo_comprehend.types.max_results_integer
    import capo_comprehend.types.string


class ListFlywheelsRequest(TypedDict, closed=True):
    filter: NotRequired["capo_comprehend.types.flywheel_filter.FlywheelFilter"]
    """<p>Filters the flywheels that are returned. You can filter flywheels on their status, or the date and time that they were submitted. You can only set one filter at a time. </p>"""
    next_token: NotRequired["capo_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""
    max_results: NotRequired[
        "capo_comprehend.types.max_results_integer.MaxResultsInteger"
    ]
    """<p>Maximum number of results to return in a response. The default is 100.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFlywheelsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_comprehend.types.flywheel_filter

        out["Filter"] = capo_comprehend.types.flywheel_filter.serialize_aws_json_1_1(
            value["filter"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFlywheelsRequest:
    out: ListFlywheelsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filter") is not None:
        import capo_comprehend.types.flywheel_filter

        out["filter"] = capo_comprehend.types.flywheel_filter.deserialize_aws_json_1_1(
            data["Filter"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListFlywheelsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_comprehend.types.flywheel_filter

        out["Filter"] = capo_comprehend.types.flywheel_filter.serialize_cbor(
            value["filter"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> ListFlywheelsRequest:
    out: ListFlywheelsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filter") is not None:
        import capo_comprehend.types.flywheel_filter

        out["filter"] = capo_comprehend.types.flywheel_filter.deserialize_cbor(
            data["Filter"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
