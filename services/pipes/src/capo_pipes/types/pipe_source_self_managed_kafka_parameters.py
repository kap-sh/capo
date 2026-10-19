"""Generated from Smithy shape ``com.amazonaws.pipes#PipeSourceSelfManagedKafkaParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.kafka_bootstrap_servers
    import capo_pipes.types.kafka_topic_name
    import capo_pipes.types.limit_max10000
    import capo_pipes.types.maximum_batching_window_in_seconds
    import capo_pipes.types.secret_manager_arn
    import capo_pipes.types.self_managed_kafka_access_configuration_credentials
    import capo_pipes.types.self_managed_kafka_access_configuration_vpc
    import capo_pipes.types.self_managed_kafka_start_position
    import capo_pipes.types.uri


class PipeSourceSelfManagedKafkaParameters(TypedDict, closed=True):
    topic_name: "capo_pipes.types.kafka_topic_name.KafkaTopicName"
    """<p>The name of the topic that the pipe will read from.</p>"""
    starting_position: NotRequired[
        "capo_pipes.types.self_managed_kafka_start_position.SelfManagedKafkaStartPosition"
    ]
    """<p>The position in a stream from which to start reading.</p>"""
    additional_bootstrap_servers: NotRequired[
        "capo_pipes.types.kafka_bootstrap_servers.KafkaBootstrapServers"
    ]
    """<p>An array of server URLs.</p>"""
    batch_size: NotRequired["capo_pipes.types.limit_max10000.LimitMax10000"]
    """<p>The maximum number of records to include in each batch.</p>"""
    maximum_batching_window_in_seconds: NotRequired[
        "capo_pipes.types.maximum_batching_window_in_seconds.MaximumBatchingWindowInSeconds"
    ]
    """<p>The maximum length of a time to wait for events.</p>"""
    consumer_group_id: NotRequired["capo_pipes.types.uri.URI"]
    """<p>The name of the destination queue to consume.</p>"""
    credentials: NotRequired[
        "capo_pipes.types.self_managed_kafka_access_configuration_credentials.SelfManagedKafkaAccessConfigurationCredentials"
    ]
    """<p>The credentials needed to access the resource.</p>"""
    server_root_ca_certificate: NotRequired[
        "capo_pipes.types.secret_manager_arn.SecretManagerArn"
    ]
    """<p>The ARN of the Secrets Manager secret used for certification.</p>"""
    vpc: NotRequired[
        "capo_pipes.types.self_managed_kafka_access_configuration_vpc.SelfManagedKafkaAccessConfigurationVpc"
    ]
    """<p>This structure specifies the VPC subnets and security groups for the stream, and whether a public IP address is to be used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipeSourceSelfManagedKafkaParameters) -> dict:
    out: dict = {}
    out["TopicName"] = value["topic_name"]
    if "starting_position" in value:
        out["StartingPosition"] = value["starting_position"]
    if "additional_bootstrap_servers" in value:
        import capo_pipes.types.kafka_bootstrap_servers

        out["AdditionalBootstrapServers"] = (
            capo_pipes.types.kafka_bootstrap_servers.serialize_json(
                value["additional_bootstrap_servers"]
            )
        )
    if "batch_size" in value:
        out["BatchSize"] = value["batch_size"]
    if "maximum_batching_window_in_seconds" in value:
        out["MaximumBatchingWindowInSeconds"] = value[
            "maximum_batching_window_in_seconds"
        ]
    if "consumer_group_id" in value:
        out["ConsumerGroupID"] = value["consumer_group_id"]
    if "credentials" in value:
        import capo_pipes.types.self_managed_kafka_access_configuration_credentials

        out["Credentials"] = (
            capo_pipes.types.self_managed_kafka_access_configuration_credentials.serialize_json(
                value["credentials"]
            )
        )
    if "server_root_ca_certificate" in value:
        out["ServerRootCaCertificate"] = value["server_root_ca_certificate"]
    if "vpc" in value:
        import capo_pipes.types.self_managed_kafka_access_configuration_vpc

        out["Vpc"] = (
            capo_pipes.types.self_managed_kafka_access_configuration_vpc.serialize_json(
                value["vpc"]
            )
        )
    return out


def deserialize_json(data: dict) -> PipeSourceSelfManagedKafkaParameters:
    out: PipeSourceSelfManagedKafkaParameters = {}  # type: ignore[typeddict-item]
    if data.get("TopicName") is not None:
        out["topic_name"] = data["TopicName"]
    else:
        out["topic_name"] = ""
    if data.get("StartingPosition") is not None:
        out["starting_position"] = data["StartingPosition"]
    if data.get("AdditionalBootstrapServers") is not None:
        import capo_pipes.types.kafka_bootstrap_servers

        out["additional_bootstrap_servers"] = (
            capo_pipes.types.kafka_bootstrap_servers.deserialize_json(
                data["AdditionalBootstrapServers"]
            )
        )
    if data.get("BatchSize") is not None:
        out["batch_size"] = data["BatchSize"]
    if data.get("MaximumBatchingWindowInSeconds") is not None:
        out["maximum_batching_window_in_seconds"] = data[
            "MaximumBatchingWindowInSeconds"
        ]
    if data.get("ConsumerGroupID") is not None:
        out["consumer_group_id"] = data["ConsumerGroupID"]
    if data.get("Credentials") is not None:
        import capo_pipes.types.self_managed_kafka_access_configuration_credentials

        out["credentials"] = (
            capo_pipes.types.self_managed_kafka_access_configuration_credentials.deserialize_json(
                data["Credentials"]
            )
        )
    if data.get("ServerRootCaCertificate") is not None:
        out["server_root_ca_certificate"] = data["ServerRootCaCertificate"]
    if data.get("Vpc") is not None:
        import capo_pipes.types.self_managed_kafka_access_configuration_vpc

        out["vpc"] = (
            capo_pipes.types.self_managed_kafka_access_configuration_vpc.deserialize_json(
                data["Vpc"]
            )
        )
    return out


def redact_sensitive(value: PipeSourceSelfManagedKafkaParameters) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "topic_name" in value:
        out["topic_name"] = "*** Sensitive Data Redacted ***"
    if "additional_bootstrap_servers" in value:
        import capo_pipes.types.kafka_bootstrap_servers

        out["additional_bootstrap_servers"] = (
            capo_pipes.types.kafka_bootstrap_servers.redact_sensitive(
                value["additional_bootstrap_servers"]
            )
        )
    if "consumer_group_id" in value:
        out["consumer_group_id"] = "*** Sensitive Data Redacted ***"
    if "vpc" in value:
        import capo_pipes.types.self_managed_kafka_access_configuration_vpc

        out["vpc"] = (
            capo_pipes.types.self_managed_kafka_access_configuration_vpc.redact_sensitive(
                value["vpc"]
            )
        )
    return out
