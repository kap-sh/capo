"""Generated from Smithy shape ``com.amazonaws.iotwireless#GsmNmrObj``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.bcch
    import capo_iot_wireless.types.bsic
    import capo_iot_wireless.types.global_identity
    import capo_iot_wireless.types.rx_level


class GsmNmrObj(TypedDict, closed=True):
    bsic: "capo_iot_wireless.types.bsic.BSIC"
    """<p>GSM base station identity code (BSIC).</p>"""
    bcch: "capo_iot_wireless.types.bcch.BCCH"
    """<p>GSM broadcast control channel.</p>"""
    rx_level: NotRequired["capo_iot_wireless.types.rx_level.RxLevel"]
    """<p>Rx level, which is the received signal power, measured in dBm (decibel-milliwatts).</p>"""
    global_identity: NotRequired[
        "capo_iot_wireless.types.global_identity.GlobalIdentity"
    ]
    """<p>Global identity information of the GSM object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GsmNmrObj) -> dict:
    out: dict = {}
    out["Bsic"] = value["bsic"]
    out["Bcch"] = value["bcch"]
    if "rx_level" in value:
        out["RxLevel"] = value["rx_level"]
    if "global_identity" in value:
        import capo_iot_wireless.types.global_identity

        out["GlobalIdentity"] = capo_iot_wireless.types.global_identity.serialize_json(
            value["global_identity"]
        )
    return out


def deserialize_json(data: dict) -> GsmNmrObj:
    out: GsmNmrObj = {}  # type: ignore[typeddict-item]
    if data.get("Bsic") is not None:
        out["bsic"] = data["Bsic"]
    else:
        out["bsic"] = 0
    if data.get("Bcch") is not None:
        out["bcch"] = data["Bcch"]
    else:
        out["bcch"] = 0
    if data.get("RxLevel") is not None:
        out["rx_level"] = data["RxLevel"]
    if data.get("GlobalIdentity") is not None:
        import capo_iot_wireless.types.global_identity

        out["global_identity"] = (
            capo_iot_wireless.types.global_identity.deserialize_json(
                data["GlobalIdentity"]
            )
        )
    return out
