"""Generated from Smithy shape ``com.amazonaws.iotwireless#WcdmaObj``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.lac
    import capo_iot_wireless.types.mcc
    import capo_iot_wireless.types.mnc
    import capo_iot_wireless.types.path_loss
    import capo_iot_wireless.types.rscp
    import capo_iot_wireless.types.utran_cid
    import capo_iot_wireless.types.wcdma_local_id
    import capo_iot_wireless.types.wcdma_nmr_list


class WcdmaObj(TypedDict, closed=True):
    mcc: "capo_iot_wireless.types.mcc.MCC"
    """<p>Mobile Country Code.</p>"""
    mnc: "capo_iot_wireless.types.mnc.MNC"
    """<p>Mobile Network Code.</p>"""
    lac: NotRequired["capo_iot_wireless.types.lac.LAC"]
    """<p>Location Area Code.</p>"""
    utran_cid: "capo_iot_wireless.types.utran_cid.UtranCid"
    """<p>UTRAN (UMTS Terrestrial Radio Access Network) Cell Global Identifier.</p>"""
    wcdma_local_id: NotRequired["capo_iot_wireless.types.wcdma_local_id.WcdmaLocalId"]
    """<p>WCDMA local ID information.</p>"""
    rscp: NotRequired["capo_iot_wireless.types.rscp.RSCP"]
    """<p>Received Signal Code Power (signal power) (dBm).</p>"""
    path_loss: NotRequired["capo_iot_wireless.types.path_loss.PathLoss"]
    """<p>Path loss, or path attenuation, is the reduction in power density of an electromagnetic wave as it propagates through space.</p>"""
    wcdma_nmr: NotRequired["capo_iot_wireless.types.wcdma_nmr_list.WcdmaNmrList"]
    """<p>WCDMA object for network measurement reports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WcdmaObj) -> dict:
    out: dict = {}
    out["Mcc"] = value["mcc"]
    out["Mnc"] = value["mnc"]
    if "lac" in value:
        out["Lac"] = value["lac"]
    out["UtranCid"] = value["utran_cid"]
    if "wcdma_local_id" in value:
        import capo_iot_wireless.types.wcdma_local_id

        out["WcdmaLocalId"] = capo_iot_wireless.types.wcdma_local_id.serialize_json(
            value["wcdma_local_id"]
        )
    if "rscp" in value:
        out["Rscp"] = value["rscp"]
    if "path_loss" in value:
        out["PathLoss"] = value["path_loss"]
    if "wcdma_nmr" in value:
        import capo_iot_wireless.types.wcdma_nmr_list

        out["WcdmaNmr"] = capo_iot_wireless.types.wcdma_nmr_list.serialize_json(
            value["wcdma_nmr"]
        )
    return out


def deserialize_json(data: dict) -> WcdmaObj:
    out: WcdmaObj = {}  # type: ignore[typeddict-item]
    if data.get("Mcc") is not None:
        out["mcc"] = data["Mcc"]
    else:
        out["mcc"] = 0
    if data.get("Mnc") is not None:
        out["mnc"] = data["Mnc"]
    else:
        out["mnc"] = 0
    if data.get("Lac") is not None:
        out["lac"] = data["Lac"]
    if data.get("UtranCid") is not None:
        out["utran_cid"] = data["UtranCid"]
    else:
        out["utran_cid"] = 0
    if data.get("WcdmaLocalId") is not None:
        import capo_iot_wireless.types.wcdma_local_id

        out["wcdma_local_id"] = capo_iot_wireless.types.wcdma_local_id.deserialize_json(
            data["WcdmaLocalId"]
        )
    if data.get("Rscp") is not None:
        out["rscp"] = data["Rscp"]
    if data.get("PathLoss") is not None:
        out["path_loss"] = data["PathLoss"]
    if data.get("WcdmaNmr") is not None:
        import capo_iot_wireless.types.wcdma_nmr_list

        out["wcdma_nmr"] = capo_iot_wireless.types.wcdma_nmr_list.deserialize_json(
            data["WcdmaNmr"]
        )
    return out
