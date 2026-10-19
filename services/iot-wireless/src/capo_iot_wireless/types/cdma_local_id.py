"""Generated from Smithy shape ``com.amazonaws.iotwireless#CdmaLocalId``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.cdma_channel
    import capo_iot_wireless.types.pn_offset


class CdmaLocalId(TypedDict, closed=True):
    pn_offset: "capo_iot_wireless.types.pn_offset.PnOffset"
    """<p>Pseudo-noise offset, which is a characteristic of the signal from a cell on a radio tower.</p>"""
    cdma_channel: "capo_iot_wireless.types.cdma_channel.CdmaChannel"
    """<p>CDMA channel information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CdmaLocalId) -> dict:
    out: dict = {}
    out["PnOffset"] = value["pn_offset"]
    out["CdmaChannel"] = value["cdma_channel"]
    return out


def deserialize_json(data: dict) -> CdmaLocalId:
    out: CdmaLocalId = {}  # type: ignore[typeddict-item]
    if data.get("PnOffset") is not None:
        out["pn_offset"] = data["PnOffset"]
    else:
        out["pn_offset"] = 0
    if data.get("CdmaChannel") is not None:
        out["cdma_channel"] = data["CdmaChannel"]
    else:
        out["cdma_channel"] = 0
    return out
