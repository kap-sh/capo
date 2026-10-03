"""Generated from Smithy shape ``com.amazonaws.eventbridge#CreateEventBusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.dead_letter_config
    import capo_eventbridge.types.event_bus_description
    import capo_eventbridge.types.kms_key_identifier
    import capo_eventbridge.types.log_config
    import capo_eventbridge.types.string


class CreateEventBusResponse(TypedDict, closed=True):
    event_bus_arn: NotRequired["capo_eventbridge.types.string.String"]
    """<p>The ARN of the new event bus.</p>"""
    description: NotRequired[
        "capo_eventbridge.types.event_bus_description.EventBusDescription"
    ]
    """<p>The event bus description.</p>"""
    kms_key_identifier: NotRequired[
        "capo_eventbridge.types.kms_key_identifier.KmsKeyIdentifier"
    ]
    """<p>The identifier of the KMS customer managed key for EventBridge to use to encrypt events on this event bus, if one has been specified.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-encryption.html">Data encryption in EventBridge</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""
    dead_letter_config: NotRequired[
        "capo_eventbridge.types.dead_letter_config.DeadLetterConfig"
    ]
    log_config: NotRequired["capo_eventbridge.types.log_config.LogConfig"]
    """<p>The logging configuration settings for the event bus.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-logs.html">Configuring logs for event buses</a> in the <i>EventBridge User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEventBusResponse) -> dict:
    out: dict = {}
    if "event_bus_arn" in value:
        out["EventBusArn"] = value["event_bus_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "kms_key_identifier" in value:
        out["KmsKeyIdentifier"] = value["kms_key_identifier"]
    if "dead_letter_config" in value:
        import capo_eventbridge.types.dead_letter_config

        out["DeadLetterConfig"] = (
            capo_eventbridge.types.dead_letter_config.serialize_aws_json_1_1(
                value["dead_letter_config"]
            )
        )
    if "log_config" in value:
        import capo_eventbridge.types.log_config

        out["LogConfig"] = capo_eventbridge.types.log_config.serialize_aws_json_1_1(
            value["log_config"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEventBusResponse:
    out: CreateEventBusResponse = {}  # type: ignore[typeddict-item]
    if data.get("EventBusArn") is not None:
        out["event_bus_arn"] = data["EventBusArn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("KmsKeyIdentifier") is not None:
        out["kms_key_identifier"] = data["KmsKeyIdentifier"]
    if data.get("DeadLetterConfig") is not None:
        import capo_eventbridge.types.dead_letter_config

        out["dead_letter_config"] = (
            capo_eventbridge.types.dead_letter_config.deserialize_aws_json_1_1(
                data["DeadLetterConfig"]
            )
        )
    if data.get("LogConfig") is not None:
        import capo_eventbridge.types.log_config

        out["log_config"] = capo_eventbridge.types.log_config.deserialize_aws_json_1_1(
            data["LogConfig"]
        )
    return out
