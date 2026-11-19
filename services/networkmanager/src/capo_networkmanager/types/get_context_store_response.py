"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetContextStoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.context_store


class GetContextStoreResponse(TypedDict, closed=True):
    context_store: NotRequired["capo_networkmanager.types.context_store.ContextStore"]
    """<p>Information about the context store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContextStoreResponse) -> dict:
    out: dict = {}
    if "context_store" in value:
        import capo_networkmanager.types.context_store

        out["ContextStore"] = capo_networkmanager.types.context_store.serialize_json(
            value["context_store"]
        )
    return out


def deserialize_json(data: dict) -> GetContextStoreResponse:
    out: GetContextStoreResponse = {}  # type: ignore[typeddict-item]
    if data.get("ContextStore") is not None:
        import capo_networkmanager.types.context_store

        out["context_store"] = capo_networkmanager.types.context_store.deserialize_json(
            data["ContextStore"]
        )
    return out
