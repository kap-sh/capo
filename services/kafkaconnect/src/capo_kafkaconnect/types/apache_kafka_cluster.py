"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#ApacheKafkaCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kafkaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__string
    import capo_kafkaconnect.types.vpc


class ApacheKafkaCluster(TypedDict, closed=True):
    bootstrap_servers: "capo_kafkaconnect.types.__string.__string"
    """<p>The bootstrap servers of the cluster.</p>"""
    vpc: "capo_kafkaconnect.types.vpc.Vpc"
    """<p>Details of an Amazon VPC which has network connectivity to the Apache Kafka cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApacheKafkaCluster) -> dict:
    out: dict = {}
    out["bootstrapServers"] = value["bootstrap_servers"]
    import capo_kafkaconnect.types.vpc

    out["vpc"] = capo_kafkaconnect.types.vpc.serialize_json(value["vpc"])
    return out


def deserialize_json(data: dict) -> ApacheKafkaCluster:
    out: ApacheKafkaCluster = {}  # type: ignore[typeddict-item]
    if data.get("bootstrapServers") is not None:
        out["bootstrap_servers"] = data["bootstrapServers"]
    else:
        out["bootstrap_servers"] = ""
    if data.get("vpc") is not None:
        import capo_kafkaconnect.types.vpc

        out["vpc"] = capo_kafkaconnect.types.vpc.deserialize_json(data["vpc"])
    else:
        raise DeserializationError("ApacheKafkaCluster.vpc required")
    return out
