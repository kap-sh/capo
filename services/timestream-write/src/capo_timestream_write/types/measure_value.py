"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#MeasureValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_timestream_write.errors import DeserializationError

if TYPE_CHECKING:
    import capo_timestream_write.types.measure_value_type
    import capo_timestream_write.types.schema_name
    import capo_timestream_write.types.string_value2048


class MeasureValue(TypedDict, closed=True):
    name: "capo_timestream_write.types.schema_name.SchemaName"
    """<p> The name of the MeasureValue. </p> <p> For constraints on MeasureValue names, see <a href="https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html#limits.naming"> Naming Constraints</a> in the Amazon Timestream Developer Guide.</p>"""
    value: "capo_timestream_write.types.string_value2048.StringValue2048"
    """<p> The value for the MeasureValue. For information, see <a href="https://docs.aws.amazon.com/timestream/latest/developerguide/writes.html#writes.data-types">Data types</a>.</p>"""
    type: "capo_timestream_write.types.measure_value_type.MeasureValueType"
    """<p>Contains the data type of the MeasureValue for the time-series data point.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MeasureValue) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    import capo_timestream_write.types.measure_value_type

    out["Type"] = capo_timestream_write.types.measure_value_type.serialize_aws_json_1_0(
        value["type"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> MeasureValue:
    out: MeasureValue = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("MeasureValue.name required")
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("MeasureValue.value required")
    if data.get("Type") is not None:
        import capo_timestream_write.types.measure_value_type

        out["type"] = (
            capo_timestream_write.types.measure_value_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("MeasureValue.type required")
    return out
