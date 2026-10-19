"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#MissingSensorData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.integer


class MissingSensorData(TypedDict, closed=True):
    affected_sensor_count: "capo_lookoutequipment.types.integer.Integer"
    """<p> Indicates the number of sensors that have atleast some data missing. </p>"""
    total_number_of_missing_values: "capo_lookoutequipment.types.integer.Integer"
    """<p> Indicates the total number of missing values across all the sensors. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MissingSensorData) -> dict:
    out: dict = {}
    out["AffectedSensorCount"] = value["affected_sensor_count"]
    out["TotalNumberOfMissingValues"] = value["total_number_of_missing_values"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MissingSensorData:
    out: MissingSensorData = {}  # type: ignore[typeddict-item]
    if data.get("AffectedSensorCount") is not None:
        out["affected_sensor_count"] = data["AffectedSensorCount"]
    else:
        out["affected_sensor_count"] = 0
    if data.get("TotalNumberOfMissingValues") is not None:
        out["total_number_of_missing_values"] = data["TotalNumberOfMissingValues"]
    else:
        out["total_number_of_missing_values"] = 0
    return out
