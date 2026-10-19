"""Generated from Smithy shape ``com.amazonaws.lambda#EphemeralStorage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.ephemeral_storage_size


class EphemeralStorage(TypedDict, closed=True):
    size: "capo_lambda.types.ephemeral_storage_size.EphemeralStorageSize"
    """<p>The size of the function's <code>/tmp</code> directory.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EphemeralStorage) -> dict:
    out: dict = {}
    out["Size"] = value["size"]
    return out


def deserialize_json(data: dict) -> EphemeralStorage:
    out: EphemeralStorage = {}  # type: ignore[typeddict-item]
    if data.get("Size") is not None:
        out["size"] = data["Size"]
    else:
        out["size"] = 0
    return out
