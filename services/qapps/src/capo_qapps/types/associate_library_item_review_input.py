"""Generated from Smithy shape ``com.amazonaws.qapps#AssociateLibraryItemReviewInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.instance_id
    import capo_qapps.types.uuid


class AssociateLibraryItemReviewInput(TypedDict, closed=True):
    instance_id: "capo_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier for the Amazon Q Business application environment instance.</p>"""
    library_item_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the library item to associate the review with.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateLibraryItemReviewInput) -> dict:
    out: dict = {}
    out["libraryItemId"] = value["library_item_id"]
    return out


def deserialize_json(data: dict) -> AssociateLibraryItemReviewInput:
    out: AssociateLibraryItemReviewInput = {}  # type: ignore[typeddict-item]
    if data.get("libraryItemId") is not None:
        out["library_item_id"] = data["libraryItemId"]
    else:
        out["library_item_id"] = ""
    return out
