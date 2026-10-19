"""Generated from Smithy shape ``com.amazonaws.iotwireless#TdscdmaObj``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.lac
    import capo_iot_wireless.types.mcc
    import capo_iot_wireless.types.mnc
    import capo_iot_wireless.types.path_loss
    import capo_iot_wireless.types.rscp
    import capo_iot_wireless.types.tdscdma_local_id
    import capo_iot_wireless.types.tdscdma_nmr_list
    import capo_iot_wireless.types.tdscdma_timing_advance
    import capo_iot_wireless.types.utran_cid


class TdscdmaObj(TypedDict, closed=True):
    mcc: "capo_iot_wireless.types.mcc.MCC"
    """<p>Mobile Country Code.</p>"""
    mnc: "capo_iot_wireless.types.mnc.MNC"
    """<p>Mobile Network Code.</p>"""
    lac: NotRequired["capo_iot_wireless.types.lac.LAC"]
    """<p>Location Area Code.</p>"""
    utran_cid: "capo_iot_wireless.types.utran_cid.UtranCid"
    """<p>UTRAN (UMTS Terrestrial Radio Access Network) Cell Global Identifier.</p>"""
    tdscdma_local_id: NotRequired[
        "capo_iot_wireless.types.tdscdma_local_id.TdscdmaLocalId"
    ]
    """<p>TD-SCDMA local identification (local ID) information.</p>"""
    tdscdma_timing_advance: NotRequired[
        "capo_iot_wireless.types.tdscdma_timing_advance.TdscdmaTimingAdvance"
    ]
    """<p>TD-SCDMA Timing advance.</p>"""
    rscp: NotRequired["capo_iot_wireless.types.rscp.RSCP"]
    """<p>Signal power of the received signal (Received Signal Code Power), measured in decibel-milliwatts (dBm).</p>"""
    path_loss: NotRequired["capo_iot_wireless.types.path_loss.PathLoss"]
    """<p>Path loss, or path attenuation, is the reduction in power density of an electromagnetic wave as it propagates through space.</p>"""
    tdscdma_nmr: NotRequired["capo_iot_wireless.types.tdscdma_nmr_list.TdscdmaNmrList"]
    """<p>TD-SCDMA object for network measurement reports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TdscdmaObj) -> dict:
    out: dict = {}
    out["Mcc"] = value["mcc"]
    out["Mnc"] = value["mnc"]
    if "lac" in value:
        out["Lac"] = value["lac"]
    out["UtranCid"] = value["utran_cid"]
    if "tdscdma_local_id" in value:
        import capo_iot_wireless.types.tdscdma_local_id

        out["TdscdmaLocalId"] = capo_iot_wireless.types.tdscdma_local_id.serialize_json(
            value["tdscdma_local_id"]
        )
    if "tdscdma_timing_advance" in value:
        out["TdscdmaTimingAdvance"] = value["tdscdma_timing_advance"]
    if "rscp" in value:
        out["Rscp"] = value["rscp"]
    if "path_loss" in value:
        out["PathLoss"] = value["path_loss"]
    if "tdscdma_nmr" in value:
        import capo_iot_wireless.types.tdscdma_nmr_list

        out["TdscdmaNmr"] = capo_iot_wireless.types.tdscdma_nmr_list.serialize_json(
            value["tdscdma_nmr"]
        )
    return out


def deserialize_json(data: dict) -> TdscdmaObj:
    out: TdscdmaObj = {}  # type: ignore[typeddict-item]
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
    if data.get("TdscdmaLocalId") is not None:
        import capo_iot_wireless.types.tdscdma_local_id

        out["tdscdma_local_id"] = (
            capo_iot_wireless.types.tdscdma_local_id.deserialize_json(
                data["TdscdmaLocalId"]
            )
        )
    if data.get("TdscdmaTimingAdvance") is not None:
        out["tdscdma_timing_advance"] = data["TdscdmaTimingAdvance"]
    if data.get("Rscp") is not None:
        out["rscp"] = data["Rscp"]
    if data.get("PathLoss") is not None:
        out["path_loss"] = data["PathLoss"]
    if data.get("TdscdmaNmr") is not None:
        import capo_iot_wireless.types.tdscdma_nmr_list

        out["tdscdma_nmr"] = capo_iot_wireless.types.tdscdma_nmr_list.deserialize_json(
            data["TdscdmaNmr"]
        )
    return out
