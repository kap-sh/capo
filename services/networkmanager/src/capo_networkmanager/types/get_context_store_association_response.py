"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetContextStoreAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.context_store_association


class GetContextStoreAssociationResponse(TypedDict, closed=True):
    context_store_association: NotRequired[
        "capo_networkmanager.types.context_store_association.ContextStoreAssociation"
    ]
    """<p>Information about the context store association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContextStoreAssociationResponse) -> dict:
    out: dict = {}
    if "context_store_association" in value:
        import capo_networkmanager.types.context_store_association

        out["ContextStoreAssociation"] = (
            capo_networkmanager.types.context_store_association.serialize_json(
                value["context_store_association"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetContextStoreAssociationResponse:
    out: GetContextStoreAssociationResponse = {}  # type: ignore[typeddict-item]
    if data.get("ContextStoreAssociation") is not None:
        import capo_networkmanager.types.context_store_association

        out["context_store_association"] = (
            capo_networkmanager.types.context_store_association.deserialize_json(
                data["ContextStoreAssociation"]
            )
        )
    return out
