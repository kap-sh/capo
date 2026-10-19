"""Generated from Smithy shape ``com.amazonaws.invoicing#ListProcurementPortalPreferencesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.basic_string_without_space
    import capo_invoicing.types.max_results


class ListProcurementPortalPreferencesRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p>The token for the next set of results. (You received this token from a previous call.)</p>"""
    max_results: NotRequired["capo_invoicing.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListProcurementPortalPreferencesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListProcurementPortalPreferencesRequest:
    out: ListProcurementPortalPreferencesRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
