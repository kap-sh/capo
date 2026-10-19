"""Generated from Smithy shape ``com.amazonaws.connect#SearchContactsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.large_next_token
    import capo_connect.types.max_result100
    import capo_connect.types.search_contacts_time_range
    import capo_connect.types.search_criteria
    import capo_connect.types.sort


class SearchContactsRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of Connect Customer instance. You can find the instance ID in the Amazon Resource Name (ARN) of the instance.</p>"""
    time_range: "capo_connect.types.search_contacts_time_range.SearchContactsTimeRange"
    """<p>Time range that you want to search results.</p>"""
    search_criteria: NotRequired["capo_connect.types.search_criteria.SearchCriteria"]
    """<p>The search criteria to be used to return contacts.</p>"""
    max_results: NotRequired["capo_connect.types.max_result100.MaxResult100"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired["capo_connect.types.large_next_token.LargeNextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    sort: NotRequired["capo_connect.types.sort.Sort"]
    """<p>Specifies a field to sort by and a sort order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchContactsRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    import capo_connect.types.search_contacts_time_range

    out["TimeRange"] = capo_connect.types.search_contacts_time_range.serialize_json(
        value["time_range"]
    )
    if "search_criteria" in value:
        import capo_connect.types.search_criteria

        out["SearchCriteria"] = capo_connect.types.search_criteria.serialize_json(
            value["search_criteria"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "sort" in value:
        import capo_connect.types.sort

        out["Sort"] = capo_connect.types.sort.serialize_json(value["sort"])
    return out


def deserialize_json(data: dict) -> SearchContactsRequest:
    out: SearchContactsRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        out["instance_id"] = ""
    if data.get("TimeRange") is not None:
        import capo_connect.types.search_contacts_time_range

        out["time_range"] = (
            capo_connect.types.search_contacts_time_range.deserialize_json(
                data["TimeRange"]
            )
        )
    else:
        raise DeserializationError("SearchContactsRequest.time_range required")
    if data.get("SearchCriteria") is not None:
        import capo_connect.types.search_criteria

        out["search_criteria"] = capo_connect.types.search_criteria.deserialize_json(
            data["SearchCriteria"]
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Sort") is not None:
        import capo_connect.types.sort

        out["sort"] = capo_connect.types.sort.deserialize_json(data["Sort"])
    return out


def redact_sensitive(value: SearchContactsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "search_criteria" in value:
        import capo_connect.types.search_criteria

        out["search_criteria"] = capo_connect.types.search_criteria.redact_sensitive(
            value["search_criteria"]
        )
    return out
