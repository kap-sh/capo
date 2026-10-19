"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#KafkaClusterEncryptionInTransit``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.kafka_cluster_encryption_in_transit_type


class KafkaClusterEncryptionInTransit(TypedDict, closed=True):
    encryption_type: "capo_kafkaconnect.types.kafka_cluster_encryption_in_transit_type.KafkaClusterEncryptionInTransitType"
    """<p>The type of encryption in transit to the Apache Kafka cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaClusterEncryptionInTransit) -> dict:
    out: dict = {}
    out["encryptionType"] = value["encryption_type"]
    return out


def deserialize_json(data: dict) -> KafkaClusterEncryptionInTransit:
    out: KafkaClusterEncryptionInTransit = {}  # type: ignore[typeddict-item]
    if data.get("encryptionType") is not None:
        out["encryption_type"] = data["encryptionType"]
    else:
        out["encryption_type"] = ""
    return out
