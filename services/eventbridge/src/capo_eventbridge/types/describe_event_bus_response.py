"""Generated from Smithy shape ``com.amazonaws.eventbridge#DescribeEventBusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.dead_letter_config
    import capo_eventbridge.types.event_bus_description
    import capo_eventbridge.types.kms_key_identifier
    import capo_eventbridge.types.log_config
    import capo_eventbridge.types.managed_by
    import capo_eventbridge.types.string
    import capo_eventbridge.types.timestamp


class DescribeEventBusResponse(TypedDict, closed=True):
    name: NotRequired["capo_eventbridge.types.string.String"]
    """<p>The name of the event bus. Currently, this is always <code>default</code>.</p>"""
    arn: NotRequired["capo_eventbridge.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the account permitted to write events to the current account.</p>"""
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
    policy: NotRequired["capo_eventbridge.types.string.String"]
    """<p>The policy that enables the external account to send events to your account.</p>"""
    log_config: NotRequired["capo_eventbridge.types.log_config.LogConfig"]
    """<p>The logging configuration settings for the event bus.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-logs.html">Configuring logs for event buses</a> in the <i>EventBridge User Guide</i>.</p>"""
    creation_time: NotRequired["capo_eventbridge.types.timestamp.Timestamp"]
    """<p>The time the event bus was created.</p>"""
    last_modified_time: NotRequired["capo_eventbridge.types.timestamp.Timestamp"]
    """<p>The time the event bus was last modified.</p>"""
    managed_by: NotRequired["capo_eventbridge.types.managed_by.ManagedBy"]
    """<p>If the event bus was created on behalf of your account by an Amazon Web Services service, this field displays the principal name of the service that created the event bus.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventBusResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
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
    if "policy" in value:
        out["Policy"] = value["policy"]
    if "log_config" in value:
        import capo_eventbridge.types.log_config

        out["LogConfig"] = capo_eventbridge.types.log_config.serialize_aws_json_1_1(
            value["log_config"]
        )
    if "creation_time" in value:
        import capo_eventbridge.types.timestamp

        out["CreationTime"] = capo_eventbridge.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_eventbridge.types.timestamp

        out["LastModifiedTime"] = (
            capo_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "managed_by" in value:
        out["ManagedBy"] = value["managed_by"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventBusResponse:
    out: DescribeEventBusResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
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
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    if data.get("LogConfig") is not None:
        import capo_eventbridge.types.log_config

        out["log_config"] = capo_eventbridge.types.log_config.deserialize_aws_json_1_1(
            data["LogConfig"]
        )
    if data.get("CreationTime") is not None:
        import capo_eventbridge.types.timestamp

        out["creation_time"] = (
            capo_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if data.get("LastModifiedTime") is not None:
        import capo_eventbridge.types.timestamp

        out["last_modified_time"] = (
            capo_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("ManagedBy") is not None:
        out["managed_by"] = data["ManagedBy"]
    return out
