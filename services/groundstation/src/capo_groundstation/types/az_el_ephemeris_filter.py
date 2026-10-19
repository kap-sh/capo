"""Generated from Smithy shape ``com.amazonaws.groundstation#AzElEphemerisFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.uuid


class AzElEphemerisFilter(TypedDict, closed=True):
    id: "capo_groundstation.types.uuid.Uuid"
    """<p>Unique identifier of the azimuth elevation ephemeris.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzElEphemerisFilter) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> AzElEphemerisFilter:
    out: AzElEphemerisFilter = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out
