"""Generated from Smithy shape ``com.amazonaws.inspector2#ListFiltersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.filter_list
    import capo_inspector2.types.next_token


class ListFiltersResponse(TypedDict, closed=True):
    filters: "capo_inspector2.types.filter_list.FilterList"
    """<p>Contains details on the filters associated with your account.</p>"""
    next_token: NotRequired["capo_inspector2.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the <code>NextToken</code> value returned from the previous request to continue listing results after the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFiltersResponse) -> dict:
    out: dict = {}
    import capo_inspector2.types.filter_list

    out["filters"] = capo_inspector2.types.filter_list.serialize_json(value["filters"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFiltersResponse:
    out: ListFiltersResponse = {}  # type: ignore[typeddict-item]
    if data.get("filters") is not None:
        import capo_inspector2.types.filter_list

        out["filters"] = capo_inspector2.types.filter_list.deserialize_json(
            data["filters"]
        )
    else:
        out["filters"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
