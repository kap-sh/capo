"""Generated from Smithy shape ``com.amazonaws.qapps#DeleteLibraryItemInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.instance_id
    import capo_qapps.types.uuid


class DeleteLibraryItemInput(TypedDict, closed=True):
    instance_id: "capo_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    library_item_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the library item to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLibraryItemInput) -> dict:
    out: dict = {}
    out["libraryItemId"] = value["library_item_id"]
    return out


def deserialize_json(data: dict) -> DeleteLibraryItemInput:
    out: DeleteLibraryItemInput = {}  # type: ignore[typeddict-item]
    if data.get("libraryItemId") is not None:
        out["library_item_id"] = data["libraryItemId"]
    else:
        out["library_item_id"] = ""
    return out
