"""Generated from Smithy shape ``com.amazonaws.networkmanager#UpdateContextStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.context_store_id


class UpdateContextStoreRequest(TypedDict, closed=True):
    context_store_id: "capo_networkmanager.types.context_store_id.ContextStoreId"
    """<p>The ID of the context store.</p>"""
    description: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The new description of the context store.</p> <p>Constraints: Maximum length of 256 characters. Only printable ASCII characters are allowed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateContextStoreRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateContextStoreRequest:
    out: UpdateContextStoreRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
