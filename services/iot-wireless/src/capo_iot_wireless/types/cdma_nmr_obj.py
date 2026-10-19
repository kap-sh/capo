"""Generated from Smithy shape ``com.amazonaws.iotwireless#CdmaNmrObj``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.base_station_id
    import capo_iot_wireless.types.cdma_channel
    import capo_iot_wireless.types.pilot_power
    import capo_iot_wireless.types.pn_offset


class CdmaNmrObj(TypedDict, closed=True):
    pn_offset: "capo_iot_wireless.types.pn_offset.PnOffset"
    """<p>Pseudo-noise offset, which is a characteristic of the signal from a cell on a radio tower.</p>"""
    cdma_channel: "capo_iot_wireless.types.cdma_channel.CdmaChannel"
    """<p>CDMA channel information.</p>"""
    pilot_power: NotRequired["capo_iot_wireless.types.pilot_power.PilotPower"]
    """<p>Transmit power level of the pilot signal, measured in dBm (decibel-milliwatts).</p>"""
    base_station_id: NotRequired[
        "capo_iot_wireless.types.base_station_id.BaseStationId"
    ]
    """<p>CDMA base station ID (BSID).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CdmaNmrObj) -> dict:
    out: dict = {}
    out["PnOffset"] = value["pn_offset"]
    out["CdmaChannel"] = value["cdma_channel"]
    if "pilot_power" in value:
        out["PilotPower"] = value["pilot_power"]
    if "base_station_id" in value:
        out["BaseStationId"] = value["base_station_id"]
    return out


def deserialize_json(data: dict) -> CdmaNmrObj:
    out: CdmaNmrObj = {}  # type: ignore[typeddict-item]
    if data.get("PnOffset") is not None:
        out["pn_offset"] = data["PnOffset"]
    else:
        out["pn_offset"] = 0
    if data.get("CdmaChannel") is not None:
        out["cdma_channel"] = data["CdmaChannel"]
    else:
        out["cdma_channel"] = 0
    if data.get("PilotPower") is not None:
        out["pilot_power"] = data["PilotPower"]
    if data.get("BaseStationId") is not None:
        out["base_station_id"] = data["BaseStationId"]
    return out
