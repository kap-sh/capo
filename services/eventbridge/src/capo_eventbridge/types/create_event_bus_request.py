"""Generated from Smithy shape ``com.amazonaws.eventbridge#CreateEventBusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridge.types.dead_letter_config
    import capo_eventbridge.types.event_bus_description
    import capo_eventbridge.types.event_bus_name
    import capo_eventbridge.types.event_source_name
    import capo_eventbridge.types.kms_key_identifier
    import capo_eventbridge.types.log_config
    import capo_eventbridge.types.tag_list


class CreateEventBusRequest(TypedDict, closed=True):
    name: "capo_eventbridge.types.event_bus_name.EventBusName"
    """<p>The name of the new event bus. </p> <p>Custom event bus names can't contain the <code>/</code> character, but you can use the <code>/</code> character in partner event bus names. In addition, for partner event buses, the name must exactly match the name of the partner event source that this event bus is matched to.</p> <p>You can't use the name <code>default</code> for a custom event bus, as this name is already used for your account's default event bus.</p>"""
    event_source_name: NotRequired[
        "capo_eventbridge.types.event_source_name.EventSourceName"
    ]
    """<p>If you are creating a partner event bus, this specifies the partner event source that the new event bus will be matched with.</p>"""
    description: NotRequired[
        "capo_eventbridge.types.event_bus_description.EventBusDescription"
    ]
    """<p>The event bus description.</p>"""
    kms_key_identifier: NotRequired[
        "capo_eventbridge.types.kms_key_identifier.KmsKeyIdentifier"
    ]
    """<p>The identifier of the KMS customer managed key for EventBridge to use, if you choose to use a customer managed key to encrypt events on this event bus. The identifier can be the key Amazon Resource Name (ARN), KeyId, key alias, or key alias ARN.</p> <p>If you do not specify a customer managed key identifier, EventBridge uses an Amazon Web Services owned key to encrypt events on the event bus.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys.html">Identify and view keys</a> in the <i>Key Management Service Developer Guide</i>. </p> <note> <p>Schema discovery is not supported for event buses encrypted using a customer managed key. EventBridge returns an error if: </p> <ul> <li> <p>You call <code> <a href="https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-discoverers.html#CreateDiscoverer">CreateDiscoverer</a> </code> on an event bus set to use a customer managed key for encryption.</p> </li> <li> <p>You call <code> <a href="https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_UpdatedEventBus.html">UpdatedEventBus</a> </code> to set a customer managed key on an event bus with schema discovery enabled.</p> </li> </ul> <p>To enable schema discovery on an event bus, choose to use an Amazon Web Services owned key. For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-encryption-event-bus-cmkey.html">Encrypting events</a> in the <i>Amazon EventBridge User Guide</i>.</p> </note> <important> <p>If you have specified that EventBridge use a customer managed key for encrypting the source event bus, we strongly recommend you also specify a customer managed key for any archives for the event bus as well. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/encryption-archives.html">Encrypting archives</a> in the <i>Amazon EventBridge User Guide</i>.</p> </important>"""
    dead_letter_config: NotRequired[
        "capo_eventbridge.types.dead_letter_config.DeadLetterConfig"
    ]
    log_config: NotRequired["capo_eventbridge.types.log_config.LogConfig"]
    """<p>The logging configuration settings for the event bus.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-logs.html">Configuring logs for event buses</a> in the <i>EventBridge User Guide</i>.</p>"""
    tags: NotRequired["capo_eventbridge.types.tag_list.TagList"]
    """<p>Tags to associate with the event bus.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEventBusRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "event_source_name" in value:
        out["EventSourceName"] = value["event_source_name"]
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
    if "tags" in value:
        import capo_eventbridge.types.tag_list

        out["Tags"] = capo_eventbridge.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEventBusRequest:
    out: CreateEventBusRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateEventBusRequest.name required")
    if data.get("EventSourceName") is not None:
        out["event_source_name"] = data["EventSourceName"]
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
    if data.get("Tags") is not None:
        import capo_eventbridge.types.tag_list

        out["tags"] = capo_eventbridge.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
