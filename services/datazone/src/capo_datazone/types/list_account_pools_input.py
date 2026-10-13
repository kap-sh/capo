"""Generated from Smithy shape ``com.amazonaws.datazone#ListAccountPoolsInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.account_pool_name
    import capo_datazone.types.domain_id
    import capo_datazone.types.max_results
    import capo_datazone.types.pagination_token
    import capo_datazone.types.sort_field_account_pool
    import capo_datazone.types.sort_order


class ListAccountPoolsInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where exsting account pools are to be listed.</p>"""
    name: NotRequired["capo_datazone.types.account_pool_name.AccountPoolName"]
    """<p>The name of the account pool to be listed.</p>"""
    sort_by: NotRequired[
        "capo_datazone.types.sort_field_account_pool.SortFieldAccountPool"
    ]
    """<p>The sort by mechanism in which the existing account pools are to be listed.</p>"""
    sort_order: NotRequired["capo_datazone.types.sort_order.SortOrder"]
    """<p>The sort order in which the existing account pools are to be listed.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of account pools is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of account pools, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListAccountPools to list the next set of account pools.</p>"""
    max_results: NotRequired["capo_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of account pools to return in a single call to ListAccountPools. When the number of account pools to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListAccountPools to list the next set of account pools.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccountPoolsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAccountPoolsInput:
    out: ListAccountPoolsInput = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: ListAccountPoolsInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
