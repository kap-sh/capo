"""Generated from Smithy shape ``com.amazonaws.glue#ColumnStatisticsData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.binary_column_statistics_data
    import capo_glue.types.boolean_column_statistics_data
    import capo_glue.types.column_statistics_type
    import capo_glue.types.date_column_statistics_data
    import capo_glue.types.decimal_column_statistics_data
    import capo_glue.types.double_column_statistics_data
    import capo_glue.types.long_column_statistics_data
    import capo_glue.types.string_column_statistics_data


class ColumnStatisticsData(TypedDict, closed=True):
    type: "capo_glue.types.column_statistics_type.ColumnStatisticsType"
    """<p>The type of column statistics data.</p>"""
    boolean_column_statistics_data: NotRequired[
        "capo_glue.types.boolean_column_statistics_data.BooleanColumnStatisticsData"
    ]
    """<p>Boolean column statistics data.</p>"""
    date_column_statistics_data: NotRequired[
        "capo_glue.types.date_column_statistics_data.DateColumnStatisticsData"
    ]
    """<p>Date column statistics data.</p>"""
    decimal_column_statistics_data: NotRequired[
        "capo_glue.types.decimal_column_statistics_data.DecimalColumnStatisticsData"
    ]
    """<p> Decimal column statistics data. UnscaledValues within are Base64-encoded binary objects storing big-endian, two's complement representations of the decimal's unscaled value. </p>"""
    double_column_statistics_data: NotRequired[
        "capo_glue.types.double_column_statistics_data.DoubleColumnStatisticsData"
    ]
    """<p>Double column statistics data.</p>"""
    long_column_statistics_data: NotRequired[
        "capo_glue.types.long_column_statistics_data.LongColumnStatisticsData"
    ]
    """<p>Long column statistics data.</p>"""
    string_column_statistics_data: NotRequired[
        "capo_glue.types.string_column_statistics_data.StringColumnStatisticsData"
    ]
    """<p>String column statistics data.</p>"""
    binary_column_statistics_data: NotRequired[
        "capo_glue.types.binary_column_statistics_data.BinaryColumnStatisticsData"
    ]
    """<p>Binary column statistics data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnStatisticsData) -> dict:
    out: dict = {}
    import capo_glue.types.column_statistics_type

    out["Type"] = capo_glue.types.column_statistics_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "boolean_column_statistics_data" in value:
        import capo_glue.types.boolean_column_statistics_data

        out["BooleanColumnStatisticsData"] = (
            capo_glue.types.boolean_column_statistics_data.serialize_aws_json_1_1(
                value["boolean_column_statistics_data"]
            )
        )
    if "date_column_statistics_data" in value:
        import capo_glue.types.date_column_statistics_data

        out["DateColumnStatisticsData"] = (
            capo_glue.types.date_column_statistics_data.serialize_aws_json_1_1(
                value["date_column_statistics_data"]
            )
        )
    if "decimal_column_statistics_data" in value:
        import capo_glue.types.decimal_column_statistics_data

        out["DecimalColumnStatisticsData"] = (
            capo_glue.types.decimal_column_statistics_data.serialize_aws_json_1_1(
                value["decimal_column_statistics_data"]
            )
        )
    if "double_column_statistics_data" in value:
        import capo_glue.types.double_column_statistics_data

        out["DoubleColumnStatisticsData"] = (
            capo_glue.types.double_column_statistics_data.serialize_aws_json_1_1(
                value["double_column_statistics_data"]
            )
        )
    if "long_column_statistics_data" in value:
        import capo_glue.types.long_column_statistics_data

        out["LongColumnStatisticsData"] = (
            capo_glue.types.long_column_statistics_data.serialize_aws_json_1_1(
                value["long_column_statistics_data"]
            )
        )
    if "string_column_statistics_data" in value:
        import capo_glue.types.string_column_statistics_data

        out["StringColumnStatisticsData"] = (
            capo_glue.types.string_column_statistics_data.serialize_aws_json_1_1(
                value["string_column_statistics_data"]
            )
        )
    if "binary_column_statistics_data" in value:
        import capo_glue.types.binary_column_statistics_data

        out["BinaryColumnStatisticsData"] = (
            capo_glue.types.binary_column_statistics_data.serialize_aws_json_1_1(
                value["binary_column_statistics_data"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ColumnStatisticsData:
    out: ColumnStatisticsData = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_glue.types.column_statistics_type

        out["type"] = capo_glue.types.column_statistics_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_glue.types.column_statistics_type.ColumnStatisticsType", ""
        )
    if data.get("BooleanColumnStatisticsData") is not None:
        import capo_glue.types.boolean_column_statistics_data

        out["boolean_column_statistics_data"] = (
            capo_glue.types.boolean_column_statistics_data.deserialize_aws_json_1_1(
                data["BooleanColumnStatisticsData"]
            )
        )
    if data.get("DateColumnStatisticsData") is not None:
        import capo_glue.types.date_column_statistics_data

        out["date_column_statistics_data"] = (
            capo_glue.types.date_column_statistics_data.deserialize_aws_json_1_1(
                data["DateColumnStatisticsData"]
            )
        )
    if data.get("DecimalColumnStatisticsData") is not None:
        import capo_glue.types.decimal_column_statistics_data

        out["decimal_column_statistics_data"] = (
            capo_glue.types.decimal_column_statistics_data.deserialize_aws_json_1_1(
                data["DecimalColumnStatisticsData"]
            )
        )
    if data.get("DoubleColumnStatisticsData") is not None:
        import capo_glue.types.double_column_statistics_data

        out["double_column_statistics_data"] = (
            capo_glue.types.double_column_statistics_data.deserialize_aws_json_1_1(
                data["DoubleColumnStatisticsData"]
            )
        )
    if data.get("LongColumnStatisticsData") is not None:
        import capo_glue.types.long_column_statistics_data

        out["long_column_statistics_data"] = (
            capo_glue.types.long_column_statistics_data.deserialize_aws_json_1_1(
                data["LongColumnStatisticsData"]
            )
        )
    if data.get("StringColumnStatisticsData") is not None:
        import capo_glue.types.string_column_statistics_data

        out["string_column_statistics_data"] = (
            capo_glue.types.string_column_statistics_data.deserialize_aws_json_1_1(
                data["StringColumnStatisticsData"]
            )
        )
    if data.get("BinaryColumnStatisticsData") is not None:
        import capo_glue.types.binary_column_statistics_data

        out["binary_column_statistics_data"] = (
            capo_glue.types.binary_column_statistics_data.deserialize_aws_json_1_1(
                data["BinaryColumnStatisticsData"]
            )
        )
    return out
