"""Generated from Smithy shape ``com.amazonaws.location#DeviceState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.cell_signals
    import capo_location.types.id
    import capo_location.types.position
    import capo_location.types.positional_accuracy
    import capo_location.types.timestamp
    import capo_location.types.wi_fi_access_point_list


class DeviceState(TypedDict, closed=True):
    device_id: "capo_location.types.id.Id"
    """<p>The device identifier.</p>"""
    sample_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp at which the device's position was determined. Uses <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601 </a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""
    position: "capo_location.types.position.Position"
    """<p>The last known device position.</p>"""
    accuracy: NotRequired["capo_location.types.positional_accuracy.PositionalAccuracy"]
    ipv4_address: NotRequired["str"]
    """<p>The device's Ipv4 address.</p>"""
    wi_fi_access_points: NotRequired[
        "capo_location.types.wi_fi_access_point_list.WiFiAccessPointList"
    ]
    """<p>The Wi-Fi access points the device is using.</p>"""
    cell_signals: NotRequired["capo_location.types.cell_signals.CellSignals"]
    """<p>The cellular network infrastructure that the device is connected to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeviceState) -> dict:
    out: dict = {}
    out["DeviceId"] = value["device_id"]
    import capo_location.types.timestamp

    out["SampleTime"] = capo_location.types.timestamp.serialize_json(
        value["sample_time"]
    )
    import capo_location.types.position

    out["Position"] = capo_location.types.position.serialize_json(value["position"])
    if "accuracy" in value:
        import capo_location.types.positional_accuracy

        out["Accuracy"] = capo_location.types.positional_accuracy.serialize_json(
            value["accuracy"]
        )
    if "ipv4_address" in value:
        out["Ipv4Address"] = value["ipv4_address"]
    if "wi_fi_access_points" in value:
        import capo_location.types.wi_fi_access_point_list

        out["WiFiAccessPoints"] = (
            capo_location.types.wi_fi_access_point_list.serialize_json(
                value["wi_fi_access_points"]
            )
        )
    if "cell_signals" in value:
        import capo_location.types.cell_signals

        out["CellSignals"] = capo_location.types.cell_signals.serialize_json(
            value["cell_signals"]
        )
    return out


def deserialize_json(data: dict) -> DeviceState:
    out: DeviceState = {}  # type: ignore[typeddict-item]
    if data.get("DeviceId") is not None:
        out["device_id"] = data["DeviceId"]
    else:
        raise DeserializationError("DeviceState.device_id required")
    if data.get("SampleTime") is not None:
        import capo_location.types.timestamp

        out["sample_time"] = capo_location.types.timestamp.deserialize_json(
            data["SampleTime"]
        )
    else:
        raise DeserializationError("DeviceState.sample_time required")
    if data.get("Position") is not None:
        import capo_location.types.position

        out["position"] = capo_location.types.position.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError("DeviceState.position required")
    if data.get("Accuracy") is not None:
        import capo_location.types.positional_accuracy

        out["accuracy"] = capo_location.types.positional_accuracy.deserialize_json(
            data["Accuracy"]
        )
    if data.get("Ipv4Address") is not None:
        out["ipv4_address"] = data["Ipv4Address"]
    if data.get("WiFiAccessPoints") is not None:
        import capo_location.types.wi_fi_access_point_list

        out["wi_fi_access_points"] = (
            capo_location.types.wi_fi_access_point_list.deserialize_json(
                data["WiFiAccessPoints"]
            )
        )
    if data.get("CellSignals") is not None:
        import capo_location.types.cell_signals

        out["cell_signals"] = capo_location.types.cell_signals.deserialize_json(
            data["CellSignals"]
        )
    return out
