"""Generated from Smithy shape ``com.amazonaws.lambda#SourceAccessConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.source_access_type
    import capo_lambda.types.uri


class SourceAccessConfiguration(TypedDict, closed=True):
    type: NotRequired["capo_lambda.types.source_access_type.SourceAccessType"]
    """<p>The type of authentication protocol, VPC components, or virtual host for your event source. For example: <code>"Type":"SASL_SCRAM_512_AUTH"</code>.</p> <ul> <li> <p> <code>BASIC_AUTH</code> – (Amazon MQ) The Secrets Manager secret that stores your broker credentials.</p> </li> <li> <p> <code>BASIC_AUTH</code> – (Self-managed Apache Kafka) The Secrets Manager ARN of your secret key used for SASL/PLAIN authentication of your Apache Kafka brokers.</p> </li> <li> <p> <code>VPC_SUBNET</code> – (Self-managed Apache Kafka) The subnets associated with your VPC. Lambda connects to these subnets to fetch data from your self-managed Apache Kafka cluster.</p> </li> <li> <p> <code>VPC_SECURITY_GROUP</code> – (Self-managed Apache Kafka) The VPC security group used to manage access to your self-managed Apache Kafka brokers.</p> </li> <li> <p> <code>SASL_SCRAM_256_AUTH</code> – (Self-managed Apache Kafka) The Secrets Manager ARN of your secret key used for SASL SCRAM-256 authentication of your self-managed Apache Kafka brokers.</p> </li> <li> <p> <code>SASL_SCRAM_512_AUTH</code> – (Amazon MSK, Self-managed Apache Kafka) The Secrets Manager ARN of your secret key used for SASL SCRAM-512 authentication of your self-managed Apache Kafka brokers.</p> </li> <li> <p> <code>VIRTUAL_HOST</code> –- (RabbitMQ) The name of the virtual host in your RabbitMQ broker. Lambda uses this RabbitMQ host as the event source. This property cannot be specified in an UpdateEventSourceMapping API call.</p> </li> <li> <p> <code>CLIENT_CERTIFICATE_TLS_AUTH</code> – (Amazon MSK, self-managed Apache Kafka) The Secrets Manager ARN of your secret key containing the certificate chain (X.509 PEM), private key (PKCS#8 PEM), and private key password (optional) used for mutual TLS authentication of your MSK/Apache Kafka brokers.</p> </li> <li> <p> <code>SERVER_ROOT_CA_CERTIFICATE</code> – (Self-managed Apache Kafka) The Secrets Manager ARN of your secret key containing the root CA certificate (X.509 PEM) used for TLS encryption of your Apache Kafka brokers. </p> </li> </ul>"""
    uri: NotRequired["capo_lambda.types.uri.URI"]
    """<p>The value for your chosen configuration in <code>Type</code>. For example: <code>"URI": "arn:aws:secretsmanager:us-east-1:01234567890:secret:MyBrokerSecretName"</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceAccessConfiguration) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_lambda.types.source_access_type

        out["Type"] = capo_lambda.types.source_access_type.serialize_json(value["type"])
    if "uri" in value:
        out["URI"] = value["uri"]
    return out


def deserialize_json(data: dict) -> SourceAccessConfiguration:
    out: SourceAccessConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_lambda.types.source_access_type

        out["type"] = capo_lambda.types.source_access_type.deserialize_json(
            data["Type"]
        )
    if data.get("URI") is not None:
        out["uri"] = data["URI"]
    return out
