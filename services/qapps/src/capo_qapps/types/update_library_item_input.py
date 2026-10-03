"""Generated from Smithy shape ``com.amazonaws.qapps#UpdateLibraryItemInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qapps.types.category_id_list
    import capo_qapps.types.instance_id
    import capo_qapps.types.library_item_status
    import capo_qapps.types.uuid


class UpdateLibraryItemInput(TypedDict, closed=True):
    instance_id: "capo_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    library_item_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the library item to update.</p>"""
    status: NotRequired["capo_qapps.types.library_item_status.LibraryItemStatus"]
    """<p>The new status to set for the library item, such as "Published" or "Hidden".</p>"""
    categories: NotRequired["capo_qapps.types.category_id_list.CategoryIdList"]
    """<p>The new categories to associate with the library item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLibraryItemInput) -> dict:
    out: dict = {}
    out["libraryItemId"] = value["library_item_id"]
    if "status" in value:
        import capo_qapps.types.library_item_status

        out["status"] = capo_qapps.types.library_item_status.serialize_json(
            value["status"]
        )
    if "categories" in value:
        import capo_qapps.types.category_id_list

        out["categories"] = capo_qapps.types.category_id_list.serialize_json(
            value["categories"]
        )
    return out


def deserialize_json(data: dict) -> UpdateLibraryItemInput:
    out: UpdateLibraryItemInput = {}  # type: ignore[typeddict-item]
    if data.get("libraryItemId") is not None:
        out["library_item_id"] = data["libraryItemId"]
    else:
        raise DeserializationError("UpdateLibraryItemInput.library_item_id required")
    if data.get("status") is not None:
        import capo_qapps.types.library_item_status

        out["status"] = capo_qapps.types.library_item_status.deserialize_json(
            data["status"]
        )
    if data.get("categories") is not None:
        import capo_qapps.types.category_id_list

        out["categories"] = capo_qapps.types.category_id_list.deserialize_json(
            data["categories"]
        )
    return out
