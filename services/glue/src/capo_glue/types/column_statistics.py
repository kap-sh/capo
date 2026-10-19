"""Generated from Smithy shape ``com.amazonaws.glue#ColumnStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.column_statistics_data
    import capo_glue.types.name_string
    import capo_glue.types.timestamp
    import capo_glue.types.type_string


class ColumnStatistics(TypedDict, closed=True):
    column_name: "capo_glue.types.name_string.NameString"
    """<p>Name of column which statistics belong to.</p>"""
    column_type: "capo_glue.types.type_string.TypeString"
    """<p>The data type of the column.</p>"""
    analyzed_time: "capo_glue.types.timestamp.Timestamp"
    """<p>The timestamp of when column statistics were generated.</p>"""
    statistics_data: "capo_glue.types.column_statistics_data.ColumnStatisticsData"
    """<p>A <code>ColumnStatisticData</code> object that contains the statistics data values.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnStatistics) -> dict:
    out: dict = {}
    out["ColumnName"] = value["column_name"]
    out["ColumnType"] = value["column_type"]
    import capo_glue.types.timestamp

    out["AnalyzedTime"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
        value["analyzed_time"]
    )
    import capo_glue.types.column_statistics_data

    out["StatisticsData"] = (
        capo_glue.types.column_statistics_data.serialize_aws_json_1_1(
            value["statistics_data"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ColumnStatistics:
    out: ColumnStatistics = {}  # type: ignore[typeddict-item]
    if data.get("ColumnName") is not None:
        out["column_name"] = data["ColumnName"]
    else:
        out["column_name"] = ""
    if data.get("ColumnType") is not None:
        out["column_type"] = data["ColumnType"]
    else:
        out["column_type"] = ""
    if data.get("AnalyzedTime") is not None:
        import capo_glue.types.timestamp

        out["analyzed_time"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["AnalyzedTime"]
        )
    else:
        import datetime

        out["analyzed_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("StatisticsData") is not None:
        import capo_glue.types.column_statistics_data

        out["statistics_data"] = (
            capo_glue.types.column_statistics_data.deserialize_aws_json_1_1(
                data["StatisticsData"]
            )
        )
    else:
        raise DeserializationError("ColumnStatistics.statistics_data required")
    return out
