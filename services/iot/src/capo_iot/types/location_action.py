"""Generated from Smithy shape ``com.amazonaws.iot#LocationAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.aws_arn
    import capo_iot.types.location_timestamp
    import capo_iot.types.string


class LocationAction(TypedDict, closed=True):
    role_arn: "capo_iot.types.aws_arn.AwsArn"
    """<p>The IAM role that grants permission to write to the Amazon Location resource.</p>"""
    tracker_name: "capo_iot.types.string.String"
    """<p>The name of the tracker resource in Amazon Location in which the location is updated.</p>"""
    device_id: "capo_iot.types.string.String"
    """<p>The unique ID of the device providing the location data.</p>"""
    timestamp: NotRequired["capo_iot.types.location_timestamp.LocationTimestamp"]
    """<p>The time that the location data was sampled. The default value is the time the MQTT message was processed.</p>"""
    latitude: "capo_iot.types.string.String"
    """<p>A string that evaluates to a double value that represents the latitude of the device's location.</p>"""
    longitude: "capo_iot.types.string.String"
    """<p>A string that evaluates to a double value that represents the longitude of the device's location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LocationAction) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    out["trackerName"] = value["tracker_name"]
    out["deviceId"] = value["device_id"]
    if "timestamp" in value:
        import capo_iot.types.location_timestamp

        out["timestamp"] = capo_iot.types.location_timestamp.serialize_json(
            value["timestamp"]
        )
    out["latitude"] = value["latitude"]
    out["longitude"] = value["longitude"]
    return out


def deserialize_json(data: dict) -> LocationAction:
    out: LocationAction = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("trackerName") is not None:
        out["tracker_name"] = data["trackerName"]
    else:
        out["tracker_name"] = ""
    if data.get("deviceId") is not None:
        out["device_id"] = data["deviceId"]
    else:
        out["device_id"] = ""
    if data.get("timestamp") is not None:
        import capo_iot.types.location_timestamp

        out["timestamp"] = capo_iot.types.location_timestamp.deserialize_json(
            data["timestamp"]
        )
    if data.get("latitude") is not None:
        out["latitude"] = data["latitude"]
    else:
        out["latitude"] = ""
    if data.get("longitude") is not None:
        out["longitude"] = data["longitude"]
    else:
        out["longitude"] = ""
    return out
