"""Generated from Smithy shape ``com.amazonaws.connect#ParticipantDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.display_name


class ParticipantDetails(TypedDict, closed=True):
    display_name: "capo_connect.types.display_name.DisplayName"
    """<p>Display name of the participant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantDetails) -> dict:
    out: dict = {}
    out["DisplayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> ParticipantDetails:
    out: ParticipantDetails = {}  # type: ignore[typeddict-item]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    else:
        out["display_name"] = ""
    return out
