"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListImageRecipesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.filter_list
    import capo_imagebuilder.types.ownership
    import capo_imagebuilder.types.pagination_token
    import capo_imagebuilder.types.restricted_integer


class ListImageRecipesRequest(TypedDict, closed=True):
    owner: NotRequired["capo_imagebuilder.types.ownership.Ownership"]
    """<p>You can specify the recipe owner to filter results by that owner. By default, this request will only show image recipes owned by your account. To filter by a different owner, specify one of the <code>Valid Values</code> that are listed for this parameter.</p>"""
    filters: NotRequired["capo_imagebuilder.types.filter_list.FilterList"]
    """<p>Use the following filters to streamline results:</p> <ul> <li> <p> <code>name</code> </p> </li> <li> <p> <code>parentImage</code> </p> </li> <li> <p> <code>platform</code> </p> </li> </ul>"""
    max_results: NotRequired[
        "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
    ]
    """<p>The maximum number of items to return in a single request. If you don't specify a value, Image Builder returns up to 25 items. The largest page size that you can request is 100 items. A page can contain fewer items than the maximum, with a <code>nextToken</code> to continue paging.</p>"""
    next_token: NotRequired["capo_imagebuilder.types.pagination_token.PaginationToken"]
    """<p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImageRecipesRequest) -> dict:
    out: dict = {}
    if "owner" in value:
        import capo_imagebuilder.types.ownership

        out["owner"] = capo_imagebuilder.types.ownership.serialize_json(value["owner"])
    if "filters" in value:
        import capo_imagebuilder.types.filter_list

        out["filters"] = capo_imagebuilder.types.filter_list.serialize_json(
            value["filters"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImageRecipesRequest:
    out: ListImageRecipesRequest = {}  # type: ignore[typeddict-item]
    if data.get("owner") is not None:
        import capo_imagebuilder.types.ownership

        out["owner"] = capo_imagebuilder.types.ownership.deserialize_json(data["owner"])
    if data.get("filters") is not None:
        import capo_imagebuilder.types.filter_list

        out["filters"] = capo_imagebuilder.types.filter_list.deserialize_json(
            data["filters"]
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
