"""Generated from Smithy shape ``com.amazonaws.iotwireless#GlobalIdentity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.geran_cid
    import capo_iot_wireless.types.lac


class GlobalIdentity(TypedDict, closed=True):
    lac: "capo_iot_wireless.types.lac.LAC"
    """<p>Location area code of the global identity.</p>"""
    geran_cid: "capo_iot_wireless.types.geran_cid.GeranCid"
    """<p>GERAN (GSM EDGE Radio Access Network) cell global identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlobalIdentity) -> dict:
    out: dict = {}
    out["Lac"] = value["lac"]
    out["GeranCid"] = value["geran_cid"]
    return out


def deserialize_json(data: dict) -> GlobalIdentity:
    out: GlobalIdentity = {}  # type: ignore[typeddict-item]
    if data.get("Lac") is not None:
        out["lac"] = data["Lac"]
    else:
        out["lac"] = 0
    if data.get("GeranCid") is not None:
        out["geran_cid"] = data["GeranCid"]
    else:
        out["geran_cid"] = 0
    return out
