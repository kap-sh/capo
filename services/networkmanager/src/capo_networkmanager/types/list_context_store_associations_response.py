"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListContextStoreAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.context_store_association_list
    import capo_networkmanager.types.next_token


class ListContextStoreAssociationsResponse(TypedDict, closed=True):
    context_store_associations: NotRequired[
        "capo_networkmanager.types.context_store_association_list.ContextStoreAssociationList"
    ]
    """<p>The context store associations.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContextStoreAssociationsResponse) -> dict:
    out: dict = {}
    if "context_store_associations" in value:
        import capo_networkmanager.types.context_store_association_list

        out["ContextStoreAssociations"] = (
            capo_networkmanager.types.context_store_association_list.serialize_json(
                value["context_store_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListContextStoreAssociationsResponse:
    out: ListContextStoreAssociationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ContextStoreAssociations") is not None:
        import capo_networkmanager.types.context_store_association_list

        out["context_store_associations"] = (
            capo_networkmanager.types.context_store_association_list.deserialize_json(
                data["ContextStoreAssociations"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
