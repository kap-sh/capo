"""Generated from Smithy shape ``com.amazonaws.timestreamquery#DimensionMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.dimension_value_type
    import capo_timestream_query.types.schema_name


class DimensionMapping(TypedDict, closed=True):
    name: "capo_timestream_query.types.schema_name.SchemaName"
    """<p>Column name from query result.</p>"""
    dimension_value_type: (
        "capo_timestream_query.types.dimension_value_type.DimensionValueType"
    )
    """<p>Type for the dimension. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DimensionMapping) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_timestream_query.types.dimension_value_type

    out["DimensionValueType"] = (
        capo_timestream_query.types.dimension_value_type.serialize_aws_json_1_0(
            value["dimension_value_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DimensionMapping:
    out: DimensionMapping = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("DimensionValueType") is not None:
        import capo_timestream_query.types.dimension_value_type

        out["dimension_value_type"] = (
            capo_timestream_query.types.dimension_value_type.deserialize_aws_json_1_0(
                data["DimensionValueType"]
            )
        )
    else:
        import typing

        out["dimension_value_type"] = typing.cast(
            "capo_timestream_query.types.dimension_value_type.DimensionValueType", ""
        )
    return out
