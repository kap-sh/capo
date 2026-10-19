"""Generated from Smithy shape ``com.amazonaws.managedblockchain#RemoveAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.resource_id_string


class RemoveAction(TypedDict, closed=True):
    member_id: "capo_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the member to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveAction) -> dict:
    out: dict = {}
    out["MemberId"] = value["member_id"]
    return out


def deserialize_json(data: dict) -> RemoveAction:
    out: RemoveAction = {}  # type: ignore[typeddict-item]
    if data.get("MemberId") is not None:
        out["member_id"] = data["MemberId"]
    else:
        out["member_id"] = ""
    return out
