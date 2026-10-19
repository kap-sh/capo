"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListBillEstimateInputCommitmentModificationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.max_results
    import capo_bcm_pricing_calculator.types.next_page_token
    import capo_bcm_pricing_calculator.types.resource_id


class ListBillEstimateInputCommitmentModificationsRequest(TypedDict, closed=True):
    bill_estimate_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The unique identifier of the bill estimate to list input commitment modifications for. </p>"""
    next_token: NotRequired[
        "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
    ]
    """<p> A token to retrieve the next page of results. </p>"""
    max_results: NotRequired["capo_bcm_pricing_calculator.types.max_results.MaxResults"]
    """<p> The maximum number of results to return per page. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ListBillEstimateInputCommitmentModificationsRequest,
) -> dict:
    out: dict = {}
    out["billEstimateId"] = value["bill_estimate_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ListBillEstimateInputCommitmentModificationsRequest:
    out: ListBillEstimateInputCommitmentModificationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("billEstimateId") is not None:
        out["bill_estimate_id"] = data["billEstimateId"]
    else:
        out["bill_estimate_id"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
