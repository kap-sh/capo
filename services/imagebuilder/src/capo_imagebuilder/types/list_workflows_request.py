"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListWorkflowsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.boolean
    import capo_imagebuilder.types.filter_list
    import capo_imagebuilder.types.ownership
    import capo_imagebuilder.types.pagination_token
    import capo_imagebuilder.types.restricted_integer


class ListWorkflowsRequest(TypedDict, closed=True):
    owner: NotRequired["capo_imagebuilder.types.ownership.Ownership"]
    """<p>Filters results based on the workflow owner. By default, this request returns the workflows that your account owns (<code>Self</code>). Specify <code>Amazon</code> to list the workflows that Image Builder manages. Image Builder rejects the <code>Shared</code> and <code>ThirdParty</code> owner values for workflows, and <code>AWSMarketplace</code> returns no results.</p>"""
    filters: NotRequired["capo_imagebuilder.types.filter_list.FilterList"]
    """<p>Filters to narrow the list of workflows. You can filter on <code>name</code>, <code>version</code>, <code>description</code>, and <code>type</code>.</p>"""
    by_name: NotRequired["capo_imagebuilder.types.boolean.Boolean"]
    """<p>Specifies whether to return one entry per workflow name, with all versions of each workflow aggregated. Defaults to <code>false</code>, which returns one entry per workflow version. You can't combine this option with the <code>version</code> filter.</p>"""
    max_results: NotRequired[
        "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
    ]
    """<p>The maximum number of items to return in a single request.</p>"""
    next_token: NotRequired["capo_imagebuilder.types.pagination_token.PaginationToken"]
    """<p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowsRequest) -> dict:
    out: dict = {}
    if "owner" in value:
        import capo_imagebuilder.types.ownership

        out["owner"] = capo_imagebuilder.types.ownership.serialize_json(value["owner"])
    if "filters" in value:
        import capo_imagebuilder.types.filter_list

        out["filters"] = capo_imagebuilder.types.filter_list.serialize_json(
            value["filters"]
        )
    if "by_name" in value:
        out["byName"] = value["by_name"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWorkflowsRequest:
    out: ListWorkflowsRequest = {}  # type: ignore[typeddict-item]
    if data.get("owner") is not None:
        import capo_imagebuilder.types.ownership

        out["owner"] = capo_imagebuilder.types.ownership.deserialize_json(data["owner"])
    if data.get("filters") is not None:
        import capo_imagebuilder.types.filter_list

        out["filters"] = capo_imagebuilder.types.filter_list.deserialize_json(
            data["filters"]
        )
    if data.get("byName") is not None:
        out["by_name"] = data["byName"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
