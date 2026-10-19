"""Generated from Smithy shape ``com.amazonaws.iot#InfluxDBAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.aws_arn
    import capo_iot.types.influx_db_batch_config
    import capo_iot.types.influx_db_database_name
    import capo_iot.types.influx_db_organization
    import capo_iot.types.influx_db_table_name
    import capo_iot.types.influx_db_tag_map
    import capo_iot.types.influx_db_timestamp_unit


class InfluxDBAction(TypedDict, closed=True):
    destination_arn: "capo_iot.types.aws_arn.AwsArn"
    """<p>The ARN of the InfluxDB topic rule destination that identifies the InfluxDB instance to write to.</p>"""
    role_arn: "capo_iot.types.aws_arn.AwsArn"
    """<p>The ARN of the role that grants permission to retrieve the InfluxDB API token from Amazon Web Services Secrets Manager.</p>"""
    database_name: "capo_iot.types.influx_db_database_name.InfluxDBDatabaseName"
    """<p>The name of the InfluxDB database to write to. In InfluxDB 2, this is the name of the bucket.</p>"""
    table_name: "capo_iot.types.influx_db_table_name.InfluxDBTableName"
    """<p>The name of the table to write the data point to. This is the measurement name of the InfluxDB line protocol record.</p> <p>Accepts substitution templates.</p>"""
    organization: NotRequired[
        "capo_iot.types.influx_db_organization.InfluxDBOrganization"
    ]
    """<p>The name of the InfluxDB organization that owns the database.</p> <p>A write to an InfluxDB 2 instance fails if this value isn't set. This value isn't used when the destination is an InfluxDB 3 instance.</p>"""
    tags: NotRequired["capo_iot.types.influx_db_tag_map.InfluxDBTagMap"]
    """<p>The set of tags to write with each data point. Tags are the indexed metadata of an InfluxDB data point.</p> <p>Tag names and tag values accept substitution templates. A tag name can't use the <code>@{...}</code> per-element form. A tag name must resolve to the same value for every element of an array payload.</p>"""
    timestamp_unit: NotRequired[
        "capo_iot.types.influx_db_timestamp_unit.InfluxDBTimestampUnit"
    ]
    """<p>The precision of the timestamp written with each data point. Valid values are <code>s</code> (seconds), <code>ms</code> (milliseconds), <code>us</code> (microseconds), and <code>ns</code> (nanoseconds).</p> <p>If omitted, the topic rule action uses <code>ms</code>.</p>"""
    batch_config: NotRequired[
        "capo_iot.types.influx_db_batch_config.InfluxDBBatchConfig"
    ]
    """<p>The batching configuration for the action. When present, IoT collects data points from multiple messages and writes them to InfluxDB in a single request.</p> <p>If omitted, each message is written to InfluxDB in its own request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InfluxDBAction) -> dict:
    out: dict = {}
    out["destinationArn"] = value["destination_arn"]
    out["roleArn"] = value["role_arn"]
    out["databaseName"] = value["database_name"]
    out["tableName"] = value["table_name"]
    if "organization" in value:
        out["organization"] = value["organization"]
    if "tags" in value:
        import capo_iot.types.influx_db_tag_map

        out["tags"] = capo_iot.types.influx_db_tag_map.serialize_json(value["tags"])
    if "timestamp_unit" in value:
        import capo_iot.types.influx_db_timestamp_unit

        out["timestampUnit"] = capo_iot.types.influx_db_timestamp_unit.serialize_json(
            value["timestamp_unit"]
        )
    if "batch_config" in value:
        import capo_iot.types.influx_db_batch_config

        out["batchConfig"] = capo_iot.types.influx_db_batch_config.serialize_json(
            value["batch_config"]
        )
    return out


def deserialize_json(data: dict) -> InfluxDBAction:
    out: InfluxDBAction = {}  # type: ignore[typeddict-item]
    if data.get("destinationArn") is not None:
        out["destination_arn"] = data["destinationArn"]
    else:
        out["destination_arn"] = ""
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
    if data.get("organization") is not None:
        out["organization"] = data["organization"]
    if data.get("tags") is not None:
        import capo_iot.types.influx_db_tag_map

        out["tags"] = capo_iot.types.influx_db_tag_map.deserialize_json(data["tags"])
    if data.get("timestampUnit") is not None:
        import capo_iot.types.influx_db_timestamp_unit

        out["timestamp_unit"] = (
            capo_iot.types.influx_db_timestamp_unit.deserialize_json(
                data["timestampUnit"]
            )
        )
    if data.get("batchConfig") is not None:
        import capo_iot.types.influx_db_batch_config

        out["batch_config"] = capo_iot.types.influx_db_batch_config.deserialize_json(
            data["batchConfig"]
        )
    return out
