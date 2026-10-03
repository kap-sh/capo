"""Generated from Smithy shape ``com.amazonaws.location#ListDevicePositionsResponseEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.id
    import capo_location.types.position
    import capo_location.types.position_property_map
    import capo_location.types.positional_accuracy
    import capo_location.types.timestamp


class ListDevicePositionsResponseEntry(TypedDict, closed=True):
    device_id: "capo_location.types.id.Id"
    """<p>The ID of the device for this position.</p>"""
    sample_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp at which the device position was determined. Uses <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>.</p>"""
    position: "capo_location.types.position.Position"
    """<p>The last known device position. Empty if no positions currently stored.</p>"""
    accuracy: NotRequired["capo_location.types.positional_accuracy.PositionalAccuracy"]
    """<p>The accuracy of the device position.</p>"""
    position_properties: NotRequired[
        "capo_location.types.position_property_map.PositionPropertyMap"
    ]
    """<p>The properties associated with the position.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDevicePositionsResponseEntry) -> dict:
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
    if "position_properties" in value:
        import capo_location.types.position_property_map

        out["PositionProperties"] = (
            capo_location.types.position_property_map.serialize_json(
                value["position_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListDevicePositionsResponseEntry:
    out: ListDevicePositionsResponseEntry = {}  # type: ignore[typeddict-item]
    if data.get("DeviceId") is not None:
        out["device_id"] = data["DeviceId"]
    else:
        raise DeserializationError(
            "ListDevicePositionsResponseEntry.device_id required"
        )
    if data.get("SampleTime") is not None:
        import capo_location.types.timestamp

        out["sample_time"] = capo_location.types.timestamp.deserialize_json(
            data["SampleTime"]
        )
    else:
        raise DeserializationError(
            "ListDevicePositionsResponseEntry.sample_time required"
        )
    if data.get("Position") is not None:
        import capo_location.types.position

        out["position"] = capo_location.types.position.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError("ListDevicePositionsResponseEntry.position required")
    if data.get("Accuracy") is not None:
        import capo_location.types.positional_accuracy

        out["accuracy"] = capo_location.types.positional_accuracy.deserialize_json(
            data["Accuracy"]
        )
    if data.get("PositionProperties") is not None:
        import capo_location.types.position_property_map

        out["position_properties"] = (
            capo_location.types.position_property_map.deserialize_json(
                data["PositionProperties"]
            )
        )
    return out
