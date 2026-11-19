"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetContextVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.context_store_id


class GetContextVersionRequest(TypedDict, closed=True):
    context_store_id: "capo_networkmanager.types.context_store_id.ContextStoreId"
    """<p>The ID of the context store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContextVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetContextVersionRequest:
    out: GetContextVersionRequest = {}  # type: ignore[typeddict-item]
    return out
