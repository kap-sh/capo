"""Generated from Smithy shape ``com.amazonaws.pipes#UpdatePipeSourceSelfManagedKafkaParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.limit_max10000
    import capo_pipes.types.maximum_batching_window_in_seconds
    import capo_pipes.types.secret_manager_arn
    import capo_pipes.types.self_managed_kafka_access_configuration_credentials
    import capo_pipes.types.self_managed_kafka_access_configuration_vpc


class UpdatePipeSourceSelfManagedKafkaParameters(TypedDict, closed=True):
    batch_size: NotRequired["capo_pipes.types.limit_max10000.LimitMax10000"]
    """<p>The maximum number of records to include in each batch.</p>"""
    maximum_batching_window_in_seconds: NotRequired[
        "capo_pipes.types.maximum_batching_window_in_seconds.MaximumBatchingWindowInSeconds"
    ]
    """<p>The maximum length of a time to wait for events.</p>"""
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
def serialize_json(value: UpdatePipeSourceSelfManagedKafkaParameters) -> dict:
    out: dict = {}
    if "batch_size" in value:
        out["BatchSize"] = value["batch_size"]
    if "maximum_batching_window_in_seconds" in value:
        out["MaximumBatchingWindowInSeconds"] = value[
            "maximum_batching_window_in_seconds"
        ]
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


def deserialize_json(data: dict) -> UpdatePipeSourceSelfManagedKafkaParameters:
    out: UpdatePipeSourceSelfManagedKafkaParameters = {}  # type: ignore[typeddict-item]
    if data.get("BatchSize") is not None:
        out["batch_size"] = data["BatchSize"]
    if data.get("MaximumBatchingWindowInSeconds") is not None:
        out["maximum_batching_window_in_seconds"] = data[
            "MaximumBatchingWindowInSeconds"
        ]
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


def redact_sensitive(
    value: UpdatePipeSourceSelfManagedKafkaParameters,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "vpc" in value:
        import capo_pipes.types.self_managed_kafka_access_configuration_vpc

        out["vpc"] = (
            capo_pipes.types.self_managed_kafka_access_configuration_vpc.redact_sensitive(
                value["vpc"]
            )
        )
    return out
