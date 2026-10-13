"""Generated from Smithy shape ``com.amazonaws.connectcases#SearchRelatedItemsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcases.types.next_token
    import capo_connectcases.types.search_related_items_response_item_list


class SearchRelatedItemsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. This is null if there are no more results to return.</p>"""
    related_items: "capo_connectcases.types.search_related_items_response_item_list.SearchRelatedItemsResponseItemList"
    """<p>A list of items related to a case. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchRelatedItemsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_connectcases.types.search_related_items_response_item_list

    out["relatedItems"] = (
        capo_connectcases.types.search_related_items_response_item_list.serialize_json(
            value["related_items"]
        )
    )
    return out


def deserialize_json(data: dict) -> SearchRelatedItemsResponse:
    out: SearchRelatedItemsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("relatedItems") is not None:
        import capo_connectcases.types.search_related_items_response_item_list

        out["related_items"] = (
            capo_connectcases.types.search_related_items_response_item_list.deserialize_json(
                data["relatedItems"]
            )
        )
    else:
        raise DeserializationError("SearchRelatedItemsResponse.related_items required")
    return out


def redact_sensitive(value: SearchRelatedItemsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "related_items" in value:
        import capo_connectcases.types.search_related_items_response_item_list

        out["related_items"] = (
            capo_connectcases.types.search_related_items_response_item_list.redact_sensitive(
                value["related_items"]
            )
        )
    return out
