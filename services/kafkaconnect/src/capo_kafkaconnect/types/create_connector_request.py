"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#CreateConnectorRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_kafkaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__list_of_plugin
    import capo_kafkaconnect.types.__string
    import capo_kafkaconnect.types.__string_max1024
    import capo_kafkaconnect.types.__string_min1_max128
    import capo_kafkaconnect.types.capacity
    import capo_kafkaconnect.types.connector_configuration
    import capo_kafkaconnect.types.kafka_cluster
    import capo_kafkaconnect.types.kafka_cluster_client_authentication
    import capo_kafkaconnect.types.kafka_cluster_encryption_in_transit
    import capo_kafkaconnect.types.log_delivery
    import capo_kafkaconnect.types.network_type
    import capo_kafkaconnect.types.tags
    import capo_kafkaconnect.types.worker_configuration


class CreateConnectorRequest(TypedDict, closed=True):
    capacity: "capo_kafkaconnect.types.capacity.Capacity"
    """<p>Information about the capacity allocated to the connector. Exactly one of the two properties must be specified.</p>"""
    connector_configuration: (
        "capo_kafkaconnect.types.connector_configuration.ConnectorConfiguration"
    )
    """<p>A map of keys to values that represent the configuration for the connector.</p>"""
    connector_description: NotRequired[
        "capo_kafkaconnect.types.__string_max1024.__stringMax1024"
    ]
    """<p>A summary description of the connector.</p>"""
    connector_name: "capo_kafkaconnect.types.__string_min1_max128.__stringMin1Max128"
    """<p>The name of the connector.</p>"""
    kafka_cluster: "capo_kafkaconnect.types.kafka_cluster.KafkaCluster"
    """<p>Specifies which Apache Kafka cluster to connect to.</p>"""
    kafka_cluster_client_authentication: "capo_kafkaconnect.types.kafka_cluster_client_authentication.KafkaClusterClientAuthentication"
    """<p>Details of the client authentication used by the Apache Kafka cluster.</p>"""
    kafka_cluster_encryption_in_transit: "capo_kafkaconnect.types.kafka_cluster_encryption_in_transit.KafkaClusterEncryptionInTransit"
    """<p>Details of encryption in transit to the Apache Kafka cluster.</p>"""
    kafka_connect_version: "capo_kafkaconnect.types.__string.__string"
    """<p>The version of Kafka Connect. It has to be compatible with both the Apache Kafka cluster's version and the plugins.</p>"""
    log_delivery: NotRequired["capo_kafkaconnect.types.log_delivery.LogDelivery"]
    """<p>Details about log delivery.</p>"""
    network_type: NotRequired["capo_kafkaconnect.types.network_type.NetworkType"]
    """<p>The network type of the connector. It gives connectors connectivity to either IPv4 (IPV4) or IPv4 and IPv6 (DUAL) destinations. Defaults to IPV4.</p>"""
    plugins: "capo_kafkaconnect.types.__list_of_plugin.__listOfPlugin"
    """<important> <p>Amazon MSK Connect does not currently support specifying multiple plugins as a list. To use more than one plugin for your connector, you can create a single custom plugin using a ZIP file that bundles multiple plugins together.</p> </important> <p>Specifies which plugin to use for the connector. You must specify a single-element list containing one <code>customPlugin</code> object.</p>"""
    service_execution_role_arn: "capo_kafkaconnect.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the IAM role used by the connector to access the Amazon Web Services resources that it needs. The types of resources depends on the logic of the connector. For example, a connector that has Amazon S3 as a destination must have permissions that allow it to write to the S3 destination bucket.</p>"""
    worker_configuration: NotRequired[
        "capo_kafkaconnect.types.worker_configuration.WorkerConfiguration"
    ]
    """<p>Specifies which worker configuration to use with the connector.</p>"""
    tags: NotRequired["capo_kafkaconnect.types.tags.Tags"]
    """<p>The tags you want to attach to the connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectorRequest) -> dict:
    out: dict = {}
    import capo_kafkaconnect.types.capacity

    out["capacity"] = capo_kafkaconnect.types.capacity.serialize_json(value["capacity"])
    import capo_kafkaconnect.types.connector_configuration

    out["connectorConfiguration"] = (
        capo_kafkaconnect.types.connector_configuration.serialize_json(
            value["connector_configuration"]
        )
    )
    if "connector_description" in value:
        out["connectorDescription"] = value["connector_description"]
    out["connectorName"] = value["connector_name"]
    import capo_kafkaconnect.types.kafka_cluster

    out["kafkaCluster"] = capo_kafkaconnect.types.kafka_cluster.serialize_json(
        value["kafka_cluster"]
    )
    import capo_kafkaconnect.types.kafka_cluster_client_authentication

    out["kafkaClusterClientAuthentication"] = (
        capo_kafkaconnect.types.kafka_cluster_client_authentication.serialize_json(
            value["kafka_cluster_client_authentication"]
        )
    )
    import capo_kafkaconnect.types.kafka_cluster_encryption_in_transit

    out["kafkaClusterEncryptionInTransit"] = (
        capo_kafkaconnect.types.kafka_cluster_encryption_in_transit.serialize_json(
            value["kafka_cluster_encryption_in_transit"]
        )
    )
    out["kafkaConnectVersion"] = value["kafka_connect_version"]
    if "log_delivery" in value:
        import capo_kafkaconnect.types.log_delivery

        out["logDelivery"] = capo_kafkaconnect.types.log_delivery.serialize_json(
            value["log_delivery"]
        )
    if "network_type" in value:
        out["networkType"] = value["network_type"]
    import capo_kafkaconnect.types.__list_of_plugin

    out["plugins"] = capo_kafkaconnect.types.__list_of_plugin.serialize_json(
        value["plugins"]
    )
    out["serviceExecutionRoleArn"] = value["service_execution_role_arn"]
    if "worker_configuration" in value:
        import capo_kafkaconnect.types.worker_configuration

        out["workerConfiguration"] = (
            capo_kafkaconnect.types.worker_configuration.serialize_json(
                value["worker_configuration"]
            )
        )
    if "tags" in value:
        import capo_kafkaconnect.types.tags

        out["tags"] = capo_kafkaconnect.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateConnectorRequest:
    out: CreateConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("capacity") is not None:
        import capo_kafkaconnect.types.capacity

        out["capacity"] = capo_kafkaconnect.types.capacity.deserialize_json(
            data["capacity"]
        )
    else:
        raise DeserializationError("CreateConnectorRequest.capacity required")
    if data.get("connectorConfiguration") is not None:
        import capo_kafkaconnect.types.connector_configuration

        out["connector_configuration"] = (
            capo_kafkaconnect.types.connector_configuration.deserialize_json(
                data["connectorConfiguration"]
            )
        )
    else:
        out["connector_configuration"] = {}
    if data.get("connectorDescription") is not None:
        out["connector_description"] = data["connectorDescription"]
    if data.get("connectorName") is not None:
        out["connector_name"] = data["connectorName"]
    else:
        out["connector_name"] = ""
    if data.get("kafkaCluster") is not None:
        import capo_kafkaconnect.types.kafka_cluster

        out["kafka_cluster"] = capo_kafkaconnect.types.kafka_cluster.deserialize_json(
            data["kafkaCluster"]
        )
    else:
        raise DeserializationError("CreateConnectorRequest.kafka_cluster required")
    if data.get("kafkaClusterClientAuthentication") is not None:
        import capo_kafkaconnect.types.kafka_cluster_client_authentication

        out["kafka_cluster_client_authentication"] = (
            capo_kafkaconnect.types.kafka_cluster_client_authentication.deserialize_json(
                data["kafkaClusterClientAuthentication"]
            )
        )
    else:
        raise DeserializationError(
            "CreateConnectorRequest.kafka_cluster_client_authentication required"
        )
    if data.get("kafkaClusterEncryptionInTransit") is not None:
        import capo_kafkaconnect.types.kafka_cluster_encryption_in_transit

        out["kafka_cluster_encryption_in_transit"] = (
            capo_kafkaconnect.types.kafka_cluster_encryption_in_transit.deserialize_json(
                data["kafkaClusterEncryptionInTransit"]
            )
        )
    else:
        raise DeserializationError(
            "CreateConnectorRequest.kafka_cluster_encryption_in_transit required"
        )
    if data.get("kafkaConnectVersion") is not None:
        out["kafka_connect_version"] = data["kafkaConnectVersion"]
    else:
        out["kafka_connect_version"] = ""
    if data.get("logDelivery") is not None:
        import capo_kafkaconnect.types.log_delivery

        out["log_delivery"] = capo_kafkaconnect.types.log_delivery.deserialize_json(
            data["logDelivery"]
        )
    if data.get("networkType") is not None:
        out["network_type"] = data["networkType"]
    if data.get("plugins") is not None:
        import capo_kafkaconnect.types.__list_of_plugin

        out["plugins"] = capo_kafkaconnect.types.__list_of_plugin.deserialize_json(
            data["plugins"]
        )
    else:
        out["plugins"] = []
    if data.get("serviceExecutionRoleArn") is not None:
        out["service_execution_role_arn"] = data["serviceExecutionRoleArn"]
    else:
        out["service_execution_role_arn"] = ""
    if data.get("workerConfiguration") is not None:
        import capo_kafkaconnect.types.worker_configuration

        out["worker_configuration"] = (
            capo_kafkaconnect.types.worker_configuration.deserialize_json(
                data["workerConfiguration"]
            )
        )
    if data.get("tags") is not None:
        import capo_kafkaconnect.types.tags

        out["tags"] = capo_kafkaconnect.types.tags.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: CreateConnectorRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "connector_configuration" in value:
        out["connector_configuration"] = "*** Sensitive Data Redacted ***"
    return out
