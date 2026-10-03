"""Generated from Smithy shape ``com.amazonaws.kafka#ClusterInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__integer
    import capo_kafka.types.__map_of__string
    import capo_kafka.types.__string
    import capo_kafka.types.__timestamp_iso8601
    import capo_kafka.types.broker_node_group_info
    import capo_kafka.types.broker_software_info
    import capo_kafka.types.client_authentication
    import capo_kafka.types.cluster_state
    import capo_kafka.types.customer_action_status
    import capo_kafka.types.encryption_info
    import capo_kafka.types.enhanced_monitoring
    import capo_kafka.types.logging_info
    import capo_kafka.types.open_monitoring
    import capo_kafka.types.rebalancing
    import capo_kafka.types.state_info
    import capo_kafka.types.storage_mode


class ClusterInfo(TypedDict, closed=True):
    active_operation_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>Arn of active cluster operation.</p>"""
    broker_node_group_info: NotRequired[
        "capo_kafka.types.broker_node_group_info.BrokerNodeGroupInfo"
    ]
    """<p>Information about the broker nodes.</p>"""
    rebalancing: NotRequired["capo_kafka.types.rebalancing.Rebalancing"]
    """<p>Contains information about intelligent rebalancing for new MSK Provisioned clusters with Express brokers. By default, intelligent rebalancing status is ACTIVE.</p>"""
    client_authentication: NotRequired[
        "capo_kafka.types.client_authentication.ClientAuthentication"
    ]
    """<p>Includes all client authentication information.</p>"""
    cluster_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>"""
    cluster_name: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The name of the cluster.</p>"""
    creation_time: NotRequired[
        "capo_kafka.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time when the cluster was created.</p>"""
    current_broker_software_info: NotRequired[
        "capo_kafka.types.broker_software_info.BrokerSoftwareInfo"
    ]
    """<p>Information about the version of software currently deployed on the Apache Kafka brokers in the cluster.</p>"""
    current_version: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The current version of the MSK cluster.</p>"""
    encryption_info: NotRequired["capo_kafka.types.encryption_info.EncryptionInfo"]
    """<p>Includes all encryption-related information.</p>"""
    enhanced_monitoring: NotRequired[
        "capo_kafka.types.enhanced_monitoring.EnhancedMonitoring"
    ]
    """<p>Specifies which metrics are gathered for the MSK cluster. This property has the following possible values: DEFAULT, PER_BROKER, PER_TOPIC_PER_BROKER, and PER_TOPIC_PER_PARTITION. For a list of the metrics associated with each of these levels of monitoring, see <a href="https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html">Monitoring</a>.</p>"""
    open_monitoring: NotRequired["capo_kafka.types.open_monitoring.OpenMonitoring"]
    """<p>Settings for open monitoring using Prometheus.</p>"""
    logging_info: NotRequired["capo_kafka.types.logging_info.LoggingInfo"]
    number_of_broker_nodes: NotRequired["capo_kafka.types.__integer.__integer"]
    """<p>The number of broker nodes in the cluster.</p>"""
    state: NotRequired["capo_kafka.types.cluster_state.ClusterState"]
    """<p>The state of the cluster. The possible states are ACTIVE, CREATING, DELETING, FAILED, HEALING, MAINTENANCE, REBOOTING_BROKER, and UPDATING.</p>"""
    state_info: NotRequired["capo_kafka.types.state_info.StateInfo"]
    tags: NotRequired["capo_kafka.types.__map_of__string.__mapOf__string"]
    """<p>Tags attached to the cluster.</p>"""
    zookeeper_connect_string: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The connection string to use to connect to the Apache ZooKeeper cluster.</p>"""
    zookeeper_connect_string_tls: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The connection string to use to connect to zookeeper cluster on Tls port.</p>"""
    storage_mode: NotRequired["capo_kafka.types.storage_mode.StorageMode"]
    """<p>This controls storage mode for supported storage tiers.</p>"""
    customer_action_status: NotRequired[
        "capo_kafka.types.customer_action_status.CustomerActionStatus"
    ]
    """<p>Determines if there is an action required from the customer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterInfo) -> dict:
    out: dict = {}
    if "active_operation_arn" in value:
        out["activeOperationArn"] = value["active_operation_arn"]
    if "broker_node_group_info" in value:
        import capo_kafka.types.broker_node_group_info

        out["brokerNodeGroupInfo"] = (
            capo_kafka.types.broker_node_group_info.serialize_json(
                value["broker_node_group_info"]
            )
        )
    if "rebalancing" in value:
        import capo_kafka.types.rebalancing

        out["rebalancing"] = capo_kafka.types.rebalancing.serialize_json(
            value["rebalancing"]
        )
    if "client_authentication" in value:
        import capo_kafka.types.client_authentication

        out["clientAuthentication"] = (
            capo_kafka.types.client_authentication.serialize_json(
                value["client_authentication"]
            )
        )
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "creation_time" in value:
        import capo_kafka.types.__timestamp_iso8601

        out["creationTime"] = capo_kafka.types.__timestamp_iso8601.serialize_json(
            value["creation_time"]
        )
    if "current_broker_software_info" in value:
        import capo_kafka.types.broker_software_info

        out["currentBrokerSoftwareInfo"] = (
            capo_kafka.types.broker_software_info.serialize_json(
                value["current_broker_software_info"]
            )
        )
    if "current_version" in value:
        out["currentVersion"] = value["current_version"]
    if "encryption_info" in value:
        import capo_kafka.types.encryption_info

        out["encryptionInfo"] = capo_kafka.types.encryption_info.serialize_json(
            value["encryption_info"]
        )
    if "enhanced_monitoring" in value:
        import capo_kafka.types.enhanced_monitoring

        out["enhancedMonitoring"] = capo_kafka.types.enhanced_monitoring.serialize_json(
            value["enhanced_monitoring"]
        )
    if "open_monitoring" in value:
        import capo_kafka.types.open_monitoring

        out["openMonitoring"] = capo_kafka.types.open_monitoring.serialize_json(
            value["open_monitoring"]
        )
    if "logging_info" in value:
        import capo_kafka.types.logging_info

        out["loggingInfo"] = capo_kafka.types.logging_info.serialize_json(
            value["logging_info"]
        )
    if "number_of_broker_nodes" in value:
        out["numberOfBrokerNodes"] = value["number_of_broker_nodes"]
    if "state" in value:
        import capo_kafka.types.cluster_state

        out["state"] = capo_kafka.types.cluster_state.serialize_json(value["state"])
    if "state_info" in value:
        import capo_kafka.types.state_info

        out["stateInfo"] = capo_kafka.types.state_info.serialize_json(
            value["state_info"]
        )
    if "tags" in value:
        import capo_kafka.types.__map_of__string

        out["tags"] = capo_kafka.types.__map_of__string.serialize_json(value["tags"])
    if "zookeeper_connect_string" in value:
        out["zookeeperConnectString"] = value["zookeeper_connect_string"]
    if "zookeeper_connect_string_tls" in value:
        out["zookeeperConnectStringTls"] = value["zookeeper_connect_string_tls"]
    if "storage_mode" in value:
        import capo_kafka.types.storage_mode

        out["storageMode"] = capo_kafka.types.storage_mode.serialize_json(
            value["storage_mode"]
        )
    if "customer_action_status" in value:
        import capo_kafka.types.customer_action_status

        out["customerActionStatus"] = (
            capo_kafka.types.customer_action_status.serialize_json(
                value["customer_action_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> ClusterInfo:
    out: ClusterInfo = {}  # type: ignore[typeddict-item]
    if data.get("activeOperationArn") is not None:
        out["active_operation_arn"] = data["activeOperationArn"]
    if data.get("brokerNodeGroupInfo") is not None:
        import capo_kafka.types.broker_node_group_info

        out["broker_node_group_info"] = (
            capo_kafka.types.broker_node_group_info.deserialize_json(
                data["brokerNodeGroupInfo"]
            )
        )
    if data.get("rebalancing") is not None:
        import capo_kafka.types.rebalancing

        out["rebalancing"] = capo_kafka.types.rebalancing.deserialize_json(
            data["rebalancing"]
        )
    if data.get("clientAuthentication") is not None:
        import capo_kafka.types.client_authentication

        out["client_authentication"] = (
            capo_kafka.types.client_authentication.deserialize_json(
                data["clientAuthentication"]
            )
        )
    if data.get("clusterArn") is not None:
        out["cluster_arn"] = data["clusterArn"]
    if data.get("clusterName") is not None:
        out["cluster_name"] = data["clusterName"]
    if data.get("creationTime") is not None:
        import capo_kafka.types.__timestamp_iso8601

        out["creation_time"] = capo_kafka.types.__timestamp_iso8601.deserialize_json(
            data["creationTime"]
        )
    if data.get("currentBrokerSoftwareInfo") is not None:
        import capo_kafka.types.broker_software_info

        out["current_broker_software_info"] = (
            capo_kafka.types.broker_software_info.deserialize_json(
                data["currentBrokerSoftwareInfo"]
            )
        )
    if data.get("currentVersion") is not None:
        out["current_version"] = data["currentVersion"]
    if data.get("encryptionInfo") is not None:
        import capo_kafka.types.encryption_info

        out["encryption_info"] = capo_kafka.types.encryption_info.deserialize_json(
            data["encryptionInfo"]
        )
    if data.get("enhancedMonitoring") is not None:
        import capo_kafka.types.enhanced_monitoring

        out["enhanced_monitoring"] = (
            capo_kafka.types.enhanced_monitoring.deserialize_json(
                data["enhancedMonitoring"]
            )
        )
    if data.get("openMonitoring") is not None:
        import capo_kafka.types.open_monitoring

        out["open_monitoring"] = capo_kafka.types.open_monitoring.deserialize_json(
            data["openMonitoring"]
        )
    if data.get("loggingInfo") is not None:
        import capo_kafka.types.logging_info

        out["logging_info"] = capo_kafka.types.logging_info.deserialize_json(
            data["loggingInfo"]
        )
    if data.get("numberOfBrokerNodes") is not None:
        out["number_of_broker_nodes"] = data["numberOfBrokerNodes"]
    if data.get("state") is not None:
        import capo_kafka.types.cluster_state

        out["state"] = capo_kafka.types.cluster_state.deserialize_json(data["state"])
    if data.get("stateInfo") is not None:
        import capo_kafka.types.state_info

        out["state_info"] = capo_kafka.types.state_info.deserialize_json(
            data["stateInfo"]
        )
    if data.get("tags") is not None:
        import capo_kafka.types.__map_of__string

        out["tags"] = capo_kafka.types.__map_of__string.deserialize_json(data["tags"])
    if data.get("zookeeperConnectString") is not None:
        out["zookeeper_connect_string"] = data["zookeeperConnectString"]
    if data.get("zookeeperConnectStringTls") is not None:
        out["zookeeper_connect_string_tls"] = data["zookeeperConnectStringTls"]
    if data.get("storageMode") is not None:
        import capo_kafka.types.storage_mode

        out["storage_mode"] = capo_kafka.types.storage_mode.deserialize_json(
            data["storageMode"]
        )
    if data.get("customerActionStatus") is not None:
        import capo_kafka.types.customer_action_status

        out["customer_action_status"] = (
            capo_kafka.types.customer_action_status.deserialize_json(
                data["customerActionStatus"]
            )
        )
    return out
