"""Generated from Smithy shape ``com.amazonaws.pi#DataPoint``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pi.types.double
    import capo_pi.types.iso_timestamp


class DataPoint(TypedDict, closed=True):
    timestamp: "capo_pi.types.iso_timestamp.ISOTimestamp"
    """<p>The time, in epoch format, associated with a particular <code>Value</code>.</p>"""
    value: "capo_pi.types.double.Double"
    """<p>The actual value associated with a particular <code>Timestamp</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataPoint) -> dict:
    out: dict = {}
    import capo_pi.types.iso_timestamp

    out["Timestamp"] = capo_pi.types.iso_timestamp.serialize_aws_json_1_1(
        value["timestamp"]
    )
    out["Value"] = (
        "NaN"
        if value["value"] != value["value"]
        else "Infinity"
        if value["value"] == float("inf")
        else "-Infinity"
        if value["value"] == float("-inf")
        else value["value"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataPoint:
    out: DataPoint = {}  # type: ignore[typeddict-item]
    if data.get("Timestamp") is not None:
        import capo_pi.types.iso_timestamp

        out["timestamp"] = capo_pi.types.iso_timestamp.deserialize_aws_json_1_1(
            data["Timestamp"]
        )
    else:
        import datetime

        out["timestamp"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Value") is not None:
        out["value"] = float(data["Value"])
    else:
        out["value"] = 0.0
    return out
