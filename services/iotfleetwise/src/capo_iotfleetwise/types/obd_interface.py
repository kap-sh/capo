"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ObdInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.non_negative_integer
    import capo_iotfleetwise.types.obd_interface_name
    import capo_iotfleetwise.types.obd_standard


class ObdInterface(TypedDict, closed=True):
    name: "capo_iotfleetwise.types.obd_interface_name.ObdInterfaceName"
    """<p>The name of the interface.</p>"""
    request_message_id: (
        "capo_iotfleetwise.types.non_negative_integer.nonNegativeInteger"
    )
    """<p>The ID of the message requesting vehicle data.</p>"""
    obd_standard: NotRequired["capo_iotfleetwise.types.obd_standard.ObdStandard"]
    """<p>The standard OBD II PID.</p>"""
    pid_request_interval_seconds: (
        "capo_iotfleetwise.types.non_negative_integer.nonNegativeInteger"
    )
    """<p>The maximum number message requests per second.</p>"""
    dtc_request_interval_seconds: (
        "capo_iotfleetwise.types.non_negative_integer.nonNegativeInteger"
    )
    """<p>The maximum number message requests per diagnostic trouble code per second.</p>"""
    use_extended_ids: "bool"
    """<p>Whether to use extended IDs in the message.</p>"""
    has_transmission_ecu: "bool"
    """<p>Whether the vehicle has a transmission control module (TCM).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ObdInterface) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["requestMessageId"] = value.get("request_message_id", 0)
    if "obd_standard" in value:
        out["obdStandard"] = value["obd_standard"]
    out["pidRequestIntervalSeconds"] = value.get("pid_request_interval_seconds", 0)
    out["dtcRequestIntervalSeconds"] = value.get("dtc_request_interval_seconds", 0)
    out["useExtendedIds"] = value.get("use_extended_ids", False)
    out["hasTransmissionEcu"] = value.get("has_transmission_ecu", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> ObdInterface:
    out: ObdInterface = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("requestMessageId") is not None:
        out["request_message_id"] = data["requestMessageId"]
    else:
        out["request_message_id"] = 0
    if data.get("obdStandard") is not None:
        out["obd_standard"] = data["obdStandard"]
    if data.get("pidRequestIntervalSeconds") is not None:
        out["pid_request_interval_seconds"] = data["pidRequestIntervalSeconds"]
    else:
        out["pid_request_interval_seconds"] = 0
    if data.get("dtcRequestIntervalSeconds") is not None:
        out["dtc_request_interval_seconds"] = data["dtcRequestIntervalSeconds"]
    else:
        out["dtc_request_interval_seconds"] = 0
    if data.get("useExtendedIds") is not None:
        out["use_extended_ids"] = data["useExtendedIds"]
    else:
        out["use_extended_ids"] = False
    if data.get("hasTransmissionEcu") is not None:
        out["has_transmission_ecu"] = data["hasTransmissionEcu"]
    else:
        out["has_transmission_ecu"] = False
    return out
