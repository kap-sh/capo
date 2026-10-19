"""Generated from Smithy shape ``com.amazonaws.groundstation#OemProgramTrackSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.uuid


class OemProgramTrackSettings(TypedDict, closed=True):
    ephemeris_id: "capo_groundstation.types.uuid.Uuid"
    """<p>Unique identifier of the OEM ephemeris.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OemProgramTrackSettings) -> dict:
    out: dict = {}
    out["ephemerisId"] = value["ephemeris_id"]
    return out


def deserialize_json(data: dict) -> OemProgramTrackSettings:
    out: OemProgramTrackSettings = {}  # type: ignore[typeddict-item]
    if data.get("ephemerisId") is not None:
        out["ephemeris_id"] = data["ephemerisId"]
    else:
        out["ephemeris_id"] = ""
    return out
