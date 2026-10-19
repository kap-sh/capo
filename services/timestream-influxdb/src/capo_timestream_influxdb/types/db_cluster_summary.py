"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DbClusterSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.allocated_storage
    import capo_timestream_influxdb.types.arn
    import capo_timestream_influxdb.types.cluster_deployment_type
    import capo_timestream_influxdb.types.cluster_status
    import capo_timestream_influxdb.types.db_cluster_id
    import capo_timestream_influxdb.types.db_cluster_name
    import capo_timestream_influxdb.types.db_instance_type
    import capo_timestream_influxdb.types.db_storage_type
    import capo_timestream_influxdb.types.engine_type
    import capo_timestream_influxdb.types.network_type
    import capo_timestream_influxdb.types.port


class DbClusterSummary(TypedDict, closed=True):
    id: "capo_timestream_influxdb.types.db_cluster_id.DbClusterId"
    """<p>Service-generated unique identifier of the DB cluster to retrieve.</p>"""
    name: "capo_timestream_influxdb.types.db_cluster_name.DbClusterName"
    """<p>Customer supplied name of the Timestream for InfluxDB cluster.</p>"""
    arn: "capo_timestream_influxdb.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the DB cluster.</p>"""
    status: NotRequired["capo_timestream_influxdb.types.cluster_status.ClusterStatus"]
    """<p>The status of the DB cluster.</p>"""
    endpoint: NotRequired["str"]
    """<p>The endpoint used to connect to the Timestream for InfluxDB cluster for write and read operations.</p>"""
    reader_endpoint: NotRequired["str"]
    """<p>The endpoint used to connect to the Timestream for InfluxDB cluster for read-only operations.</p>"""
    port: NotRequired["capo_timestream_influxdb.types.port.Port"]
    """<p>The port number on which InfluxDB accepts connections.</p>"""
    deployment_type: NotRequired[
        "capo_timestream_influxdb.types.cluster_deployment_type.ClusterDeploymentType"
    ]
    """<p>Deployment type of the DB cluster</p>"""
    db_instance_type: NotRequired[
        "capo_timestream_influxdb.types.db_instance_type.DbInstanceType"
    ]
    """<p>The Timestream for InfluxDB DB instance type that InfluxDB runs on.</p>"""
    network_type: NotRequired["capo_timestream_influxdb.types.network_type.NetworkType"]
    """<p>Specifies whether the network type of the Timestream for InfluxDB Cluster is IPv4, which can communicate over IPv4 protocol only, or DUAL, which can communicate over both IPv4 and IPv6 protocols.</p>"""
    db_storage_type: NotRequired[
        "capo_timestream_influxdb.types.db_storage_type.DbStorageType"
    ]
    """<p>The Timestream for InfluxDB DB storage type that InfluxDB stores data on.</p>"""
    allocated_storage: NotRequired[
        "capo_timestream_influxdb.types.allocated_storage.AllocatedStorage"
    ]
    """<p>The amount of storage allocated for your DB storage type (in gibibytes).</p>"""
    engine_type: NotRequired["capo_timestream_influxdb.types.engine_type.EngineType"]
    """<p>The engine type of your DB cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbClusterSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    if "status" in value:
        import capo_timestream_influxdb.types.cluster_status

        out["status"] = (
            capo_timestream_influxdb.types.cluster_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "endpoint" in value:
        out["endpoint"] = value["endpoint"]
    if "reader_endpoint" in value:
        out["readerEndpoint"] = value["reader_endpoint"]
    if "port" in value:
        out["port"] = value["port"]
    if "deployment_type" in value:
        import capo_timestream_influxdb.types.cluster_deployment_type

        out["deploymentType"] = (
            capo_timestream_influxdb.types.cluster_deployment_type.serialize_aws_json_1_0(
                value["deployment_type"]
            )
        )
    if "db_instance_type" in value:
        import capo_timestream_influxdb.types.db_instance_type

        out["dbInstanceType"] = (
            capo_timestream_influxdb.types.db_instance_type.serialize_aws_json_1_0(
                value["db_instance_type"]
            )
        )
    if "network_type" in value:
        import capo_timestream_influxdb.types.network_type

        out["networkType"] = (
            capo_timestream_influxdb.types.network_type.serialize_aws_json_1_0(
                value["network_type"]
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
    if "engine_type" in value:
        import capo_timestream_influxdb.types.engine_type

        out["engineType"] = (
            capo_timestream_influxdb.types.engine_type.serialize_aws_json_1_0(
                value["engine_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DbClusterSummary:
    out: DbClusterSummary = {}  # type: ignore[typeddict-item]
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
        import capo_timestream_influxdb.types.cluster_status

        out["status"] = (
            capo_timestream_influxdb.types.cluster_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    if data.get("readerEndpoint") is not None:
        out["reader_endpoint"] = data["readerEndpoint"]
    if data.get("port") is not None:
        out["port"] = data["port"]
    if data.get("deploymentType") is not None:
        import capo_timestream_influxdb.types.cluster_deployment_type

        out["deployment_type"] = (
            capo_timestream_influxdb.types.cluster_deployment_type.deserialize_aws_json_1_0(
                data["deploymentType"]
            )
        )
    if data.get("dbInstanceType") is not None:
        import capo_timestream_influxdb.types.db_instance_type

        out["db_instance_type"] = (
            capo_timestream_influxdb.types.db_instance_type.deserialize_aws_json_1_0(
                data["dbInstanceType"]
            )
        )
    if data.get("networkType") is not None:
        import capo_timestream_influxdb.types.network_type

        out["network_type"] = (
            capo_timestream_influxdb.types.network_type.deserialize_aws_json_1_0(
                data["networkType"]
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
    if data.get("engineType") is not None:
        import capo_timestream_influxdb.types.engine_type

        out["engine_type"] = (
            capo_timestream_influxdb.types.engine_type.deserialize_aws_json_1_0(
                data["engineType"]
            )
        )
    return out
