"""Generated from Smithy shape ``com.amazonaws.comprehend#ListDatasetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.comprehend_flywheel_arn
    import capo_comprehend.types.dataset_filter
    import capo_comprehend.types.max_results_integer
    import capo_comprehend.types.string


class ListDatasetsRequest(TypedDict, closed=True):
    flywheel_arn: NotRequired[
        "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the flywheel.</p>"""
    filter: NotRequired["capo_comprehend.types.dataset_filter.DatasetFilter"]
    """<p>Filters the datasets to be returned in the response.</p>"""
    next_token: NotRequired["capo_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""
    max_results: NotRequired[
        "capo_comprehend.types.max_results_integer.MaxResultsInteger"
    ]
    """<p>Maximum number of results to return in a response. The default is 100.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDatasetsRequest) -> dict:
    out: dict = {}
    if "flywheel_arn" in value:
        out["FlywheelArn"] = value["flywheel_arn"]
    if "filter" in value:
        import capo_comprehend.types.dataset_filter

        out["Filter"] = capo_comprehend.types.dataset_filter.serialize_aws_json_1_1(
            value["filter"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDatasetsRequest:
    out: ListDatasetsRequest = {}  # type: ignore[typeddict-item]
    if data.get("FlywheelArn") is not None:
        out["flywheel_arn"] = data["FlywheelArn"]
    if data.get("Filter") is not None:
        import capo_comprehend.types.dataset_filter

        out["filter"] = capo_comprehend.types.dataset_filter.deserialize_aws_json_1_1(
            data["Filter"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListDatasetsRequest) -> dict:
    out: dict = {}
    if "flywheel_arn" in value:
        out["FlywheelArn"] = value["flywheel_arn"]
    if "filter" in value:
        import capo_comprehend.types.dataset_filter

        out["Filter"] = capo_comprehend.types.dataset_filter.serialize_cbor(
            value["filter"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> ListDatasetsRequest:
    out: ListDatasetsRequest = {}  # type: ignore[typeddict-item]
    if data.get("FlywheelArn") is not None:
        out["flywheel_arn"] = data["FlywheelArn"]
    if data.get("Filter") is not None:
        import capo_comprehend.types.dataset_filter

        out["filter"] = capo_comprehend.types.dataset_filter.deserialize_cbor(
            data["Filter"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
