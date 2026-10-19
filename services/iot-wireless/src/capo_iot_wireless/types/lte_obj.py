"""Generated from Smithy shape ``com.amazonaws.iotwireless#LteObj``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.eutran_cid
    import capo_iot_wireless.types.lte_local_id
    import capo_iot_wireless.types.lte_nmr_list
    import capo_iot_wireless.types.lte_timing_advance
    import capo_iot_wireless.types.mcc
    import capo_iot_wireless.types.mnc
    import capo_iot_wireless.types.nr_capable
    import capo_iot_wireless.types.rsrp
    import capo_iot_wireless.types.rsrq
    import capo_iot_wireless.types.tac


class LteObj(TypedDict, closed=True):
    mcc: "capo_iot_wireless.types.mcc.MCC"
    """<p>Mobile Country Code.</p>"""
    mnc: "capo_iot_wireless.types.mnc.MNC"
    """<p>Mobile Network Code.</p>"""
    eutran_cid: "capo_iot_wireless.types.eutran_cid.EutranCid"
    """<p>E-UTRAN (Evolved Universal Terrestrial Radio Access Network) Cell Global Identifier.</p>"""
    tac: NotRequired["capo_iot_wireless.types.tac.TAC"]
    """<p>LTE tracking area code.</p>"""
    lte_local_id: NotRequired["capo_iot_wireless.types.lte_local_id.LteLocalId"]
    """<p>LTE local identification (local ID) information.</p>"""
    lte_timing_advance: NotRequired[
        "capo_iot_wireless.types.lte_timing_advance.LteTimingAdvance"
    ]
    """<p>LTE timing advance.</p>"""
    rsrp: NotRequired["capo_iot_wireless.types.rsrp.RSRP"]
    """<p>Signal power of the reference signal received, measured in dBm (decibel-milliwatts).</p>"""
    rsrq: NotRequired["capo_iot_wireless.types.rsrq.RSRQ"]
    """<p>Signal quality of the reference Signal received, measured in decibels (dB).</p>"""
    nr_capable: "capo_iot_wireless.types.nr_capable.NRCapable"
    """<p>Parameter that determines whether the LTE object is capable of supporting NR (new radio).</p>"""
    lte_nmr: NotRequired["capo_iot_wireless.types.lte_nmr_list.LteNmrList"]
    """<p>LTE object for network measurement reports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LteObj) -> dict:
    out: dict = {}
    out["Mcc"] = value["mcc"]
    out["Mnc"] = value["mnc"]
    out["EutranCid"] = value["eutran_cid"]
    if "tac" in value:
        out["Tac"] = value["tac"]
    if "lte_local_id" in value:
        import capo_iot_wireless.types.lte_local_id

        out["LteLocalId"] = capo_iot_wireless.types.lte_local_id.serialize_json(
            value["lte_local_id"]
        )
    if "lte_timing_advance" in value:
        out["LteTimingAdvance"] = value["lte_timing_advance"]
    if "rsrp" in value:
        out["Rsrp"] = value["rsrp"]
    if "rsrq" in value:
        out["Rsrq"] = (
            "NaN"
            if value["rsrq"] != value["rsrq"]
            else "Infinity"
            if value["rsrq"] == float("inf")
            else "-Infinity"
            if value["rsrq"] == float("-inf")
            else value["rsrq"]
        )
    out["NrCapable"] = value.get("nr_capable", False)
    if "lte_nmr" in value:
        import capo_iot_wireless.types.lte_nmr_list

        out["LteNmr"] = capo_iot_wireless.types.lte_nmr_list.serialize_json(
            value["lte_nmr"]
        )
    return out


def deserialize_json(data: dict) -> LteObj:
    out: LteObj = {}  # type: ignore[typeddict-item]
    if data.get("Mcc") is not None:
        out["mcc"] = data["Mcc"]
    else:
        out["mcc"] = 0
    if data.get("Mnc") is not None:
        out["mnc"] = data["Mnc"]
    else:
        out["mnc"] = 0
    if data.get("EutranCid") is not None:
        out["eutran_cid"] = data["EutranCid"]
    else:
        out["eutran_cid"] = 0
    if data.get("Tac") is not None:
        out["tac"] = data["Tac"]
    if data.get("LteLocalId") is not None:
        import capo_iot_wireless.types.lte_local_id

        out["lte_local_id"] = capo_iot_wireless.types.lte_local_id.deserialize_json(
            data["LteLocalId"]
        )
    if data.get("LteTimingAdvance") is not None:
        out["lte_timing_advance"] = data["LteTimingAdvance"]
    if data.get("Rsrp") is not None:
        out["rsrp"] = data["Rsrp"]
    if data.get("Rsrq") is not None:
        out["rsrq"] = float(data["Rsrq"])
    if data.get("NrCapable") is not None:
        out["nr_capable"] = data["NrCapable"]
    else:
        out["nr_capable"] = False
    if data.get("LteNmr") is not None:
        import capo_iot_wireless.types.lte_nmr_list

        out["lte_nmr"] = capo_iot_wireless.types.lte_nmr_list.deserialize_json(
            data["LteNmr"]
        )
    return out
