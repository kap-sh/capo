"""Generated from Smithy shape ``com.amazonaws.kafka#EnhancedMonitoring``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies which metrics are gathered for the MSK cluster. This property has the following possible values: DEFAULT, PER_BROKER, PER_TOPIC_PER_BROKER, and PER_TOPIC_PER_PARTITION. For a list of the metrics associated with each of these levels of monitoring, see <a href="https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html">Monitoring</a>.</p>"""
EnhancedMonitoring: TypeAlias = Literal[
    "DEFAULT",
    "PER_BROKER",
    "PER_TOPIC_PER_BROKER",
    "PER_TOPIC_PER_PARTITION",
]


# --- restJson1 ser/de ---
def serialize_json(value: EnhancedMonitoring) -> str:
    return value


def deserialize_json(data: str) -> EnhancedMonitoring:
    return cast(EnhancedMonitoring, data)
