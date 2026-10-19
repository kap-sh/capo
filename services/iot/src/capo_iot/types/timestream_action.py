"""Generated from Smithy shape ``com.amazonaws.iot#TimestreamAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.aws_arn
    import capo_iot.types.timestream_database_name
    import capo_iot.types.timestream_dimension_list
    import capo_iot.types.timestream_table_name
    import capo_iot.types.timestream_timestamp


class TimestreamAction(TypedDict, closed=True):
    role_arn: "capo_iot.types.aws_arn.AwsArn"
    """<p>The ARN of the role that grants permission to write to the Amazon Timestream database table.</p>"""
    database_name: "capo_iot.types.timestream_database_name.TimestreamDatabaseName"
    """<p>The name of an Amazon Timestream database.</p>"""
    table_name: "capo_iot.types.timestream_table_name.TimestreamTableName"
    """<p>The name of the database table into which to write the measure records.</p>"""
    dimensions: "capo_iot.types.timestream_dimension_list.TimestreamDimensionList"
    """<p>Metadata attributes of the time series that are written in each measure record.</p>"""
    timestamp: NotRequired["capo_iot.types.timestream_timestamp.TimestreamTimestamp"]
    """<p>Specifies an application-defined value to replace the default value assigned to the Timestream record's timestamp in the <code>time</code> column.</p> <p>You can use this property to specify the value and the precision of the Timestream record's timestamp. You can specify a value from the message payload or a value computed by a substitution template.</p> <p>If omitted, the topic rule action assigns the timestamp, in milliseconds, at the time it processed the rule. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimestreamAction) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    out["databaseName"] = value["database_name"]
    out["tableName"] = value["table_name"]
    import capo_iot.types.timestream_dimension_list

    out["dimensions"] = capo_iot.types.timestream_dimension_list.serialize_json(
        value["dimensions"]
    )
    if "timestamp" in value:
        import capo_iot.types.timestream_timestamp

        out["timestamp"] = capo_iot.types.timestream_timestamp.serialize_json(
            value["timestamp"]
        )
    return out


def deserialize_json(data: dict) -> TimestreamAction:
    out: TimestreamAction = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("databaseName") is not None:
        out["database_name"] = data["databaseName"]
    else:
        out["database_name"] = ""
    if data.get("tableName") is not None:
        out["table_name"] = data["tableName"]
    else:
        out["table_name"] = ""
    if data.get("dimensions") is not None:
        import capo_iot.types.timestream_dimension_list

        out["dimensions"] = capo_iot.types.timestream_dimension_list.deserialize_json(
            data["dimensions"]
        )
    else:
        out["dimensions"] = []
    if data.get("timestamp") is not None:
        import capo_iot.types.timestream_timestamp

        out["timestamp"] = capo_iot.types.timestream_timestamp.deserialize_json(
            data["timestamp"]
        )
    return out
