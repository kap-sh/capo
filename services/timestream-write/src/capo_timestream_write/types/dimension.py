"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#Dimension``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_timestream_write.errors import DeserializationError

if TYPE_CHECKING:
    import capo_timestream_write.types.dimension_value_type
    import capo_timestream_write.types.schema_name
    import capo_timestream_write.types.schema_value


class Dimension(TypedDict, closed=True):
    name: "capo_timestream_write.types.schema_name.SchemaName"
    """<p> Dimension represents the metadata attributes of the time series. For example, the name and Availability Zone of an EC2 instance or the name of the manufacturer of a wind turbine are dimensions. </p> <p>For constraints on dimension names, see <a href="https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html#limits.naming">Naming Constraints</a>.</p>"""
    value: "capo_timestream_write.types.schema_value.SchemaValue"
    """<p>The value of the dimension.</p>"""
    dimension_value_type: NotRequired[
        "capo_timestream_write.types.dimension_value_type.DimensionValueType"
    ]
    """<p>The data type of the dimension for the time-series data point.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Dimension) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    if "dimension_value_type" in value:
        import capo_timestream_write.types.dimension_value_type

        out["DimensionValueType"] = (
            capo_timestream_write.types.dimension_value_type.serialize_aws_json_1_0(
                value["dimension_value_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Dimension:
    out: Dimension = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Dimension.name required")
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("Dimension.value required")
    if data.get("DimensionValueType") is not None:
        import capo_timestream_write.types.dimension_value_type

        out["dimension_value_type"] = (
            capo_timestream_write.types.dimension_value_type.deserialize_aws_json_1_0(
                data["DimensionValueType"]
            )
        )
    return out
