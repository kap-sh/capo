"""Generated from Smithy shape ``com.amazonaws.datazone#OwnerGroupProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.group_identifier


class OwnerGroupProperties(TypedDict, closed=True):
    group_identifier: "capo_datazone.types.group_identifier.GroupIdentifier"
    """<p>The ID of the domain unit owners group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OwnerGroupProperties) -> dict:
    out: dict = {}
    out["groupIdentifier"] = value["group_identifier"]
    return out


def deserialize_json(data: dict) -> OwnerGroupProperties:
    out: OwnerGroupProperties = {}  # type: ignore[typeddict-item]
    if data.get("groupIdentifier") is not None:
        out["group_identifier"] = data["groupIdentifier"]
    else:
        out["group_identifier"] = ""
    return out
