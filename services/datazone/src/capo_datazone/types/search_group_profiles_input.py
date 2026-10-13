"""Generated from Smithy shape ``com.amazonaws.datazone#SearchGroupProfilesInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.group_search_text
    import capo_datazone.types.group_search_type
    import capo_datazone.types.max_results
    import capo_datazone.types.pagination_token


class SearchGroupProfilesInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which you want to search group profiles.</p>"""
    group_type: "capo_datazone.types.group_search_type.GroupSearchType"
    """<p>The group type for which to search.</p>"""
    search_text: NotRequired["capo_datazone.types.group_search_text.GroupSearchText"]
    """<p>Specifies the text for which to search.</p>"""
    max_results: NotRequired["capo_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call to <code>SearchGroupProfiles</code>. When the number of results to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>SearchGroupProfiles</code> to list the next set of results. </p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of results is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of results, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>SearchGroupProfiles</code> to list the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchGroupProfilesInput) -> dict:
    out: dict = {}
    import capo_datazone.types.group_search_type

    out["groupType"] = capo_datazone.types.group_search_type.serialize_json(
        value["group_type"]
    )
    if "search_text" in value:
        out["searchText"] = value["search_text"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchGroupProfilesInput:
    out: SearchGroupProfilesInput = {}  # type: ignore[typeddict-item]
    if data.get("groupType") is not None:
        import capo_datazone.types.group_search_type

        out["group_type"] = capo_datazone.types.group_search_type.deserialize_json(
            data["groupType"]
        )
    else:
        raise DeserializationError("SearchGroupProfilesInput.group_type required")
    if data.get("searchText") is not None:
        out["search_text"] = data["searchText"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: SearchGroupProfilesInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "search_text" in value:
        out["search_text"] = "*** Sensitive Data Redacted ***"
    return out
