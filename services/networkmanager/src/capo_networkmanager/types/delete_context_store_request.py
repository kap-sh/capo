"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeleteContextStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.context_store_id


class DeleteContextStoreRequest(TypedDict, closed=True):
    context_store_id: "capo_networkmanager.types.context_store_id.ContextStoreId"
    """<p>The ID of the context store to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteContextStoreRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteContextStoreRequest:
    out: DeleteContextStoreRequest = {}  # type: ignore[typeddict-item]
    return out
