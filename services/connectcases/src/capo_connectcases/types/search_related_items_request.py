"""Generated from Smithy shape ``com.amazonaws.connectcases#SearchRelatedItemsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_id
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.next_token
    import capo_connectcases.types.related_item_filter_list


class SearchRelatedItemsRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    case_id: "capo_connectcases.types.case_id.CaseId"
    """<p>A unique identifier of the case.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired["capo_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    filters: NotRequired[
        "capo_connectcases.types.related_item_filter_list.RelatedItemFilterList"
    ]
    """<p>The list of types of related items and their parameters to use for filtering.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchRelatedItemsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "filters" in value:
        import capo_connectcases.types.related_item_filter_list

        out["filters"] = (
            capo_connectcases.types.related_item_filter_list.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchRelatedItemsRequest:
    out: SearchRelatedItemsRequest = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("filters") is not None:
        import capo_connectcases.types.related_item_filter_list

        out["filters"] = (
            capo_connectcases.types.related_item_filter_list.deserialize_json(
                data["filters"]
            )
        )
    return out


def redact_sensitive(value: SearchRelatedItemsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filters" in value:
        import capo_connectcases.types.related_item_filter_list

        out["filters"] = (
            capo_connectcases.types.related_item_filter_list.redact_sensitive(
                value["filters"]
            )
        )
    return out
