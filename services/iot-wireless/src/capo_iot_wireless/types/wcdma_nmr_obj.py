"""Generated from Smithy shape ``com.amazonaws.iotwireless#WcdmaNmrObj``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.path_loss
    import capo_iot_wireless.types.psc
    import capo_iot_wireless.types.rscp
    import capo_iot_wireless.types.uarfcndl
    import capo_iot_wireless.types.utran_cid


class WcdmaNmrObj(TypedDict, closed=True):
    uarfcndl: "capo_iot_wireless.types.uarfcndl.UARFCNDL"
    """<p>WCDMA UTRA Absolute RF Channel Number downlink.</p>"""
    psc: "capo_iot_wireless.types.psc.PSC"
    """<p>Primary Scrambling Code.</p>"""
    utran_cid: "capo_iot_wireless.types.utran_cid.UtranCid"
    """<p>UTRAN (UMTS Terrestrial Radio Access Network) Cell Global Identifier.</p>"""
    rscp: NotRequired["capo_iot_wireless.types.rscp.RSCP"]
    """<p>Received Signal Code Power (signal power) (dBm)</p>"""
    path_loss: NotRequired["capo_iot_wireless.types.path_loss.PathLoss"]
    """<p>Path loss, or path attenuation, is the reduction in power density of an electromagnetic wave as it propagates through space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WcdmaNmrObj) -> dict:
    out: dict = {}
    out["Uarfcndl"] = value["uarfcndl"]
    out["Psc"] = value["psc"]
    out["UtranCid"] = value["utran_cid"]
    if "rscp" in value:
        out["Rscp"] = value["rscp"]
    if "path_loss" in value:
        out["PathLoss"] = value["path_loss"]
    return out


def deserialize_json(data: dict) -> WcdmaNmrObj:
    out: WcdmaNmrObj = {}  # type: ignore[typeddict-item]
    if data.get("Uarfcndl") is not None:
        out["uarfcndl"] = data["Uarfcndl"]
    else:
        out["uarfcndl"] = 0
    if data.get("Psc") is not None:
        out["psc"] = data["Psc"]
    else:
        out["psc"] = 0
    if data.get("UtranCid") is not None:
        out["utran_cid"] = data["UtranCid"]
    else:
        out["utran_cid"] = 0
    if data.get("Rscp") is not None:
        out["rscp"] = data["Rscp"]
    if data.get("PathLoss") is not None:
        out["path_loss"] = data["PathLoss"]
    return out
