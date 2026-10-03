"""Generated from Smithy shape ``com.amazonaws.elasticache#PendingLogDeliveryConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.destination_details
    import capo_elasticache.types.destination_type
    import capo_elasticache.types.log_format
    import capo_elasticache.types.log_type


class PendingLogDeliveryConfiguration(TypedDict, closed=True):
    log_type: NotRequired["capo_elasticache.types.log_type.LogType"]
    """<p>Refers to <a href="https://redis.io/commands/slowlog">slow-log</a> or engine-log..</p>"""
    destination_type: NotRequired[
        "capo_elasticache.types.destination_type.DestinationType"
    ]
    """<p>Returns the destination type, either CloudWatch Logs or Kinesis Data Firehose.</p>"""
    destination_details: NotRequired[
        "capo_elasticache.types.destination_details.DestinationDetails"
    ]
    """<p>Configuration details of either a CloudWatch Logs destination or Kinesis Data Firehose destination.</p>"""
    log_format: NotRequired["capo_elasticache.types.log_format.LogFormat"]
    """<p>Returns the log format, either JSON or TEXT</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PendingLogDeliveryConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "log_type" in value:
        import capo_elasticache.types.log_type

        capo_elasticache.types.log_type.serialize_query(
            value["log_type"], pairs, f"{key_prefix}LogType"
        )
    if "destination_type" in value:
        import capo_elasticache.types.destination_type

        capo_elasticache.types.destination_type.serialize_query(
            value["destination_type"], pairs, f"{key_prefix}DestinationType"
        )
    if "destination_details" in value:
        import capo_elasticache.types.destination_details

        capo_elasticache.types.destination_details.serialize_query(
            value["destination_details"], pairs, f"{key_prefix}DestinationDetails"
        )
    if "log_format" in value:
        import capo_elasticache.types.log_format

        capo_elasticache.types.log_format.serialize_query(
            value["log_format"], pairs, f"{key_prefix}LogFormat"
        )


def deserialize_query(el: Element) -> PendingLogDeliveryConfiguration:
    out: PendingLogDeliveryConfiguration = {}  # type: ignore[typeddict-item]
    child_log_type = el.find("LogType")
    if child_log_type is not None:
        import capo_elasticache.types.log_type

        out["log_type"] = capo_elasticache.types.log_type.deserialize_query(
            child_log_type
        )
    child_destination_type = el.find("DestinationType")
    if child_destination_type is not None:
        import capo_elasticache.types.destination_type

        out["destination_type"] = (
            capo_elasticache.types.destination_type.deserialize_query(
                child_destination_type
            )
        )
    child_destination_details = el.find("DestinationDetails")
    if child_destination_details is not None:
        import capo_elasticache.types.destination_details

        out["destination_details"] = (
            capo_elasticache.types.destination_details.deserialize_query(
                child_destination_details
            )
        )
    child_log_format = el.find("LogFormat")
    if child_log_format is not None:
        import capo_elasticache.types.log_format

        out["log_format"] = capo_elasticache.types.log_format.deserialize_query(
            child_log_format
        )
    return out
