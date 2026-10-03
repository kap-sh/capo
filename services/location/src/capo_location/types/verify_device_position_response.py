"""Generated from Smithy shape ``com.amazonaws.location#VerifyDevicePositionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.distance_unit
    import capo_location.types.id
    import capo_location.types.inferred_state
    import capo_location.types.timestamp


class VerifyDevicePositionResponse(TypedDict, closed=True):
    inferred_state: "capo_location.types.inferred_state.InferredState"
    """<p>The inferred state of the device, given the provided position, IP address, cellular signals, and Wi-Fi- access points.</p>"""
    device_id: "capo_location.types.id.Id"
    """<p>The device identifier.</p>"""
    sample_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp at which the device's position was determined. Uses <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601 </a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""
    received_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the tracker resource received the device position in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601 </a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""
    distance_unit: "capo_location.types.distance_unit.DistanceUnit"
    """<p>The distance unit for the verification response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VerifyDevicePositionResponse) -> dict:
    out: dict = {}
    import capo_location.types.inferred_state

    out["InferredState"] = capo_location.types.inferred_state.serialize_json(
        value["inferred_state"]
    )
    out["DeviceId"] = value["device_id"]
    import capo_location.types.timestamp

    out["SampleTime"] = capo_location.types.timestamp.serialize_json(
        value["sample_time"]
    )
    import capo_location.types.timestamp

    out["ReceivedTime"] = capo_location.types.timestamp.serialize_json(
        value["received_time"]
    )
    out["DistanceUnit"] = value["distance_unit"]
    return out


def deserialize_json(data: dict) -> VerifyDevicePositionResponse:
    out: VerifyDevicePositionResponse = {}  # type: ignore[typeddict-item]
    if data.get("InferredState") is not None:
        import capo_location.types.inferred_state

        out["inferred_state"] = capo_location.types.inferred_state.deserialize_json(
            data["InferredState"]
        )
    else:
        raise DeserializationError(
            "VerifyDevicePositionResponse.inferred_state required"
        )
    if data.get("DeviceId") is not None:
        out["device_id"] = data["DeviceId"]
    else:
        raise DeserializationError("VerifyDevicePositionResponse.device_id required")
    if data.get("SampleTime") is not None:
        import capo_location.types.timestamp

        out["sample_time"] = capo_location.types.timestamp.deserialize_json(
            data["SampleTime"]
        )
    else:
        raise DeserializationError("VerifyDevicePositionResponse.sample_time required")
    if data.get("ReceivedTime") is not None:
        import capo_location.types.timestamp

        out["received_time"] = capo_location.types.timestamp.deserialize_json(
            data["ReceivedTime"]
        )
    else:
        raise DeserializationError(
            "VerifyDevicePositionResponse.received_time required"
        )
    if data.get("DistanceUnit") is not None:
        out["distance_unit"] = data["DistanceUnit"]
    else:
        raise DeserializationError(
            "VerifyDevicePositionResponse.distance_unit required"
        )
    return out
