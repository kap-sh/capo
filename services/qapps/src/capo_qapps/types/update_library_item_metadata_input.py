"""Generated from Smithy shape ``com.amazonaws.qapps#UpdateLibraryItemMetadataInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.instance_id
    import capo_qapps.types.uuid


class UpdateLibraryItemMetadataInput(TypedDict, closed=True):
    instance_id: "capo_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    library_item_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the updated library item.</p>"""
    is_verified: NotRequired["bool"]
    """<p>The verification status of the library item</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLibraryItemMetadataInput) -> dict:
    out: dict = {}
    out["libraryItemId"] = value["library_item_id"]
    if "is_verified" in value:
        out["isVerified"] = value["is_verified"]
    return out


def deserialize_json(data: dict) -> UpdateLibraryItemMetadataInput:
    out: UpdateLibraryItemMetadataInput = {}  # type: ignore[typeddict-item]
    if data.get("libraryItemId") is not None:
        out["library_item_id"] = data["libraryItemId"]
    else:
        out["library_item_id"] = ""
    if data.get("isVerified") is not None:
        out["is_verified"] = data["isVerified"]
    return out
