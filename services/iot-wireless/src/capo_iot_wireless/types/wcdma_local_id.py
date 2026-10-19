"""Generated from Smithy shape ``com.amazonaws.iotwireless#WcdmaLocalId``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.psc
    import capo_iot_wireless.types.uarfcndl


class WcdmaLocalId(TypedDict, closed=True):
    uarfcndl: "capo_iot_wireless.types.uarfcndl.UARFCNDL"
    """<p>WCDMA UTRA Absolute RF Channel Number downlink.</p>"""
    psc: "capo_iot_wireless.types.psc.PSC"
    """<p>Primary Scrambling Code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WcdmaLocalId) -> dict:
    out: dict = {}
    out["Uarfcndl"] = value["uarfcndl"]
    out["Psc"] = value["psc"]
    return out


def deserialize_json(data: dict) -> WcdmaLocalId:
    out: WcdmaLocalId = {}  # type: ignore[typeddict-item]
    if data.get("Uarfcndl") is not None:
        out["uarfcndl"] = data["Uarfcndl"]
    else:
        out["uarfcndl"] = 0
    if data.get("Psc") is not None:
        out["psc"] = data["Psc"]
    else:
        out["psc"] = 0
    return out
