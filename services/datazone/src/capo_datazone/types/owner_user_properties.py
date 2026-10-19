"""Generated from Smithy shape ``com.amazonaws.datazone#OwnerUserProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.user_identifier


class OwnerUserProperties(TypedDict, closed=True):
    user_identifier: "capo_datazone.types.user_identifier.UserIdentifier"
    """<p>The ID of the owner user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OwnerUserProperties) -> dict:
    out: dict = {}
    out["userIdentifier"] = value["user_identifier"]
    return out


def deserialize_json(data: dict) -> OwnerUserProperties:
    out: OwnerUserProperties = {}  # type: ignore[typeddict-item]
    if data.get("userIdentifier") is not None:
        out["user_identifier"] = data["userIdentifier"]
    else:
        out["user_identifier"] = ""
    return out
