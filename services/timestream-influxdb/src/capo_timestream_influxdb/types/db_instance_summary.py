"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DbInstanceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.allocated_storage
    import capo_timestream_influxdb.types.arn
    import capo_timestream_influxdb.types.db_instance_id
    import capo_timestream_influxdb.types.db_instance_name
    import capo_timestream_influxdb.types.db_instance_type
    import capo_timestream_influxdb.types.db_storage_type
    import capo_timestream_influxdb.types.deployment_type
    import capo_timestream_influxdb.types.network_type
    import capo_timestream_influxdb.types.port
    import capo_timestream_influxdb.types.status


class DbInstanceSummary(TypedDict, closed=True):
    id: "capo_timestream_influxdb.types.db_instance_id.DbInstanceId"
    """<p>The service-generated unique identifier of the DB instance.</p>"""
    name: "capo_timestream_influxdb.types.db_instance_name.DbInstanceName"
    """<p>This customer-supplied name uniquely identifies the DB instance when interacting with the Amazon Timestream for InfluxDB API and CLI commands.</p>"""
    arn: "capo_timestream_influxdb.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the DB instance.</p>"""
    status: NotRequired["capo_timestream_influxdb.types.status.Status"]
    """<p>The status of the DB instance.</p>"""
    endpoint: NotRequired["str"]
    """<p>The endpoint used to connect to InfluxDB. The default InfluxDB port is 8086.</p>"""
    port: NotRequired["capo_timestream_influxdb.types.port.Port"]
    """<p>The port number on which InfluxDB accepts connections.</p>"""
    network_type: NotRequired["capo_timestream_influxdb.types.network_type.NetworkType"]
    """<p>Specifies whether the networkType of the Timestream for InfluxDB instance is IPV4, which can communicate over IPv4 protocol only, or DUAL, which can communicate over both IPv4 and IPv6 protocols.</p>"""
    db_instance_type: NotRequired[
        "capo_timestream_influxdb.types.db_instance_type.DbInstanceType"
    ]
    """<p>The Timestream for InfluxDB instance type to run InfluxDB on.</p>"""
    db_storage_type: NotRequired[
        "capo_timestream_influxdb.types.db_storage_type.DbStorageType"
    ]
    """<p>The storage type for your DB instance.</p>"""
    allocated_storage: NotRequired[
        "capo_timestream_influxdb.types.allocated_storage.AllocatedStorage"
    ]
    """<p>The amount of storage to allocate for your DbStorageType in GiB (gibibytes).</p>"""
    deployment_type: NotRequired[
        "capo_timestream_influxdb.types.deployment_type.DeploymentType"
    ]
    """<p>Single-Instance or with a MultiAZ Standby for High availability.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbInstanceSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    if "status" in value:
        import capo_timestream_influxdb.types.status

        out["status"] = capo_timestream_influxdb.types.status.serialize_aws_json_1_0(
            value["status"]
        )
    if "endpoint" in value:
        out["endpoint"] = value["endpoint"]
    if "port" in value:
        out["port"] = value["port"]
    if "network_type" in value:
        import capo_timestream_influxdb.types.network_type

        out["networkType"] = (
            capo_timestream_influxdb.types.network_type.serialize_aws_json_1_0(
                value["network_type"]
            )
        )
    if "db_instance_type" in value:
        import capo_timestream_influxdb.types.db_instance_type

        out["dbInstanceType"] = (
            capo_timestream_influxdb.types.db_instance_type.serialize_aws_json_1_0(
                value["db_instance_type"]
            )
        )
    if "db_storage_type" in value:
        import capo_timestream_influxdb.types.db_storage_type

        out["dbStorageType"] = (
            capo_timestream_influxdb.types.db_storage_type.serialize_aws_json_1_0(
                value["db_storage_type"]
            )
        )
    if "allocated_storage" in value:
        out["allocatedStorage"] = value["allocated_storage"]
    if "deployment_type" in value:
        import capo_timestream_influxdb.types.deployment_type

        out["deploymentType"] = (
            capo_timestream_influxdb.types.deployment_type.serialize_aws_json_1_0(
                value["deployment_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DbInstanceSummary:
    out: DbInstanceSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("status") is not None:
        import capo_timestream_influxdb.types.status

        out["status"] = capo_timestream_influxdb.types.status.deserialize_aws_json_1_0(
            data["status"]
        )
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    if data.get("port") is not None:
        out["port"] = data["port"]
    if data.get("networkType") is not None:
        import capo_timestream_influxdb.types.network_type

        out["network_type"] = (
            capo_timestream_influxdb.types.network_type.deserialize_aws_json_1_0(
                data["networkType"]
            )
        )
    if data.get("dbInstanceType") is not None:
        import capo_timestream_influxdb.types.db_instance_type

        out["db_instance_type"] = (
            capo_timestream_influxdb.types.db_instance_type.deserialize_aws_json_1_0(
                data["dbInstanceType"]
            )
        )
    if data.get("dbStorageType") is not None:
        import capo_timestream_influxdb.types.db_storage_type

        out["db_storage_type"] = (
            capo_timestream_influxdb.types.db_storage_type.deserialize_aws_json_1_0(
                data["dbStorageType"]
            )
        )
    if data.get("allocatedStorage") is not None:
        out["allocated_storage"] = data["allocatedStorage"]
    if data.get("deploymentType") is not None:
        import capo_timestream_influxdb.types.deployment_type

        out["deployment_type"] = (
            capo_timestream_influxdb.types.deployment_type.deserialize_aws_json_1_0(
                data["deploymentType"]
            )
        )
    return out
