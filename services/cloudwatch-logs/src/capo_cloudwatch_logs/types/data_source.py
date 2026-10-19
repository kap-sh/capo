"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.data_source_name
    import capo_cloudwatch_logs.types.data_source_type


class DataSource(TypedDict, closed=True):
    name: "capo_cloudwatch_logs.types.data_source_name.DataSourceName"
    """<p>The name of the data source.</p>"""
    type: NotRequired["capo_cloudwatch_logs.types.data_source_type.DataSourceType"]
    """<p>The type of the data source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSource) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataSource:
    out: DataSource = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    return out
