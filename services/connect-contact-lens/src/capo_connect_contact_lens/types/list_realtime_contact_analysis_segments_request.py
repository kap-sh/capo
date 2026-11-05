"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#ListRealtimeContactAnalysisSegmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect_contact_lens.types.contact_id
    import capo_connect_contact_lens.types.instance_id
    import capo_connect_contact_lens.types.max_results
    import capo_connect_contact_lens.types.next_token
    import capo_connect_contact_lens.types.real_time_contact_analysis_segments_filter


class ListRealtimeContactAnalysisSegmentsRequest(TypedDict, closed=True):
    instance_id: NotRequired["capo_connect_contact_lens.types.instance_id.InstanceId"]
    """<p>The identifier of the Amazon Connect instance.</p>"""
    contact_id: NotRequired["capo_connect_contact_lens.types.contact_id.ContactId"]
    """<p>The identifier of the contact.</p>"""
    max_results: NotRequired["capo_connect_contact_lens.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired["capo_connect_contact_lens.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    list_filter: NotRequired[
        "capo_connect_contact_lens.types.real_time_contact_analysis_segments_filter.RealTimeContactAnalysisSegmentsFilter"
    ]
    """<p>A filter that limits the category segments returned by the operation. When provided, use <code>CategoriesAttributeFilter</code> to return only the category segments whose rules have tags that match the filter. This enforces tag-based access control on the categories that the caller can view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRealtimeContactAnalysisSegmentsRequest) -> dict:
    out: dict = {}
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "contact_id" in value:
        out["ContactId"] = value["contact_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "list_filter" in value:
        import capo_connect_contact_lens.types.real_time_contact_analysis_segments_filter

        out["ListFilter"] = (
            capo_connect_contact_lens.types.real_time_contact_analysis_segments_filter.serialize_json(
                value["list_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRealtimeContactAnalysisSegmentsRequest:
    out: ListRealtimeContactAnalysisSegmentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ListFilter") is not None:
        import capo_connect_contact_lens.types.real_time_contact_analysis_segments_filter

        out["list_filter"] = (
            capo_connect_contact_lens.types.real_time_contact_analysis_segments_filter.deserialize_json(
                data["ListFilter"]
            )
        )
    return out
