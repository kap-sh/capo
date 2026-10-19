"""Generated from Smithy shape ``com.amazonaws.iotwireless#TdscdmaNmrObj``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.cell_params
    import capo_iot_wireless.types.path_loss
    import capo_iot_wireless.types.rscp
    import capo_iot_wireless.types.uarfcn
    import capo_iot_wireless.types.utran_cid


class TdscdmaNmrObj(TypedDict, closed=True):
    uarfcn: "capo_iot_wireless.types.uarfcn.UARFCN"
    """<p>TD-SCDMA UTRA (Universal Terrestrial Radio Access Network) absolute RF channel number.</p>"""
    cell_params: "capo_iot_wireless.types.cell_params.CellParams"
    """<p>Cell parameters for TD-SCDMA network measurement reports object.</p>"""
    utran_cid: NotRequired["capo_iot_wireless.types.utran_cid.UtranCid"]
    """<p>UTRAN (UMTS Terrestrial Radio Access Network) cell global identifier.</p>"""
    rscp: NotRequired["capo_iot_wireless.types.rscp.RSCP"]
    """<p>Code power of the received signal, measured in decibel-milliwatts (dBm).</p>"""
    path_loss: NotRequired["capo_iot_wireless.types.path_loss.PathLoss"]
    """<p>Path loss, or path attenuation, is the reduction in power density of an electromagnetic wave as it propagates through space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TdscdmaNmrObj) -> dict:
    out: dict = {}
    out["Uarfcn"] = value["uarfcn"]
    out["CellParams"] = value["cell_params"]
    if "utran_cid" in value:
        out["UtranCid"] = value["utran_cid"]
    if "rscp" in value:
        out["Rscp"] = value["rscp"]
    if "path_loss" in value:
        out["PathLoss"] = value["path_loss"]
    return out


def deserialize_json(data: dict) -> TdscdmaNmrObj:
    out: TdscdmaNmrObj = {}  # type: ignore[typeddict-item]
    if data.get("Uarfcn") is not None:
        out["uarfcn"] = data["Uarfcn"]
    else:
        out["uarfcn"] = 0
    if data.get("CellParams") is not None:
        out["cell_params"] = data["CellParams"]
    else:
        out["cell_params"] = 0
    if data.get("UtranCid") is not None:
        out["utran_cid"] = data["UtranCid"]
    if data.get("Rscp") is not None:
        out["rscp"] = data["Rscp"]
    if data.get("PathLoss") is not None:
        out["path_loss"] = data["PathLoss"]
    return out
