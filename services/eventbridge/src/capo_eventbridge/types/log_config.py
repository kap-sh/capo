"""Generated from Smithy shape ``com.amazonaws.eventbridge#LogConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.include_detail
    import capo_eventbridge.types.level


class LogConfig(TypedDict, closed=True):
    include_detail: NotRequired["capo_eventbridge.types.include_detail.IncludeDetail"]
    """<p>Whether EventBridge include detailed event information in the records it generates. Detailed data can be useful for troubleshooting and debugging. This information includes details of the event itself, as well as target details.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-logs.html#eb-event-logs-data">Including detail data in event bus logs</a> in the <i>EventBridge User Guide</i>.</p>"""
    level: NotRequired["capo_eventbridge.types.level.Level"]
    """<p>The level of logging detail to include. This applies to all log destinations for the event bus.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-logs.html#eb-event-bus-logs-level">Specifying event bus log level</a> in the <i>EventBridge User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogConfig) -> dict:
    out: dict = {}
    if "include_detail" in value:
        import capo_eventbridge.types.include_detail

        out["IncludeDetail"] = (
            capo_eventbridge.types.include_detail.serialize_aws_json_1_1(
                value["include_detail"]
            )
        )
    if "level" in value:
        import capo_eventbridge.types.level

        out["Level"] = capo_eventbridge.types.level.serialize_aws_json_1_1(
            value["level"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LogConfig:
    out: LogConfig = {}  # type: ignore[typeddict-item]
    if data.get("IncludeDetail") is not None:
        import capo_eventbridge.types.include_detail

        out["include_detail"] = (
            capo_eventbridge.types.include_detail.deserialize_aws_json_1_1(
                data["IncludeDetail"]
            )
        )
    if data.get("Level") is not None:
        import capo_eventbridge.types.level

        out["level"] = capo_eventbridge.types.level.deserialize_aws_json_1_1(
            data["Level"]
        )
    return out
