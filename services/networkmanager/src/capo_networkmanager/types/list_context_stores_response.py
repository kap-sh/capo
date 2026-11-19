"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListContextStoresResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.context_store_list
    import capo_networkmanager.types.next_token


class ListContextStoresResponse(TypedDict, closed=True):
    context_stores: NotRequired[
        "capo_networkmanager.types.context_store_list.ContextStoreList"
    ]
    """<p>The context stores.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContextStoresResponse) -> dict:
    out: dict = {}
    if "context_stores" in value:
        import capo_networkmanager.types.context_store_list

        out["ContextStores"] = (
            capo_networkmanager.types.context_store_list.serialize_json(
                value["context_stores"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListContextStoresResponse:
    out: ListContextStoresResponse = {}  # type: ignore[typeddict-item]
    if data.get("ContextStores") is not None:
        import capo_networkmanager.types.context_store_list

        out["context_stores"] = (
            capo_networkmanager.types.context_store_list.deserialize_json(
                data["ContextStores"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
