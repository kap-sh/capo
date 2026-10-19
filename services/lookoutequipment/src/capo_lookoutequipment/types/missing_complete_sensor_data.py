"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#MissingCompleteSensorData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.integer


class MissingCompleteSensorData(TypedDict, closed=True):
    affected_sensor_count: "capo_lookoutequipment.types.integer.Integer"
    """<p> Indicates the number of sensors that have data missing completely. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MissingCompleteSensorData) -> dict:
    out: dict = {}
    out["AffectedSensorCount"] = value["affected_sensor_count"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MissingCompleteSensorData:
    out: MissingCompleteSensorData = {}  # type: ignore[typeddict-item]
    if data.get("AffectedSensorCount") is not None:
        out["affected_sensor_count"] = data["AffectedSensorCount"]
    else:
        out["affected_sensor_count"] = 0
    return out
