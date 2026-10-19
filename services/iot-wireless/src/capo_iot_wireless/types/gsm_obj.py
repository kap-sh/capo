"""Generated from Smithy shape ``com.amazonaws.iotwireless#GsmObj``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.geran_cid
    import capo_iot_wireless.types.gsm_local_id
    import capo_iot_wireless.types.gsm_nmr_list
    import capo_iot_wireless.types.gsm_timing_advance
    import capo_iot_wireless.types.lac
    import capo_iot_wireless.types.mcc
    import capo_iot_wireless.types.mnc
    import capo_iot_wireless.types.rx_level


class GsmObj(TypedDict, closed=True):
    mcc: "capo_iot_wireless.types.mcc.MCC"
    """<p>Mobile Country Code.</p>"""
    mnc: "capo_iot_wireless.types.mnc.MNC"
    """<p>Mobile Network Code.</p>"""
    lac: "capo_iot_wireless.types.lac.LAC"
    """<p>Location area code.</p>"""
    geran_cid: "capo_iot_wireless.types.geran_cid.GeranCid"
    """<p>GERAN (GSM EDGE Radio Access Network) Cell Global Identifier.</p>"""
    gsm_local_id: NotRequired["capo_iot_wireless.types.gsm_local_id.GsmLocalId"]
    """<p>GSM local identification (local ID) information.</p>"""
    gsm_timing_advance: NotRequired[
        "capo_iot_wireless.types.gsm_timing_advance.GsmTimingAdvance"
    ]
    """<p>Timing advance value, which corresponds to the length of time a signal takes to reach the base station from a mobile phone.</p>"""
    rx_level: NotRequired["capo_iot_wireless.types.rx_level.RxLevel"]
    """<p>Rx level, which is the received signal power, measured in dBm (decibel-milliwatts).</p>"""
    gsm_nmr: NotRequired["capo_iot_wireless.types.gsm_nmr_list.GsmNmrList"]
    """<p>GSM object for network measurement reports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GsmObj) -> dict:
    out: dict = {}
    out["Mcc"] = value["mcc"]
    out["Mnc"] = value["mnc"]
    out["Lac"] = value["lac"]
    out["GeranCid"] = value["geran_cid"]
    if "gsm_local_id" in value:
        import capo_iot_wireless.types.gsm_local_id

        out["GsmLocalId"] = capo_iot_wireless.types.gsm_local_id.serialize_json(
            value["gsm_local_id"]
        )
    if "gsm_timing_advance" in value:
        out["GsmTimingAdvance"] = value["gsm_timing_advance"]
    if "rx_level" in value:
        out["RxLevel"] = value["rx_level"]
    if "gsm_nmr" in value:
        import capo_iot_wireless.types.gsm_nmr_list

        out["GsmNmr"] = capo_iot_wireless.types.gsm_nmr_list.serialize_json(
            value["gsm_nmr"]
        )
    return out


def deserialize_json(data: dict) -> GsmObj:
    out: GsmObj = {}  # type: ignore[typeddict-item]
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
    else:
        out["lac"] = 0
    if data.get("GeranCid") is not None:
        out["geran_cid"] = data["GeranCid"]
    else:
        out["geran_cid"] = 0
    if data.get("GsmLocalId") is not None:
        import capo_iot_wireless.types.gsm_local_id

        out["gsm_local_id"] = capo_iot_wireless.types.gsm_local_id.deserialize_json(
            data["GsmLocalId"]
        )
    if data.get("GsmTimingAdvance") is not None:
        out["gsm_timing_advance"] = data["GsmTimingAdvance"]
    if data.get("RxLevel") is not None:
        out["rx_level"] = data["RxLevel"]
    if data.get("GsmNmr") is not None:
        import capo_iot_wireless.types.gsm_nmr_list

        out["gsm_nmr"] = capo_iot_wireless.types.gsm_nmr_list.deserialize_json(
            data["GsmNmr"]
        )
    return out
