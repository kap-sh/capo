"""Generated from Smithy shape ``com.amazonaws.lambda#KafkaSchemaRegistryAccessConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.arn
    import capo_lambda.types.kafka_schema_registry_auth_type


class KafkaSchemaRegistryAccessConfig(TypedDict, closed=True):
    type: NotRequired[
        "capo_lambda.types.kafka_schema_registry_auth_type.KafkaSchemaRegistryAuthType"
    ]
    """<p> The type of authentication Lambda uses to access your schema registry. </p> <ul> <li> <p> <code>BASIC_AUTH</code> – The Secrets Manager ARN of your secret key used for basic authentication with your Confluent schema registry.</p> </li> <li> <p> <code>CLIENT_CERTIFICATE_TLS_AUTH</code> – The Secrets Manager ARN of your secret key containing the certificate chain (X.509 PEM), private key (PKCS#8 PEM), and private key password (optional) used for mutual TLS authentication with your Confluent schema registry.</p> </li> <li> <p> <code>SERVER_ROOT_CA_CERTIFICATE</code> – The Secrets Manager ARN of your secret key containing the root CA certificate (X.509 PEM) used for TLS encryption with your Confluent schema registry.</p> </li> <li> <p> <code>OAUTHBEARER_AUTH</code> – The Secrets Manager ARN of your secret key containing the OAuth 2.0 credentials that Lambda uses to acquire an access token for your Confluent schema registry. For the contents of the secret, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/kafka-cluster-auth.html#smaa-auth-oauth-secret">Configuring the OAuth secret</a>.</p> </li> </ul>"""
    uri: NotRequired["capo_lambda.types.arn.Arn"]
    """<p> The URI of the secret (Secrets Manager secret ARN) to authenticate with your schema registry. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaSchemaRegistryAccessConfig) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_lambda.types.kafka_schema_registry_auth_type

        out["Type"] = capo_lambda.types.kafka_schema_registry_auth_type.serialize_json(
            value["type"]
        )
    if "uri" in value:
        out["URI"] = value["uri"]
    return out


def deserialize_json(data: dict) -> KafkaSchemaRegistryAccessConfig:
    out: KafkaSchemaRegistryAccessConfig = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_lambda.types.kafka_schema_registry_auth_type

        out["type"] = (
            capo_lambda.types.kafka_schema_registry_auth_type.deserialize_json(
                data["Type"]
            )
        )
    if data.get("URI") is not None:
        out["uri"] = data["URI"]
    return out
