"""Generated from Smithy shape ``com.amazonaws.timestreamquery#Type``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.column_info
    import capo_timestream_query.types.column_info_list
    import capo_timestream_query.types.scalar_type


class Type(TypedDict, closed=True):
    scalar_type: NotRequired["capo_timestream_query.types.scalar_type.ScalarType"]
    """<p>Indicates if the column is of type string, integer, Boolean, double, timestamp, date, time. For more information, see <a href="https://docs.aws.amazon.com/timestream/latest/developerguide/supported-data-types.html">Supported data types</a>.</p>"""
    array_column_info: NotRequired["capo_timestream_query.types.column_info.ColumnInfo"]
    """<p>Indicates if the column is an array.</p>"""
    time_series_measure_value_column_info: NotRequired[
        "capo_timestream_query.types.column_info.ColumnInfo"
    ]
    """<p>Indicates if the column is a timeseries data type.</p>"""
    row_column_info: NotRequired[
        "capo_timestream_query.types.column_info_list.ColumnInfoList"
    ]
    """<p>Indicates if the column is a row.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Type) -> dict:
    out: dict = {}
    if "scalar_type" in value:
        import capo_timestream_query.types.scalar_type

        out["ScalarType"] = (
            capo_timestream_query.types.scalar_type.serialize_aws_json_1_0(
                value["scalar_type"]
            )
        )
    if "array_column_info" in value:
        import capo_timestream_query.types.column_info

        out["ArrayColumnInfo"] = (
            capo_timestream_query.types.column_info.serialize_aws_json_1_0(
                value["array_column_info"]
            )
        )
    if "time_series_measure_value_column_info" in value:
        import capo_timestream_query.types.column_info

        out["TimeSeriesMeasureValueColumnInfo"] = (
            capo_timestream_query.types.column_info.serialize_aws_json_1_0(
                value["time_series_measure_value_column_info"]
            )
        )
    if "row_column_info" in value:
        import capo_timestream_query.types.column_info_list

        out["RowColumnInfo"] = (
            capo_timestream_query.types.column_info_list.serialize_aws_json_1_0(
                value["row_column_info"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Type:
    out: Type = {}  # type: ignore[typeddict-item]
    if data.get("ScalarType") is not None:
        import capo_timestream_query.types.scalar_type

        out["scalar_type"] = (
            capo_timestream_query.types.scalar_type.deserialize_aws_json_1_0(
                data["ScalarType"]
            )
        )
    if data.get("ArrayColumnInfo") is not None:
        import capo_timestream_query.types.column_info

        out["array_column_info"] = (
            capo_timestream_query.types.column_info.deserialize_aws_json_1_0(
                data["ArrayColumnInfo"]
            )
        )
    if data.get("TimeSeriesMeasureValueColumnInfo") is not None:
        import capo_timestream_query.types.column_info

        out["time_series_measure_value_column_info"] = (
            capo_timestream_query.types.column_info.deserialize_aws_json_1_0(
                data["TimeSeriesMeasureValueColumnInfo"]
            )
        )
    if data.get("RowColumnInfo") is not None:
        import capo_timestream_query.types.column_info_list

        out["row_column_info"] = (
            capo_timestream_query.types.column_info_list.deserialize_aws_json_1_0(
                data["RowColumnInfo"]
            )
        )
    return out
