"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#KafkaClusterClientAuthentication``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.kafka_cluster_client_authentication_type


class KafkaClusterClientAuthentication(TypedDict, closed=True):
    authentication_type: "capo_kafkaconnect.types.kafka_cluster_client_authentication_type.KafkaClusterClientAuthenticationType"
    """<p>The type of client authentication used to connect to the Apache Kafka cluster. Value NONE means that no client authentication is used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaClusterClientAuthentication) -> dict:
    out: dict = {}
    out["authenticationType"] = value["authentication_type"]
    return out


def deserialize_json(data: dict) -> KafkaClusterClientAuthentication:
    out: KafkaClusterClientAuthentication = {}  # type: ignore[typeddict-item]
    if data.get("authenticationType") is not None:
        out["authentication_type"] = data["authenticationType"]
    else:
        out["authentication_type"] = ""
    return out
