"""Generated from Smithy shape ``com.amazonaws.iotwireless#GsmLocalId``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.bcch
    import capo_iot_wireless.types.bsic


class GsmLocalId(TypedDict, closed=True):
    bsic: "capo_iot_wireless.types.bsic.BSIC"
    """<p>GSM base station identity code (BSIC).</p>"""
    bcch: "capo_iot_wireless.types.bcch.BCCH"
    """<p>GSM broadcast control channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GsmLocalId) -> dict:
    out: dict = {}
    out["Bsic"] = value["bsic"]
    out["Bcch"] = value["bcch"]
    return out


def deserialize_json(data: dict) -> GsmLocalId:
    out: GsmLocalId = {}  # type: ignore[typeddict-item]
    if data.get("Bsic") is not None:
        out["bsic"] = data["Bsic"]
    else:
        out["bsic"] = 0
    if data.get("Bcch") is not None:
        out["bcch"] = data["Bcch"]
    else:
        out["bcch"] = 0
    return out
