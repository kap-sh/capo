"""Generated from Smithy shape ``com.amazonaws.iotwireless#LteNmrObj``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.earfcn
    import capo_iot_wireless.types.eutran_cid
    import capo_iot_wireless.types.pci
    import capo_iot_wireless.types.rsrp
    import capo_iot_wireless.types.rsrq


class LteNmrObj(TypedDict, closed=True):
    pci: "capo_iot_wireless.types.pci.PCI"
    """<p>Physical cell ID.</p>"""
    earfcn: "capo_iot_wireless.types.earfcn.EARFCN"
    """<p>E-UTRA (Evolved universal terrestrial Radio Access) absolute radio frequency channel Number (EARFCN).</p>"""
    eutran_cid: "capo_iot_wireless.types.eutran_cid.EutranCid"
    """<p>E-UTRAN (Evolved Universal Terrestrial Radio Access Network) cell global identifier (EUTRANCID).</p>"""
    rsrp: NotRequired["capo_iot_wireless.types.rsrp.RSRP"]
    """<p>Signal power of the reference signal received, measured in dBm (decibel-milliwatts).</p>"""
    rsrq: NotRequired["capo_iot_wireless.types.rsrq.RSRQ"]
    """<p>Signal quality of the reference Signal received, measured in decibels (dB).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LteNmrObj) -> dict:
    out: dict = {}
    out["Pci"] = value["pci"]
    out["Earfcn"] = value["earfcn"]
    out["EutranCid"] = value.get("eutran_cid", 0)
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
    return out


def deserialize_json(data: dict) -> LteNmrObj:
    out: LteNmrObj = {}  # type: ignore[typeddict-item]
    if data.get("Pci") is not None:
        out["pci"] = data["Pci"]
    else:
        out["pci"] = 0
    if data.get("Earfcn") is not None:
        out["earfcn"] = data["Earfcn"]
    else:
        out["earfcn"] = 0
    if data.get("EutranCid") is not None:
        out["eutran_cid"] = data["EutranCid"]
    else:
        out["eutran_cid"] = 0
    if data.get("Rsrp") is not None:
        out["rsrp"] = data["Rsrp"]
    if data.get("Rsrq") is not None:
        out["rsrq"] = float(data["Rsrq"])
    return out
